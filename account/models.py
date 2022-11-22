from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class CustomUser(AbstractUser):
    pass


class Profile(models.Model):
    
    class Role(models.TextChoices):
        WR = "WR", "Writer"
        ED = "ED", "Editor"
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="custom_profile")
    profile_pic = models.ImageField(upload_to="account/profiles/", blank=True, null=True)
    role = models.CharField(max_length=2, choices=Role.choices, default=Role.WR)
    is_cleared = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.user.username
    
    @receiver(post_save, sender=CustomUser)
    def profile_post_save_receiver(sender,instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            
        
    