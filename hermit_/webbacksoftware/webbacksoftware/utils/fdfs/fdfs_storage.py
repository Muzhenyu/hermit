from django.core.files.storage import Storage
from django.conf import settings
from fdfs_client.client import Fdfs_client
from django.utils.deconstruct import deconstructible
from django.core.files import File, locks
import re

@deconstructible
class FastdfsStorageClass(Storage):
    def __init__(self,base_url=None,client_conf=None):
        # base_url will be used to combine the complete file and photo's url
        # client_conf fdfs's completed file url

        if base_url is None:
            base_url=settings.FDFS_URL

        if client_conf is None:
            client_conf=settings.FDFS_CLIENT_CONFIG
        self.base_url=base_url

        self.client_conf=client_conf

    def _open(self,name,mode):
        # will be used by Storage.open()
        pass

    def _save(self,name,content,html=None):
        # will be used by Storage.save()
        # name:file who will be saved's name

        client_obj=Fdfs_client(self.client_conf)
        print(type(content))

        if html==None:
            ret=client_obj.upload_by_buffer(content.read())

            if ret.get('Status')!='Upload successed.':
                raise Exception('upload failure')


            filename=ret.get('Remote file_id')

            return filename
        elif html==True:
            ret = client_obj.upload_by_filename(name)
            print(ret)

            if ret.get('Status') != 'Upload successed.':
                raise Exception('upload failure')

            filename = ret.get('Remote file_id')

            return filename
    def save(self, name, content, max_length=None,html=None):
        if html==None:
            return super().save(name,content,max_length)
        elif html==True:
            if name is None:
                name = content.name

            if not hasattr(content, 'chunks'):
                content = File(content, name)

            name = self.get_available_name(name, max_length=max_length)
            return self._save(name, content,html)

    def url(self,name):
        return self.base_url+name

    def exists(self, name):
        return False

    def delete(self, name):
        return print('okay')

    def list_all_groups(self):
        client = Fdfs_client(self.client_conf)
        return client.list_all_groups()