from django.contrib import admin
from . import models
import logging
# Register your models here.
auths_log=logging.getLogger('auths')
auths_log.debug('auth_log')
admin.site.register(models.library)
admin.site.register(models.libraryUser)
admin.site.register(models.libType)
admin.site.register(models.library_detail_info_page_model)
admin.site.register(models.Usercomment)
admin.site.register(models.imgsave)
admin.site.register(models.explore_time)