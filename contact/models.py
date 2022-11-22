from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Subscription(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    def __str__(self):
        return self.email
    
    
class Contact(models.Model):
    name = models.CharField(_("Full Name"), max_length=100)
    email = models.EmailField(_("Email Address"), max_length=255)
    message = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    replied = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    