from django.db.models.signals import post_save, m2m_changed
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Tag
from taggit.models import Tag as TaggitTag
from taggit.models import TaggedItem


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(m2m_changed, sender=TaggedItem)
def sync_taggit_tags(sender, instance, action, reverse, **kwargs):
    if action == "post_add" and not reverse:
        for taggit_tag in instance.tags.all():
            # Sync Taggit tags with your custom Tag model
            tag, created = Tag.objects.get_or_create(name=taggit_tag.name)
            tag.posts.add(instance)
