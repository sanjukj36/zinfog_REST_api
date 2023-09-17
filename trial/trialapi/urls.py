# shop/urls.py

from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
# from .trialapi.views import UserViewset
from .views import UserViewset
app_name = 'trialapi'
urlpatterns = [

]
router=DefaultRouter()
router.register('register', UserViewset, basename='user')

urlpatterns+=router.urls