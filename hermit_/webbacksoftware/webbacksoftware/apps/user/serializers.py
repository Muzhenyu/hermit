from rest_framework import serializers
from django_redis import get_redis_connection
from . import models
import re
from . import constants
from rest_framework_jwt.settings import api_settings
from itsdangerous import TimedJSONWebSignatureSerializer as ts
from django.conf import settings
from django.core.mail import send_mail
from celery_tasks.email.tasks import sendmail
from libraries.models import library



class Img_CodeSerializer(serializers.Serializer):
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
        flag = redis_con_obj.get('%s_flag' % phone)
        if flag:
            raise serializers.ValidationError('do not send code until 1 minutes later')

        return attrs

class RegisterSerializer(serializers.ModelSerializer):
    v_password=serializers.CharField(label='vertified_password',write_only=True)
    msg_code=serializers.CharField(label='phonecheckcode',write_only=True)
    protocal = serializers.CharField(label='protocal',write_only=True)
    token=serializers.CharField(label='JWT_token',read_only=True)

    class Meta:
        model =models.User
        fields =('id','username','password','email','phone','v_password','msg_code','protocal','token')

    def validate(self, attrs):

        protocal=attrs['protocal']
        print(protocal)
        if(protocal=='bad'):
            raise serializers.ValidationError('must agree protocal to be a user')

        username1=attrs['username']
        if(re.match(constants.string_test_username,username1)==None):
            raise serializers.ValidationError('not a valiable username')
        phonenum=attrs['phone']
        msg_code=attrs['msg_code']
        redis_con_obj1=get_redis_connection('valid')
        print(phonenum)
        correct_phone_code=redis_con_obj1.get('%s'%phonenum+'_msg')
        correct_phone_code = correct_phone_code.decode()
        print('true phone check code:',correct_phone_code)
        if(correct_phone_code!=msg_code):
            raise serializers.ValidationError('invaliable phone message check code')
        return attrs

    def create(self, validated_data):
        print("###############")
        print(validated_data)
        del validated_data['v_password']
        del validated_data['msg_code']
        del validated_data['protocal']
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        User = super().create(validated_data)
        # User.set_password(validated_data)
        User.save()

        payload = jwt_payload_handler(User)

        print('payload:', payload)
        token = jwt_encode_handler(payload)
        print('token:', token)
        User.token = token

        return User

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.User
        fields=('id','username','phone','email','img_url','is_library')

class EmailSendSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'email')

    def validate(self, attrs):
        # print(attrs['id'])
        return attrs

    def update(self, instance, validated_data):
        instance.email=validated_data['email']
        instance.save()
        idsfy=ts(settings.SECRET_KEY)
        print(idsfy)
        data={
            'user_id' :instance.id,
            'username':instance.username,
            'email':instance.email,
        }
        token=idsfy.dumps(data).decode()
        url='http://127.0.0.1:8000/email/vary/?token='+token
        url_str='<a href='+url+'>click to verify ur email</a>'
        #todo using celery
        print(instance)
        email_url=validated_data['email']
        print(email_url)
        # send_mail(subject='hermit email active', message=url_str, from_email=settings.EMAIL_FROM,
        #           recipient_list=[email_url], html_message=url_str)
        sendmail.delay(email_url, url_str)


        return instance

class AddressSerializer(serializers.ModelSerializer):
    street=serializers.StringRelatedField(read_only=True)
    district = serializers.StringRelatedField(read_only=True)

    street_id=serializers.IntegerField(required=True)
    district_id = serializers.IntegerField(required=True)
    class Meta:
        model=models.Address
        exclude=('user','is_delete')

    def create(self, validated_data):
        print('###################')
        print(self.context)
        print(self.context['request'].user)
        validated_data['user']=self.context['request'].user
        return super().create(validated_data)


class CollectSerializer(serializers.ModelSerializer):
    library_id=serializers.IntegerField()
    class Meta:
        model=models.collect_library
        fields=('library_id',)

    def validate(self, attrs):

        user_obj=self.context['request'].user
        lib_collect_obj=models.collect_library.objects.filter(user=user_obj.id)
        for i in lib_collect_obj:
            if i.library== attrs['library']:
                raise serializers.ValidationError('this library is already exist')
        lib_obj=library.objects.get(id=attrs['library_id'])
        attrs['library']=lib_obj
        return attrs

    def create(self, validated_data):
        del validated_data['library_id']
        validated_data['user']=self.context['request'].user
        return super().create(validated_data)
class get_user_idSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.User
        fields=('id',)



class CollectionSerializer(serializers.ModelSerializer):
    street=serializers.StringRelatedField()
    district=serializers.StringRelatedField()
    class Meta:
        model=library
        fields=('lib_img_url','name','grade','street','district','lib_commit','price','lib_info_url')

class get_user_nameSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.User
        fields=('first_name','last_name')
