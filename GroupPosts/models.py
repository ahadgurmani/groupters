from django.db import models
from groups.models import CreateGroup
from users.models import SignupUser


# model for group posts

status_choices = (
    ('Pending', 'Pending'),
    ('Approve', 'Approve'),
    ('Decline', 'Decline'),
)


class GroupPost(models.Model):
    group = models.ForeignKey(CreateGroup, on_delete=models.CASCADE, related_name='groupPost_group')
    post_by = models.ForeignKey(SignupUser, on_delete=models.CASCADE, related_name='groupPost_user')
    post_title = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    post_status= models.CharField(max_length=30, choices=status_choices, default='Pending')

    def __str__(self):
        return self.post_title



# model for post likes

class GroupPostLike(models.Model):
    liked_by = models.ForeignKey(SignupUser, on_delete=models.CASCADE, related_name='group_postLike_user')
    likedPost_group = models.ForeignKey(CreateGroup, on_delete=models.CASCADE, related_name='postLiked_group')
    post_liked = models.ForeignKey(GroupPost, on_delete=models.CASCADE, related_name='postLike_groupPost')


# model for comment on  group post

class GroupPostComment(models.Model):
    comment_by = models.ForeignKey(SignupUser, on_delete=models.CASCADE, related_name='postComment_user')
    commented_post = models.ForeignKey(GroupPost, on_delete=models.CASCADE, related_name='postComment_post')
    post_group = models.ForeignKey(CreateGroup, on_delete=models.CASCADE, related_name='postComment_group')
    comment = models.TextField(null=True, blank=True)
    comment_file = models.FileField(null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

