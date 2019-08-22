from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import library,libraryUser,User_to_lib,libType,Imglist,library_detail_info_page_model,Usercomment,explore_time
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt import utils
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from django_redis import get_redis_connection
from webbacksoftware.utils.fdfs import fdfs_storage
from areas.models import Areas
from . import constants
from django.db.models import Avg
import requests
import re
import datetime
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER

class get_libtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=libType
        fields=('id','type_name')


class lib_Img_CodeSerializer(serializers.Serializer):
    image_id = serializers.UUIDField()
    image_text = serializers.CharField(max_length=4, min_length=4)
    phone = serializers.CharField(max_length=11, min_length=11)

    def validate(self, attrs):
        image_id_uuid=attrs['image_id']
        image_input_text=attrs['image_text']
        phone=attrs['phone']

        redis_con_obj = get_redis_connection('valid')
        correct_image_text = redis_con_obj.get('%s' % image_id_uuid)
        correct_image_text = correct_image_text.decode()

        if (correct_image_text.lower() != image_input_text.lower()):
            raise serializers.ValidationError('captcha is not valiable')
        flag = redis_con_obj.get('%sLib_flag' % phone)
        if flag:
            raise serializers.ValidationError('do not send code until 1 minutes later')

        return attrs


class registerSerializer(ModelSerializer):
    v_password = serializers.CharField(label='vertified_password', write_only=True)
    msg_code = serializers.CharField(label='phonecheckcode', write_only=True)
    protocal = serializers.CharField(label='protocal', write_only=True)
    token = serializers.CharField(label='JWT_token', read_only=True)
    is_library = serializers.BooleanField(label='is_library')
    class Meta:
        model=libraryUser
        fields=('id','username','password','email','phone','v_password','msg_code','protocal','token','is_library')

    def validate(self, attrs):
        username=attrs.get('username')
        phone=attrs.get('phone')
        print(attrs)
        # try:
        #     if libraryUser.objects.get(username=username):
        #         raise serializers.ValidationError('user is already exist')
        # except Exception as e:
        #     print(e)
        password=attrs.get('password')
        v_password=attrs.get('v_password')
        if password!=v_password:
            raise serializers.ValidationError('vali_password error')
        msg_code=attrs.get('msg_code')
        redis_objs=get_redis_connection('valid')
        print(redis_objs.get('%sLib_msg' % phone))
        if msg_code!=redis_objs.get('%sLib_msg' % phone).decode():
            raise serializers.ValidationError('not correct msg_code')
        protocal=attrs.get('protocal')
        if protocal!= 'good':
            raise serializers.ValidationError('must agreed user protocal to continue')
        if attrs.get('is_library')!=True:
            raise serializers.ValidationError('this is lib register')
        return attrs


    def create(self, validated_data):
        print(validated_data)
        del validated_data['v_password']
        del validated_data['msg_code']
        del validated_data['protocal']
        lib_user=super().create(validated_data)
        lib_user.save()
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user=lib_user)
        print('payload:', payload)
        token = jwt_encode_handler(payload)
        print('token:', token)
        lib_user.token = token
        return lib_user




class LibJWTSerializer(JSONWebTokenSerializer):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        super().fields['is_libraryUser']=serializers.BooleanField()

    def validate(self, attrs):
        credentials = {
            super().username_field:attrs.get(super().username_field),
            'password': attrs.get('password'),
            'is_libraryUser':attrs.get('is_libraryUser'),
        }
        print(credentials)
        if all(credentials.values()):
            user = authenticate(**credentials)

            if user:
                if not user.is_active:
                    msg = ('User account is disabled.')
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user=user)

                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            else:
                msg = ('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = ('Must include "{username_field}" and "password".')
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)

class create_lib(serializers.ModelSerializer):
    lib_img=serializers.ImageField(label='lib_img',write_only=True)
    lib_license=serializers.ImageField(label='lib_license',write_only=True)
    class Meta:
        model=library
        fields=('name','street','district','lib_commit','lib_img','lib_license','detail_address','type','price','page_mode_id')
    def validate(self, attrs):
        print(attrs)

        print('######################')

        lib_img=attrs['lib_img']
        lib_license_img=attrs['lib_license']
        img_storage=fdfs_storage.FastdfsStorageClass()
        print(type(lib_img.name))
        print(type(lib_license_img.name))
        if re.match(pattern=constants.img_file_pattern,string=lib_img.name):
            attrs['lib_img_url']=img_storage.save('lib_img',lib_img)
        else:
            raise serializers.ValidationError('this is not a valid photofile,please use *.jpg or *.png')
        if re.match(pattern=constants.img_file_pattern,string=lib_license_img.name):
            attrs['lib_license_url'] = img_storage.save('lib_license', lib_license_img)
        else:
            raise serializers.ValidationError('this is not a valid photofile,please use *.jpg or *.png')
        print(attrs['page_mode_id'])
        html_page_model = library_detail_info_page_model.objects.get(id=attrs['page_mode_id'])
        html_page=requests.get(url='http://127.0.0.1:8888/'+str(html_page_model.page_model)).text
        filename=attrs['name']+'.html'
        f=open('/home/lvbu89757/Desktop/hermit_/hermit/'+filename,'w+')
        f.write(html_page)
        f.close()
        attrs['lib_info_url'] = filename
        return attrs

    def create(self, validated_data):
        del validated_data['lib_img']
        del validated_data['lib_license']
        library=super().create(validated_data)
        User_obj=self.context['request'].user

        libuser=User_to_lib(User_obj)
        print(libuser)
        libuser.own_library=library
        libuser.save()
        return library

class none_user_lib_serializers(serializers.Serializer):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)




class show_user_lib_serializers(serializers.ModelSerializer):
    street = serializers.StringRelatedField(read_only=True)
    district = serializers.StringRelatedField(read_only=True)
    class Meta:
        model=library
        fields='__all__'



class showliblistSerializer(serializers.ModelSerializer):
    street = serializers.StringRelatedField(read_only=True)
    district = serializers.StringRelatedField(read_only=True)
    class Meta:
        model=library
        fields=('lib_img_url','name','grade','street','district','lib_commit','price','lib_info_url')


class showlibdetailpageSerializer(serializers.ModelSerializer):
    street = serializers.StringRelatedField(read_only=True)
    district = serializers.StringRelatedField(read_only=True)
    class Meta:
        model=library
        exclude=('lib_license_url','lib_info_url','page_mode_id')

class showlibdetailimgSerializer(serializers.ModelSerializer):
    class Meta:
        model=Imglist
        fields=('img_url',)
class add_user_commentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usercomment
        fields=('library_id','User_comment','User_grade')

    def validate(self, attrs):
        print(attrs)
        if attrs['User_grade']>10.0:
            raise serializers.ValidationError('can not add grade more than 10')
        user_obj=self.context['request'].user
        attrs['user_id']=user_obj.id
        return attrs
    def create(self, validated_data):
        lib_obj=library.objects.get(id=validated_data['library_id'])
        comment_avg=Usercomment.objects.filter(library_id=validated_data['library_id']).aggregate(Avg('User_grade'))
        print(comment_avg['User_grade__avg'])
        comment_sum=Usercomment.objects.filter(library_id=validated_data['library_id']).count()
        print(comment_sum)
        if comment_avg['User_grade__avg']==None:
            grade_ave=0
        if comment_avg['User_grade__avg']!=None:
            grade_ave=comment_avg['User_grade__avg']
        lib_obj.grade=(grade_ave*comment_sum+validated_data['User_grade'])/(comment_sum+1)
        lib_obj.save()
        return super().create(validated_data)


class show_user_commentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usercomment
        fields='__all__'


class explore_timeSerializer(serializers.ModelSerializer):
    class Meta:
        model=explore_time
        fields=('library_id',)

    def validate(self, attrs):
        now=datetime.datetime.now()
        attrs['explore_data_time']=now
        return attrs

    def create(self, validated_data):
        return super().create(validated_data)