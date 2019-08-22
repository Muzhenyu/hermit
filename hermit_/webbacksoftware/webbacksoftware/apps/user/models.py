from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from ckeditor_uploader.fields import RichTextUploadingField

# class BaseUser(AbstractUser):
#     is_library = models.BooleanField(default=False, verbose_name='islibraryuser')
#     class Meta:
#         abstract=True


class User(AbstractUser):

    phone=models.CharField(max_length=11,unique=True,verbose_name='phonenum',default='')
    active_email = models.BooleanField(default=False, verbose_name='activate email')
    img_url=models.CharField(max_length=100,verbose_name='img_url',default='group1/M00/00/02/wKjTiV1TbM2AZB2bAAANkt5fqtM4440190')
    is_library = models.BooleanField(default=False, verbose_name='islibraryuser')
    class Meta:
        db_table='gw_user'
        verbose_name = 'user'
        verbose_name_plural = verbose_name


class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='addresses',verbose_name='user')
    street=models.ForeignKey('areas.Areas',on_delete=models.PROTECT,related_name='street_addresses',verbose_name='street',default=None)
    district = models.ForeignKey('areas.Areas', on_delete=models.PROTECT, related_name='district_addresses',verbose_name='district',default=None)
    is_delete=models.BooleanField(default=False,verbose_name='check_if_address_is_delete_or_not')

    class Meta:
        db_table='hermit_user_address'
        verbose_name='User_address'
        verbose_name_plural=verbose_name


class collect_library(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='collected_library',verbose_name='user')
    library=models.ForeignKey('libraries.library',on_delete=models.CASCADE,related_name='user_collected_library',verbose_name='library')

    def __str__(self):
        return self.library.name
