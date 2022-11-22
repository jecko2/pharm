from django.contrib import admin
from .models import Subscription, Contact
# Register your models here.

@admin.register(Subscription)
class SubscriptionAmin(admin.ModelAdmin):
    list_display = ['email', ]
    
@admin.register(Contact)
class SubscriptionAmin(admin.ModelAdmin):
    list_display = ['name', "email", "pub_date", "replied"]
    
    
