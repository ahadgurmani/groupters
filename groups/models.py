from django.db import models





# model for create group
from users.models import SignupUser


class GroupCategory(models.Model):
    category = models.CharField(max_length=500, null=True, blank=True)


    def __str__(self):
        return self.category


group_choices = (
    ('Public', 'Public'),
    ('School', 'School')
)



class CreateGroup(models.Model):
    admin = models.ForeignKey(SignupUser, on_delete=models.CASCADE,related_name='group_user')
    members = models.ManyToManyField(SignupUser, related_name='members_user')
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=300, null=True, blank=True)
    group_Type = models.CharField(max_length=20, choices=group_choices, null=True, blank=True)
    group_category = models.ForeignKey(GroupCategory, on_delete=models.CASCADE,related_name='Group_category')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title




