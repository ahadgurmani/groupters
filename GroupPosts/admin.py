from django.contrib import admin
from .models import GroupPost, GroupPostLike, GroupPostComment


@admin.register(GroupPost)
class GroupPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'group', 'post_by', 'post_title', 'image', 'description', 'time','post_status']


@admin.register(GroupPostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'liked_by', 'likedPost_group', 'post_liked']


@admin.register(GroupPostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment_by', 'commented_post', 'post_group', 'comment', 'comment_file', 'time']
