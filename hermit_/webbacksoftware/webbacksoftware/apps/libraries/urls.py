from django.conf.urls import url
from . import views
from rest_framework import routers

urlpatterns = [
    url(r'^getlibtype',views.acquire_type.as_view()),
    url(r'^captcha_aquired',views.ImageView.as_view()),
    url(r'^msg_code_aquire',views.lib_Msg_code.as_view()),
    url(r'^register',views.lib_registerView.as_view()),
    url(r'^logining/$',views.classify_obtain_jwt_token.as_view()),
    url(r'^createlib/$',views.add_library_view.as_view()),
    url(r'^showuserlibs',views.get_user_library.as_view()),
    url(r'^showlibs/',views.show_library_list.as_view()),
    url(r'^searchliblist/',views.search_library_list.as_view()),
    url(r'^lib_info/',views.lib_detail_info.as_view()),
    url(r'^lib_info_img/',views.lib_detail_page_img_list.as_view()),
    url(r'^createuser_comment',views.add_user_comment.as_view()),
    url(r'^showuser_comment/',views.show_user_comment.as_view()),
    url(r'^updatauserlibrary',views.updata_user_library.as_view()),
    url(r'^explored',views.explore_time.as_view()),
    url(r'^showexploretime',views.show_explore_time.as_view()),
    url(r'analysisexplore',views.explore_analysis.as_view())
]
# router=routers.DefaultRouter()
# router.register(r'showlibs',views.show_library_list,base_name='showlibs')
# urlpatterns+=router.urls