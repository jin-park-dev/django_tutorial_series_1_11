from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

# Create your models here.


User = settings.AUTH_USER_MODEL

class ProfileManager(models.Manager):
    def toggle_follow(self, requested_user, username_to_toggle):
        profile_ = Profile.objects.get(user__username__iexact=username_to_toggle)
        user = requested_user
        is_following = False
        if user in profile_.followers.all():
            profile_.followers.remove(user)
        else:
            profile_.followers.add(user)
            is_following = True
        return profile_, is_following



class Profile(models.Model):
    user        = models.OneToOneField(User) # user.profile
    followers   = models.ManyToManyField(User, related_name='is_following', blank=True) # user.profile_set.all()
    # following   = models.ManyToManyField(User, related_name='following', blank=True)
    activated   = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    objects = ProfileManager()

    def __str__(self):
        return self.user.username

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance) #can do this as safe guard
        default_user_profile = Profile.objects.get_or_create(user__id=1)[0] #user__username= #Cna use object.get(user__id=1)
        default_user_profile.followers.add(instance)
        # default_user_profile.followers.remove(instance) #can remove
        # profile.followers.add(default_user_profile.user) # can also add other way
        profile.followers.add(3) #another default adding

post_save.connect(post_save_user_receiver, sender=User)