from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,GenericAPIView,UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from django_redis import get_redis_connection
from django.http import HttpResponse,JsonResponse
from .models import library,libraryUser,User_to_lib,libType,Imglist,Usercomment,library_detail_info_page_model,explore_time as explrtm
from . import constants
from rest_framework_jwt.views import ObtainJSONWebToken
from .serializers import LibJWTSerializer,registerSerializer,lib_Img_CodeSerializer,create_lib,showliblistSerializer\
    ,show_user_lib_serializers,none_user_lib_serializers,get_libtypeSerializer,showlibdetailpageSerializer,showlibdetailimgSerializer,\
    show_user_commentSerializer,add_user_commentSerializer,explore_timeSerializer
from webbacksoftware.libs.captcha import captcha
from celery_tasks.msg_code.tasks import sendmsg
from .self_define_permission import lib_permission
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from webbacksoftware.utils import selfdefineexpection
from webbacksoftware.utils.fdfs.fdfs_storage import FastdfsStorageClass
from areas.models import Areas
from pyecharts.charts import Bar
from pyecharts import options as opts
from django.db import connection
import pymysql
import random
import re
import requests
import os
import json
import datetime
# Create your views here.
import logging
library_log=logging.getLogger(__name__)
library_log.info('library_log')
class acquire_type(ListAPIView):
    serializer_class = get_libtypeSerializer
    def get_queryset(self):
        return libType.objects.all()

class ImageView(APIView):

    def get(self, request):
        print(request.query_params['image_id'])
        text, image = captcha.captcha.generate_captcha()
        print(text)
        get_redis_connection('valid').setex(request.query_params['image_id'],constants.IMAGE_UUID_REDIS_EXPIRES,text)
        return HttpResponse(image,content_type='image/jpg')

class lib_Msg_code(GenericAPIView):
    serializer_class = lib_Img_CodeSerializer

    def get(self,request):
        query_dict=request.query_params
        serializer=self.get_serializer(data=query_dict)
        serializer.is_valid(raise_exception=True)
        msg = '%04d' % random.randint(0, 9999)
        # 生成一个4位的验证码 '%04d'为这个4位数字补0
        print('msg_captcha', msg)
        redis_con_obj = get_redis_connection('valid')
        phone = query_dict['phone']
        redis_con_obj.setex('%sLib_msg' % phone, constants.PHONE_MSG_CODE_EXPIRES, msg)
        # 将验证码存入redis数据库，设置过期时间
        redis_con_obj.setex('%sLib_flag' % phone, constants.PHONE_FLAG_CODE_EXPIRES, 1)
        # 再给手机号码验证码设置一个验证过期时间的flag
        # ccp=CCP()
        # ret_data=ccp.send_template_sms(phone,[msg,'1'],1)
        # print(ret_data)
        sendmsg.delay(phone,msg)
        return HttpResponse('okay')



class lib_registerView(CreateAPIView):
    serializer_class = registerSerializer


class classify_obtain_jwt_token(ObtainJSONWebToken):
    serializer_class = LibJWTSerializer
    def post(self, request, *args, **kwargs):
        print(request.data)
        return super().post(request,*args,**kwargs)


class add_library_view(CreateAPIView):
    permission_classes = [lib_permission]

    def get_serializer_class(self):
        print('#######enter###')
        return create_lib

class get_user_library(ListAPIView):
    permission_classes = [lib_permission]

    def get_queryset(self):
        lib_obj=User_to_lib(self.request.user)
        print(lib_obj.own_library)
        return [lib_obj.own_library]

    def get_serializer_class(self):
        if self.get_queryset()[0]==None:
            return none_user_lib_serializers
        elif self.get_queryset()[0]!=None:
            return show_user_lib_serializers

class show_library_list(ListAPIView):
    serializer_class = showliblistSerializer
    def get_queryset(self):
        params=self.request.query_params
        # print(params)
        lib_obj=library.objects.order_by('?')[:4]
        return lib_obj

class search_library_list(ListAPIView):
    serializer_class = showliblistSerializer
    def get_queryset(self):
        libtype_id=self.request.query_params['libtypesearch_id']
        district_id=self.request.query_params['districtsearch_id']
        street_id=self.request.query_params['streetsearch_id']
        price=self.request.query_params['price']
        if libtype_id=='' and district_id=='' and street_id=='' and price=='':
            lib_obj=library.objects.order_by('?')[:4]
        if libtype_id=='' and district_id=='' and street_id!='' and price=='':
            lib_obj=library.objects.filter(street=street_id).order_by('?')[:4]
        if libtype_id=='' and district_id!='' and street_id=='' and price=='':
            lib_obj=library.objects.filter(district=district_id).order_by('?')[:4]
        if libtype_id=='' and district_id!='' and street_id!='' and price=='':
            lib_obj=library.objects.filter(district=district_id).filter(street=street_id).order_by('?')[:4]
        if libtype_id!='' and district_id=='' and street_id=='' and price=='':
            lib_obj=library.objects.filter(type=libtype_id).order_by('?')[:4]
        if libtype_id!='' and district_id=='' and street_id!='' and price=='':
            lib_obj=library.objects.filter(type=libtype_id).filter(street=street_id).order_by('?')[:4]
        if libtype_id!='' and district_id!='' and street_id=='' and price=='':
            lib_obj=library.objects.filter(type=libtype_id).filter(district=district_id).order_by('?')[:4]
        if libtype_id!='' and district_id!='' and street_id!='' and price=='':
            lib_obj=library.objects.filter(type=libtype_id).filter(district=district_id).filter(street=street_id).order_by('?')[:4]


        if libtype_id=='' and district_id=='' and street_id=='' and price!='':
            lib_obj=self.price_search_method(price).order_by('?')[:4]
        if libtype_id=='' and district_id=='' and street_id!='' and price!='':
            lib_obj=self.price_search_method(price).filter(street=street_id).order_by('?')[:4]
        if libtype_id=='' and district_id!='' and street_id=='' and price!='':
            lib_obj=self.price_search_method(price).filter(district=district_id).order_by('?')[:4]
        if libtype_id=='' and district_id!='' and street_id!='' and price!='':
            lib_obj=self.price_search_method(price).filter(district=district_id).filter(street=street_id).order_by('?')[:4]
        if libtype_id!='' and district_id=='' and street_id=='' and price!='':
            lib_obj=self.price_search_method(price).filter(type=libtype_id).order_by('?')[:4]
        if libtype_id!='' and district_id=='' and street_id!='' and price!='':
            lib_obj=self.price_search_method(price).filter(type=libtype_id).filter(street=street_id).order_by('?')[:4]
        if libtype_id!='' and district_id!='' and street_id=='' and price!='':
            lib_obj=self.price_search_method(price).filter(type=libtype_id).filter(district=district_id).order_by('?')[:4]
        if libtype_id!='' and district_id!='' and street_id!='' and price!='':
            lib_obj=self.price_search_method(price).filter(type=libtype_id).filter(district=district_id).filter(street=street_id).order_by('?')[:4]
        return lib_obj
    def price_search_method(self,price):
        pattern = '[0-9]\d*|<|>|-'
        price_tag = re.findall(pattern=pattern, string=price)
        price_number=[]
        situation=0
        print(price_tag)
        for i in price_tag:
            if i=='-':
                situation=1
            if i=='<':
                situation=2
            if i=='>':
                situation=3
            if i!='-' and i!='<' and i!='>':
                price_number.append(i)
        print(situation)
        if situation==1:
            search_condition1=price_number[0]
            search_condition2=price_number[1]
            search_condition=(search_condition1,search_condition2)
            return library.objects.filter(price__range=search_condition)

        if situation==2:
            search_condition=price_number[0]
            return library.objects.filter(price__lt=search_condition)
        if situation==3:
            search_condition=price_number[0]
            return library.objects.filter(price__gte=search_condition)

class lib_detail_info(ListAPIView):
    serializer_class = showlibdetailpageSerializer
    def get_queryset(self):

        library_page_url=self.request.query_params['library_page_url']

        library_page_url_tolist=list(library_page_url)
        del library_page_url_tolist[0]
        true_libray_page_url=''
        for i in library_page_url_tolist:
            true_libray_page_url=true_libray_page_url+i

        lib_obj=library.objects.filter(lib_info_url=true_libray_page_url)

        return lib_obj


class lib_detail_page_img_list(ListAPIView):
    serializer_class = showlibdetailimgSerializer
    def get_queryset(self):
        library_page_url=self.request.query_params['library_page_url']
        lib_obj=library.objects.filter(lib_info_url=library_page_url)
        img_list_obj=Imglist.objects.filter(id=lib_obj.id)
        return img_list_obj

class add_user_comment(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = add_user_commentSerializer


class show_user_comment(ListAPIView):
    serializer_class = show_user_commentSerializer
    def get_queryset(self):
        lib_id=self.request.query_params['library_id']
        Usercomment_obj=Usercomment.objects.filter(library_id=lib_id)
        return Usercomment_obj

class explore_time(CreateAPIView):
    serializer_class = explore_timeSerializer

class show_explore_time(APIView):
    def get(self,request):
        library_id=self.request.query_params['library_id']
        exploretime=explrtm.objects.filter(library_id=library_id).count()
        data={}
        data['exploretime']=exploretime

        return JsonResponse(data=data)



class updata_user_library(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        user_obj=self.request.user
        data_query=request.data

        lib_user_obj=User_to_lib(user_obj)
        library_obj=lib_user_obj.own_library
        newlib=self.updata_one_or_more(library_obj,**data_query)
        newlib.save()

        return Response('okay')

    def updata_one_or_more(self,library,**kwargs):
        fdfs_storage=FastdfsStorageClass()
        if kwargs['name']!=['']:
            os.rename('/home/lvbu89757/Desktop/hermit_/hermit/'+library.name+'.html','/home/lvbu89757/Desktop/hermit_/hermit/'+kwargs['name'][0]+'.html')
            library.name=kwargs['name'][0]
        if kwargs['street']!=['']:
            library.street=Areas.objects.get(id=kwargs['street'][0])
        if kwargs['district']!=['']:
            library.district=Areas.objects.get(id=kwargs['district'][0])
            if kwargs['street']==['']:
                raise selfdefineexpection.Not_exist('could not add without choose any street')
        if kwargs['detail_address']!=['']:
            library.detail_address=kwargs['detail_address'][0]
        if kwargs['price']!=['']:
            library.price=kwargs['price'][0]
        if kwargs['lib_img']!=['']:
            img_url=fdfs_storage.save('imglist',kwargs['lib_img'][0])
            library.lib_img_url=img_url
        if kwargs['lib_commit']!=['']:
            library.lib_commit=kwargs['lib_comment'][0]
        if kwargs['lib_license']!=['']:
            license_url=fdfs_storage.save('licenseurl',kwargs['lib_license'][0])
            library.lib_license_url=license_url
        if kwargs['type']!=['']:
            library.type=kwargs['type'][0]
        if kwargs['page_mode_id']!=['']:
            html_page_model=library_detail_info_page_model.objects.get(id=kwargs['page_mode_id'][0])
            html_page = requests.get(url='http://127.0.0.1:8888/' + str(html_page_model.page_model)).text
            if kwargs['name']!=['']:
                filename = kwargs['name'][0] + '.html'
            elif kwargs['name']==['']:
                filename = library.name+'.html'
            f = open('/home/lvbu89757/Desktop/hermit_/hermit/' + filename, 'w+')
            f.write(html_page)
            f.close()
            library.lib_info_url=filename
            library.page_mode_id=kwargs['page_mode_id'][0]
        return library

def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error


class explore_analysis(APIView):
    permission_classes = [lib_permission]
    def bar_base(self,x,y):
        c = (
            Bar()
            .add_xaxis(x)
            .add_yaxis("访问次数", y)
            .set_global_opts(title_opts=opts.TitleOpts(title=str(datetime.datetime.now().year)+"月访问次数分析图"))
            .dump_options()
        )
        return c

    def get(self,request):
        user_obj=self.request.user
        lib_user_obj=User_to_lib(user_obj)
        library_id=str(lib_user_obj.own_library.id)
        conn=pymysql.connect(host='localhost',user='debian-sys-maint',password='NMwBmsUQgRgTWqFM',database='groupwork',charset='utf8')
        cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute('select count(*) from libraries_explore_time where library_id=' + library_id + ' and month(explore_data_time)=1 and year(explore_data_time)='+str(datetime.datetime.now().year))
        Jan_explore_times=cursor.fetchall()
        cursor.execute('select count(*) from libraries_explore_time where library_id=' + library_id + ' and month(explore_data_time)=2 and year(explore_data_time)='+str(datetime.datetime.now().year))
        Feb_explore_times = cursor.fetchall()
        cursor.execute('select count(*) from libraries_explore_time where library_id=' + library_id + ' and month(explore_data_time)=3 and year(explore_data_time)='+str(datetime.datetime.now().year))
        Mar_explore_times = cursor.fetchall()
        cursor.execute('select count(*) from libraries_explore_time where library_id=' + library_id + ' and month(explore_data_time)=4 and year(explore_data_time)='+str(datetime.datetime.now().year))
        Apr_explore_times = cursor.fetchall()
        cursor.execute('select count(*) from libraries_explore_time where library_id=' + library_id + ' and month(explore_data_time)=5 and year(explore_data_time)='+str(datetime.datetime.now().year))
        May_explore_times = cursor.fetchall()
        cursor.execute('select count(*) from libraries_explore_time where library_id=' + library_id + ' and month(explore_data_time)=6 and year(explore_data_time)='+str(datetime.datetime.now().year))
        June_explore_times = cursor.fetchall()
        cursor.execute('select count(*) from libraries_explore_time where library_id=' + library_id + ' and month(explore_data_time)=7 and year(explore_data_time)='+str(datetime.datetime.now().year))
        July_explore_times = cursor.fetchall()
        cursor.execute('select count(*) from libraries_explore_time where library_id=' + library_id + ' and month(explore_data_time)=8 and year(explore_data_time)='+str(datetime.datetime.now().year))
        Aug_explore_times=cursor.fetchall()
        cursor.execute('select count(*) from libraries_explore_time where library_id=' + library_id + ' and month(explore_data_time)=9 and year(explore_data_time)='+str(datetime.datetime.now().year))
        Sep_explore_times = cursor.fetchall()
        cursor.execute('select count(*) from libraries_explore_time where library_id=' + library_id + ' and month(explore_data_time)=10 and year(explore_data_time)='+str(datetime.datetime.now().year))
        Oct_explore_times = cursor.fetchall()
        cursor.execute('select count(*) from libraries_explore_time where library_id=' + library_id + ' and month(explore_data_time)=11 and year(explore_data_time)='+str(datetime.datetime.now().year))
        Nov_explore_times = cursor.fetchall()
        cursor.execute('select count(*) from libraries_explore_time where library_id=' + library_id + ' and month(explore_data_time)=12 and year(explore_data_time)='+str(datetime.datetime.now().year))
        Dec_explore_times = cursor.fetchall()
        cursor.close()
        explore_times=[Jan_explore_times[0]['count(*)'],Feb_explore_times[0]['count(*)'],Mar_explore_times[0]['count(*)'],Apr_explore_times[0]['count(*)'],May_explore_times[0]['count(*)'],June_explore_times[0]['count(*)'],
                       July_explore_times[0]['count(*)'],Aug_explore_times[0]['count(*)'],Sep_explore_times[0]['count(*)'],Oct_explore_times[0]['count(*)'],Nov_explore_times[0]['count(*)'],Dec_explore_times[0]['count(*)']]
        xlabel=['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月']
        photo=self.bar_base(x=xlabel,y=explore_times)
        return JsonResponse(json.loads(photo))

