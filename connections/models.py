from django.db import models

from users.models import SignupUser

status_choices = (
    ('Pending', 'Pending'),
    ('Decline', 'Decline'),
    ('Accept', 'Accept')
)


class ConnectionRequests(models.Model):
    connection_to = models.ForeignKey(SignupUser, on_delete=models.CASCADE, related_name='connectionTo_user')
    connection_by = models.ForeignKey(SignupUser, on_delete=models.CASCADE, related_name='connectionBy_user')
    connection_status = models.CharField(max_length=20, choices=status_choices, null=True, blank=True, default='Pending')
