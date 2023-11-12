from rest_framework.routers import DefaultRouter
from .viewsets import UserSignupViewset, UserLoginViewset, AllUsersViewset
from django.urls import path,include


routers = DefaultRouter()
routers.register('User_Signup', UserSignupViewset, basename='userSignup')
routers.register('User_Login', UserLoginViewset, basename='userLogin')
routers.register('all_users', AllUsersViewset, basename='allusers')




urlpatterns = [
    path("", include(routers.urls)),
]