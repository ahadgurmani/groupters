from rest_framework import serializers
from fcm_django.models import FCMDevice

from posts.models import Post, RelatedFile, PostComment, PostsRating, PostLike
from users.api.v1.serializers import UserLoginSerializer


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'post_title', 'image', 'description', 'time']


# serialier for comment on posts

class PostCommentSerialier(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = ['id', 'comment_by', 'post', 'comment', 'comment_file', 'time']







# serialier for all posts list

class RelatedFilesSerializerForPosts(serializers.ModelSerializer):
    class Meta:
        model = RelatedFile
        fields = ['id', 'file', 'related_post']


class CommentSerialierForPost(serializers.ModelSerializer):
    comment_by = UserLoginSerializer(many=False,read_only=True)
    class Meta:
        model = PostComment
        fields = ['id', 'comment_by', 'post', 'comment', 'comment_file', 'time']


# serializer for rating posts

class PostsRatingserializer(serializers.ModelSerializer):
    class Meta:
        model = PostsRating
        fields = ['id', 'post', 'rating_user', 'rating']



class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['id', 'liked_by', 'post_liked']

class PostsListSerializer(serializers.ModelSerializer):
    related_files = RelatedFilesSerializerForPosts(source='relatedFile_post', many=True, read_only=True)
    user = UserLoginSerializer(many=False,read_only=True)
    comments = CommentSerialierForPost(source='comment_post', many=True, read_only=True)
    total_comments = serializers.IntegerField(read_only=True)
    ratings = serializers.SerializerMethodField(method_name="get_ratings", read_only=True)
    likes = PostLikeSerializer(source='postLike_post', many=True, read_only=True)
    total_likes = serializers.IntegerField(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'user', 'post_title', 'image', 'description', 'time', 'related_files', 'comments', 'total_comments', 'likes', 'total_likes', 'ratings']
        depth = 1

    def get_ratings(self, obj):
        try:
            return obj.rating_post.first().rating
        except:
            return 0


