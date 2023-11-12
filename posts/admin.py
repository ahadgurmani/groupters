from django.contrib import admin
from .models import RelatedFile, Post, PostComment, PostsRating, PostLike


@admin.register(RelatedFile)
class RelatedFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'related_post', 'related_GroupPost']


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post_title', 'image', 'description', 'time']


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment_by', 'post', 'comment', 'comment_file', 'time']


@admin.register(PostsRating)
class PostsRatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'rating_user', 'rating']


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'liked_by', 'post_liked']
