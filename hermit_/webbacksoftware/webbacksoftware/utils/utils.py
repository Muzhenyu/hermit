from django.contrib.auth.backends import ModelBackend
import re
from . import constants
from user.models import User
from libraries.models import libraryUser
from django.contrib.auth.hashers import check_password
from . import selfdefineexpection


class UserPhoneEmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print('#########')
        print(password)
        print(kwargs.get('is_libraryUser'))
        if kwargs.get('is_libraryUser')==None:
            try:
                if re.match(constants.string_test_phonenum,username):
                    user=User.objects.get(phone=username)
                elif re.match(constants.string_test_email,username):
                    user=User.objects.get(email=username)
                else:
                    user=User.objects.get(username=username)
            except User.DoesNotExist:
                user =None

            if user is not None and password==user.password:
                print('#########')
                return user
        elif kwargs.get('is_libraryUser')==True:
            print(libraryUser.objects.all())

            try:
                if re.match(constants.string_test_phonenum, username):
                    user = libraryUser.objects.get(phone_num=username)
                elif re.match(constants.string_test_email,username):
                    user=libraryUser.objects.get(email=username)
                else:
                    user = libraryUser.objects.get(username=username)
            except libraryUser.DoesNotExist:
                user = None

            if user is not None and user.is_library == False:
                raise selfdefineexpection.not_library_user_error('you are not a library user')



            if user is not None and password == user.password:
                print('#########')
                return user
        # else:
        #     print('password failed')
        #     return user
def jwt_response_username_userid_token(token,user=None,request=None):
        data={
            'token':token,
            'username':user.username,
            'user_id':user.id,
            'is_library':user.is_library
        }
        return data