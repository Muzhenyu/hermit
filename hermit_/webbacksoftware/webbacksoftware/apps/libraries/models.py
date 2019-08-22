from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from user.models import User
from webbacksoftware.utils.selfdefineexpection import not_library_user_error,not_User_obj_error


class library(models.Model):
    name=models.CharField(max_length=20,unique=True)
    street=models.ForeignKey('areas.Areas',on_delete=models.PROTECT,related_name='lib_street_addresses',verbose_name='street',default=None)
    district = models.ForeignKey('areas.Areas', on_delete=models.PROTECT, related_name='lib_district_addresses',verbose_name='district',default=None)
    grade=models.FloatField(default=0.0)
    detail_address=models.CharField(max_length=200,default='')
    price=models.FloatField(default=0.0)
    lib_img_url=models.CharField(max_length=100,verbose_name='img_url of the lib',null=True)
    lib_commit=models.CharField(max_length=300,verbose_name='commit of the lib')
    user_collect=models.ManyToManyField('user.User',through='user.collect_library')
    lib_license_url=models.CharField(max_length=100,verbose_name='lib_license_url',default='')
    type=models.IntegerField(null=True)
    lib_info_url=models.CharField(max_length=100,default='')
    page_mode_id=models.IntegerField(default=1)

    class Meta:
        db_table = 'libraries'
        verbose_name = 'library'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class libraryUser(User):
    own_library=models.OneToOneField(library,on_delete=models.CASCADE,related_name='libUser',verbose_name='libUser',null=True,blank=True)
    def __str__(self):
        return self.username

class Usercomment(models.Model):
    library_id=models.IntegerField(null=False)
    user_id=models.IntegerField(null=False)
    User_comment=models.CharField(max_length=500)
    User_grade=models.IntegerField(null=False)

class libType(models.Model):
    type_name=models.CharField(max_length=15,unique=True)
    type_description=models.CharField(max_length=200)

class Imglist(models.Model):
    library_id=models.IntegerField(null=False)
    img_url=models.CharField(max_length=100,null=True)

class library_detail_info_page_model(models.Model):
    page_model_views_url=models.CharField(max_length=100)
    page_model=models.FileField()

class imgsave(models.Model):
    img=models.ImageField()

class explore_time(models.Model):
    library_id=models.IntegerField()
    explore_data_time=models.DateTimeField()

def User_to_lib(User_obj):
    ret=isinstance(User_obj,User)
    if ret==True:
        if User_obj.is_library==True:
            libUserObject=libraryUser.objects.get(id=User_obj.id)
            return libUserObject
        elif User_obj.is_library==False:
            raise not_library_user_error('this is not a libraryUser')
    else:
        raise not_User_obj_error('this is not a user_obj')