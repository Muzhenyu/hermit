from django.contrib.auth.backends import ModelBackend
import re
from . import constants
from . import models
from django.contrib.auth.hashers import check_password


class LibUserPhoneAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            if re.match(constants.string_test_phonenum,username):
                libraryuser=models.libraryUser.objects.get(phone=username)
            else:
                libraryuser=models.libraryUser.objects.get(username=username)
        except models.libraryUser.DoesNotExist:
            libraryuser =None



        if libraryuser is not None and password==libraryuser.password:
            print('#########')
            return libraryuser
        # else:
        #     print('password failed')
        #     return user
def jwt_response_username_userid_token(token,libraryuser=None,request=None):
    data={
        'token':token,
        'username':libraryuser.username,
        'user_id':libraryuser.id
    }
    return data