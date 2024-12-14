from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_notifications")
    actor = models.ForeignKey (User, on_delete=models.CASCADE, related_name="sent_notifications")
    verb = models.CharField()
    target = models.GenericForeignKey to the object
    timestamp = models.DateTimeField(auto_now_add=True)

