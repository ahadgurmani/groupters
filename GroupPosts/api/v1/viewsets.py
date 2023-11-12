from django.db.models import Prefetch, Count
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from groups.api.v1.serializers import AllGroupList_Serializer
from groups.models import CreateGroup
from notifications.models import NotificationModel
from posts.models import RelatedFile
from .serializers import GroupPostSerializer, CommentSerialierForGroupPost
from GroupPosts.models import GroupPost, GroupPostLike


# viewset for creating group post
# on the basis of admin and normal user or members
class GroupPostViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def create(self,request):
        more_images = request.data.pop('more_img')
        serializer = GroupPostSerializer(data=request.data)
        post_by_id = request.data.get('post_by')
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['time'] = timezone.now()
        group = serializer.validated_data['group']
        if int(post_by_id) == group.admin.id:
            serializer.save(post_status='Approve')
            return Response({'msg':'posted successfully'})
        serializer.save()
        post_id = serializer.data.get('id')
        for img in more_images:
            RelatedFile.objects.create(related_GroupPost_id=post_id, file=img)
        return Response({'msg': 'post has been submitted'})

    @action(detail=True, methods=['GET'])
    def post_approve(self, request, pk=None):
        post = GroupPost.objects.filter(id=pk).first()
        if post:
            user = request.user
            group = post.group
            if user == group.admin:
                post.post_status = 'Approve'
                return Response({'msg': 'post approved'})
            return Response({'error': 'only group admin can approve'})
        return Response({'error': 'post does not exists'})


    @action(detail=True, methods=['GET'])
    def post_decline(self, request, pk=None):
        post = GroupPost.objects.filter(id=pk).first()
        if post:
            user = request.user
            group = post.group
            if user == group.admin:
                post.post_status = 'Decline'
                return Response({'msg': 'post Declined'})
            return Response({'msg':'only admin have this command'})

        else:
         return Response({'error': 'post does not exist'})



# viewset for all group posts lists

class AllGroupsPostsList_Viewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GroupPostSerializer
    queryset = GroupPost.objects.all().filter(post_status='Approve')

    def get_queryset(self):
        queryset = self.queryset.annotate(total_likes=Count('postLike_groupPost', distinct=True), total_comments=Count('postComment_post',distinct=True))
        return queryset

# action for group post likes
    @action(detail=False, methods=['GET'])
    def groupPost_like(self, request):
        group_id = self.request.query_params.get('group_id')
        post_id = self.request.query_params.get('post_id')
        user = request.user
        already = GroupPostLike.objects.filter(liked_by=user, likedPost_group_id=group_id, post_liked_id=post_id).first()
        if already:
            already.delete()
            return Response({'status': False})
        GroupPostLike.objects.create(liked_by=user, likedPost_group_id=group_id, post_liked_id=post_id)
        post_id =self.request.query_params.get('post_id')
        post = GroupPost.objects.filter(id=post_id).first()
        if post:
            post_user = post.post_by
            NotificationModel.objects.create(sender=request.user, receiver=post_user, body=f'{request.user.first_name} {request.user.last_name} liked your post', title='post liked')
        return Response({'status': True})

# action for group post comment
    @action(detail=False, methods=['POST'])
    def comment_groupPost(self, request):
        serializer = CommentSerialierForGroupPost(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(comment_by=request.user)
        post_id = request.data.get('commented_post')
        post = GroupPost.objects.filter(id=post_id).first()
        if post:
            post_user = post.post_by
            NotificationModel.objects.create(sender=request.user, receiver=post_user, body=f'{request.user.first_name} {request.user.last_name} comment on your post', title='post commented')
        return Response({'msg': 'commented successfuly'})





# specific group and its posts list


class SpecificGroupPostsList_Viewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self,requst):
        group = self.request.query_params.get('group')
        posts = GroupPost.objects.filter(group=group, post_status="Approve")
        serializer = GroupPostSerializer(posts, many=True)
        return Response(serializer.data)

# for getting the posts in a group of request request user and other user
    @action(detail=False, methods=['GET'])
    def SpecificUserPosts(self, request):
        user_id = self.request.query_params.get('user')
        user = request.user
        if int(user_id) == user.id:
            posts = GroupPost.objects.filter(post_by=user_id)
            serialier = GroupPostSerializer(posts, many=True)
            return Response(serialier.data)
        else:
            posts = GroupPost.objects.filter(post_by=user_id, post_status="Approve")
            serialier = GroupPostSerializer(posts, many=True)
            return Response(serialier.data)








