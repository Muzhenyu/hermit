from rest_framework.permissions import IsAuthenticated
from webbacksoftware.utils.selfdefineexpection import not_library_user_error
from .models import libraryUser

class lib_permission(IsAuthenticated):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_library)
