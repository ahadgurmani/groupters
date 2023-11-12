from django.urls import path, include
from rest_framework.routers import DefaultRouter

from GroupPosts.api.v1.viewsets import GroupPostViewset, SpecificGroupPostsList_Viewset, AllGroupsPostsList_Viewset

routers = DefaultRouter()
routers.register('create_GroupPost', GroupPostViewset, basename='create_grouppost')
routers.register('SpecificGroup_PostsList', SpecificGroupPostsList_Viewset, basename='specificGroup_PostsList')
routers.register('all_groupposts_list', AllGroupsPostsList_Viewset, basename='all_groupPosts')



urlpatterns = [
    path("", include(routers.urls)),
]