from django.contrib.auth.backends import ModelBackend
import re
from . import constants
from . import models
from django.contrib.auth.hashers import check_password


class UserPhoneEmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print('#########')
        print(password)
        try:
            if re.match(constants.string_test_phonenum,username):
                user=models.User.objects.get(phone=username)
            elif re.match(constants.string_test_email,username):
                user=models.User.objects.get(email=username)
            else:
                user=models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            user =None



        if user is not None and password==user.password:
            print('#########')
            return user
        # else:
        #     print('password failed')
        #     return user
def jwt_response_username_userid_token(token,user=None,request=None):
    data={
        'token':token,
        'username':user.username,
        'user_id':user.id
    }

    return data