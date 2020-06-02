from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def ensure_profile_created(sender, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=kwargs.get('instance'))


"""
django signals useful, when ever an even happend in database that a user is saved
to db then we recive a signal from User, and will ensure that our Profile has to be
attached to that signal
"""
