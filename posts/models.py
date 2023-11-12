from django.db import models

from GroupPosts.models import GroupPost
from users.models import SignupUser




# model for create posts

class Post(models.Model):
    user = models.ForeignKey(SignupUser, on_delete=models.CASCADE, related_name='post_user',null=True,blank=True)
    post_title = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.post_title


class RelatedFile(models.Model):
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='relatedFile_post', null=True, blank=True)
    related_GroupPost = models.ForeignKey(GroupPost, on_delete=models.CASCADE, related_name='relatedFile_grouppost', null=True,
                                     blank=True)
    file = models.FileField(null=True, blank=True)





# model for post comment

class PostComment(models.Model):
    comment_by = models.ForeignKey(SignupUser, on_delete=models.CASCADE,related_name='comment_user',null=True,blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    comment = models.TextField(null=True, blank=True)
    comment_file = models.FileField(null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)




# model for posts rating

class PostsRating(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='rating_post')
    rating_user = models.ForeignKey(SignupUser, on_delete=models.CASCADE, related_name='rating_user')
    rating = models.IntegerField(null=True, blank=True)



# model for post likes

class PostLike(models.Model):
    liked_by = models.ForeignKey(SignupUser, on_delete=models.CASCADE, related_name='postLike_user')
    post_liked = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postLike_post')



