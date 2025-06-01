from django.db.models.signals import post_save  #post_save saves after the model here User is saved there are other functions as well which can save pre_save etc,..
from django.contrib.auth.models import User 
from django.dispatch import receiver # helps in connecting functions to signals
from .models import Profile

@receiver(post_save, sender=User)   # this decorator is used to recognize when the User is saved(specifically post saved)
def build_profile(sender, instance, created, **kwargs): # these other parameters can be used in various logics i understand this is part of standard framework in signals
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)  ## whenever we make any changes in the future this will run and update the changes, that is why we have created logic in the build profile function
def save_profile(sender, instance, **kwargs):
    instance.profile.save() # at anypoint in time if a change happens to User it will reflect in the profile model

    """
    There are 2 things happening here
    1) (build_profile) is used to automatically create a profile when a new user signs up
    2) (save_profile) is used to save the profile whenever the user is updated or saved(saving can happen many times, so both are needed to make sure every user has a profile and it stays updated)
    """