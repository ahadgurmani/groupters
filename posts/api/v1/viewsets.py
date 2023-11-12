from django.db.models import Count
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from notifications.models import NotificationModel
from .serializers import CreatePostSerializer, PostsListSerializer, PostCommentSerialier, PostsRatingserializer
from posts.models import Post, RelatedFile, PostsRating, PostLike
from rest_framework.filters import OrderingFilter



# viewset for creating post

class PostCreateViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        files = request.data.pop('related_files')
        serializer = CreatePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["time"] = timezone.now()
        serializer.save()
        post_id = serializer.data.get('id')
        for i in files:
            RelatedFile.objects.create(related_post_id=post_id, file=i)
        return Response({'msg': 'post created successfully'})



# viewset for all posts list

class PostsListViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostsListSerializer
    queryset = Post.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['time']

    def get_queryset(self):
        queryset = self.queryset.annotate(total_comments=Count('comment_post', distinct=True), total_likes=Count('postLike_post',distinct=True))
        return queryset


    @action(detail=False, methods=['POST'])
    def comment(self, request):
        serialier = PostCommentSerialier(data=request.data)
        serialier.is_valid(raise_exception=True)
        serialier.validated_data['time'] = timezone.now()
        serialier.save()
        post_user = Post.objects.filter(id=request.data.get("post")).first()
        if post_user:
            post_user = post_user.user
            NotificationModel.objects.create(sender=request.user, receiver=post_user, body=f"{request.user.first_name} {request.user.last_name} comment on your post", title="post comment", )
        return Response({'msg': 'commented successfully'})

    @action(detail=True, methods=['GET'])
    def post_like(self, request, pk=None):
        already = PostLike.objects.filter(liked_by=request.user, post_liked_id= pk)
        if already:
            already.delete()
            return Response({'msg':'post unliked'})
        PostLike.objects.create(liked_by=request.user, post_liked_id=pk)
        post = Post.objects.filter(id=request.data.get('post_liked')).first()
        post_user = post.user
        NotificationModel.objects.create(sender=request.user, receiver=post_user, body=f'{request.user.first_name} {request.user.last_name} liked your post', title=f'post liked')
        return Response({'msg': 'post liked'})



# viewset for the all posts of request user

class RequestedUserPostsViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self,request):
        post_list = Post.objects.filter(user = request.user)
        serializer = PostsListSerializer(post_list,many=True)
        return Response(serializer.data)




# viewset for posts rating

class PostsRatingViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def create(self,request,*args, **kwargs):
        serializer = PostsRatingserializer(data=request.data)
        user = request.data.get('rating_user')
        post = request.data.get('post')
        already = PostsRating.objects.filter(post=post,rating_user=user)
        if already:
            already.update(rating=request.data.get('rating'))
            return Response({'msg': 'Rating Updated'})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        post = Post.objects.filter(id=request.data.get('post')).first()
        post_user = post.user
        NotificationModel.objects.create(sender=request.user, receiver=post_user, body=f'{request.user.first_name} {request.user.last_name} rated your post', title='post got rated')
        return Response({'msg':'Rated Successfully'})
