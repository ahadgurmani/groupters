from django.db import models

from users.models import SignupUser


# notification model


class NotificationModel(models.Model):
    sender = models.ForeignKey(SignupUser, on_delete=models.CASCADE, related_name='notification_user_sender')
    receiver = models.ForeignKey(SignupUser, on_delete=models.CASCADE, related_name='notification_user_receiver')
    title = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    read = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)



