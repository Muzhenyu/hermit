from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,ListAPIView,DestroyAPIView
from . import constants
from webbacksoftware.libs.captcha import captcha
from django.http import HttpResponse
from django_redis import get_redis_connection
from . import serializers
from . import models
from celery_tasks.msg_code.tasks import sendmsg
from rest_framework.permissions import IsAuthenticated
from itsdangerous import TimedJSONWebSignatureSerializer as ts
from django.conf import settings
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins
from webbacksoftware.utils.fdfs import fdfs_storage
from libraries.models import library

import logging

import random

user_log=logging.getLogger(__name__)
user_log.info('user_log')
class ImageView(APIView):

    def get(self, request,image_id):

        text, image = captcha.captcha.generate_captcha()
        print(text)
        get_redis_connection('valid').setex(image_id,constants.IMAGE_UUID_REDIS_EXPIRES,text)
        return HttpResponse(image,content_type='image/jpg')

class Msg_code(GenericAPIView):
    serializer_class = serializers.Img_CodeSerializer

    def get(self,request):
        query_dict=request.query_params
        serializer=self.get_serializer(data=query_dict)
        serializer.is_valid(raise_exception=True)
        msg = '%04d' % random.randint(0, 9999)
        # 生成一个4位的验证码 '%04d'为这个4位数字补0
        print('msg_captcha', msg)
        redis_con_obj = get_redis_connection('valid')
        phone = query_dict['phone']
        redis_con_obj.setex('%s_msg' % phone, constants.PHONE_MSG_CODE_EXPIRES, msg)
        # 将验证码存入redis数据库，设置过期时间
        redis_con_obj.setex('%s_flag' % phone, constants.PHONE_FLAG_CODE_EXPIRES, 1)
        # 再给手机号码验证码设置一个验证过期时间的flag
        # ccp=CCP()
        # ret_data=ccp.send_template_sms(phone,[msg,'1'],1)
        # print(ret_data)
        sendmsg.delay(phone,msg)
        return HttpResponse('okay')

class RegisterView(CreateAPIView):

    serializer_class = serializers.RegisterSerializer

class LoginUserInfo(RetrieveAPIView):

    serializer_class = serializers.LoginSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        print(self.request.user)
        return self.request.user

class EmailSendView(UpdateAPIView):

    serializer_class = serializers.EmailSendSerializer
    permission_classes = (IsAuthenticated,)
    def get_object(self):
        return self.request.user


class emailvaryView(APIView):

    def get(self,request):
    	# 得到url中的token信息
        receive_token = request.query_params.get('token')
        print('#############email#########')
        print(receive_token)
        # 如果没有收到token报错
        if not receive_token:
            return Response({'err_msg:lack token'},status=401)
        #	新建一个isdangerous对象，将密钥传入
        ts_obj = ts(settings.SECRET_KEY)
        # 用带密钥的isdangerous对象解码传入token，注意两次密钥都是相同的
        data=ts_obj.loads(receive_token)
        print(data)
        # 获取token解码后的信息
        user_id=data['user_id']
        username= data['username']
        email = data['email']
        # 用信息获取用户对象
        user_obj=models.User.objects.get(id=user_id,username=username,email=email)
        print(user_obj)
        # 将用户对象中的字段信息修改并保存
        user_obj.active_email=True
        user_obj.save()
        return Response('Okay')


class AddressViewSet(ModelViewSet):

    serializer_class = serializers.AddressSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        print('inner')
        print(self.request.user.addresses.filter(is_delete=False))
        print(self.request.user)
        return self.request.user.addresses.filter(is_delete=False)

    def list(self,request):
        query_set=self.get_queryset()
        print(self.request.user)
        print(query_set)
        print(self.get_serializer(query_set,many=True))
        serializer_current=self.get_serializer(query_set,many=True)
        return Response({
            'address':serializer_current.data
        })


    def update(self, request, *args, **kwargs):
        obj=self.get_object()
        obj.is_delete=True
        obj.save()
        return Response('Okay')

class user_collect_lib(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.CollectSerializer

    def get_queryset(self):
        print('enter')
        user_id=self.request.user
        return user_id
class user_cancel_collection(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        user_obj=self.request.user
        library_id=request.data['library_id']
        lib_object=library.objects.get(id=library_id)
        collection=models.collect_library.objects.filter(library=lib_object).filter(user=user_obj)
        collection.delete()
        return Response('Okay')

class get_user_id(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.get_user_idSerializer
    def get_queryset(self):
        user_obj=self.request.user
        return [user_obj]
class User_collection_visit(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.CollectionSerializer
    def get_queryset(self):
        user_obj=self.request.user.id
        lib_obj=library.objects.filter(user_collect__id=user_obj)
        return lib_obj

class User_icon(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        user_obj=self.request.user
        fdfs=fdfs_storage.FastdfsStorageClass()
        ret=fdfs.save('mytest',request.data.get('img'))
        user_obj.img_url=ret
        user_obj.save()

        return Response(ret)

class acquire_user_name(RetrieveAPIView):
    serializer_class = serializers.get_user_nameSerializer
    def get_queryset(self):
        return models.User
