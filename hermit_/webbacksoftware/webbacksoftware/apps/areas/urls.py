from .views import AreasViewSet,AreasSearchView,showdistrictView,showstreetView
from rest_framework.routers import DefaultRouter
from django.conf.urls import url,include

urlpatterns = [
    url(r'^areasearch',AreasSearchView.as_view()),
    url(r'^district',showdistrictView.as_view()),
    url(r'^street',showstreetView.as_view()),
    url(r'^areasearch',AreasSearchView.as_view()),
]

router=DefaultRouter()
router.register('areas',AreasViewSet,base_name='areas')
urlpatterns +=router.urls