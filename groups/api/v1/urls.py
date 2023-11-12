from django.urls import path,include
from rest_framework.routers import DefaultRouter

from groups.api.v1.viewsets import CreateGroupViewset, AllGroupList_Viewset, RequestedUserList, \
    RequestedUserJoined_Groups, GroupProfileImgChange_Viewset, GroupEdit_Viewset

routers = DefaultRouter()
routers.register('create_group', CreateGroupViewset, basename='group_create')
routers.register('list_all_groups', AllGroupList_Viewset, basename='list_all_group')
routers.register('list_requested_user', RequestedUserList, basename='list_group')
routers.register('list_requested_user_joined', RequestedUserJoined_Groups, basename='list_group_joined')
routers.register('group_profileimage_change', GroupProfileImgChange_Viewset, basename='Group_profileImg_change')
routers.register('group_edit', GroupEdit_Viewset, basename='edit_group')



urlpatterns = [
    path("", include(routers.urls))
]