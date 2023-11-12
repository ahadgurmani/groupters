from django.urls import path,include
from rest_framework.routers import DefaultRouter

from posts.api.v1.viewsets import PostCreateViewset, PostsListViewset, RequestedUserPostsViewset, PostsRatingViewset

routers = DefaultRouter()
routers.register('create_post', PostCreateViewset, basename='post_create')
routers.register('All_posts_list', PostsListViewset,basename='all_posts')
routers.register('requested_user_posts', RequestedUserPostsViewset, basename='requestuser_posts')
routers.register('post_rating', PostsRatingViewset, basename='rating_post')


urlpatterns = [
    path("", include(routers.urls)),
]