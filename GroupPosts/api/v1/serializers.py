from rest_framework import serializers

from GroupPosts.models import GroupPost, GroupPostLike, GroupPostComment
from users.api.v1.serializers import UserLoginSerializer


class GroupPostLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupPostLike
        fields = ['id', 'liked_by', 'likedPost_group', 'post_liked']



class CommentSerialierForGroupPost(serializers.ModelSerializer):
    comment_by = UserLoginSerializer(many=False,read_only=True)
    class Meta:
        model = GroupPostComment
        fields = ['id', 'comment_by', 'commented_post', 'post_group', 'comment', 'comment_file', 'time']



class GroupPostSerializer(serializers.ModelSerializer):
    likes = GroupPostLikesSerializer(source='postLike_groupPost', many=True, read_only=True)
    total_likes = serializers.IntegerField(read_only=True)
    comments = CommentSerialierForGroupPost(source='postComment_post', many=True, read_only=True)
    total_comments = serializers.IntegerField(read_only=True)
    class Meta:
        model = GroupPost
        fields = ['id', 'group', 'post_by', 'post_title', 'image', 'description', 'time', 'post_status', 'likes', 'total_likes', 'comments', 'total_comments']

