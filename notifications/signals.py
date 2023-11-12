from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.models import NotificationModel


@receiver(post_save,sender= NotificationModel)
def send_notification(sender, instance, *kwargs):
