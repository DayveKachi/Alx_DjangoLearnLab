from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile


User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
