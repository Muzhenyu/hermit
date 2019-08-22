from django.conf.urls import url,include
from . import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'^imgcode/(?P<image_id>[\w-]+)/$',views.ImageView.as_view()),
    url(r'^users/msg_code/$',views.Msg_code.as_view()),
    url(r'^register/$',views.RegisterView.as_view()),
    url(r'^logining/$',obtain_jwt_token),
    url(r'^loginuser/',views.LoginUserInfo.as_view()),
    url(r'^email/$',views.EmailSendView.as_view()),
    url(r'^email/vary/$',views.emailvaryView.as_view()),
    url(r'^usercollectlib',views.user_collect_lib.as_view()),
    url(r'^usercollection',views.User_collection_visit.as_view()),
    url(r'^usericon',views.User_icon.as_view()),
    url(r'^getuserid',views.get_user_id.as_view()),
    url(r'^cancel_collection',views.user_cancel_collection.as_view()),
    url(r'^show_user_name/(?P<pk>[^/.]+)/',views.acquire_user_name.as_view())
]

router=DefaultRouter()
router.register(r'addresses',views.AddressViewSet,base_name='addresses')
urlpatterns +=router.urls