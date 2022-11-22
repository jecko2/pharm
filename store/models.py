from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify

import random
import string

from account.models import Profile

def generate_unit_code():
    L=[]
    for _ in range(4):
        if len(L) < 5:
            random.shuffle(string.digits.split())
            L.append(random.choice(string.digits))
            
    return "".join(L)

class Unit(models.Model):
    name = models.CharField(_("Unit Title"), max_length=100)
    slug = models.SlugField(_("Unique URL Path"), max_length=100, unique=True)
    quote = models.CharField(max_length=200)
    code = models.IntegerField(editable=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    descr = models.TextField()
    body = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("core:content_detail_view", kwargs={
            "slug":self.slug
        })
    
    def save(self, *args, **kwargs):
        
        self.code = generate_unit_code()
        self.slug = slugify(self.name)
        
        return super().save(*args, **kwargs)
    
class UnitTopic(models.Model):
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="topic_writer")
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="unit_topic")
    title = models.CharField(_("Topic Title"), max_length=100)
    slug = models.SlugField(_("Unique for URL"), unique=True, max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)
    content = models.TextField()
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("core:topic_detail_view", kwargs={
            "pk":self.pk,
            "slug":self.slug,
        })
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        
        return super().save(*args, **kwargs)
    
    


class TopicImage(models.Model):
    topic = models.ForeignKey(UnitTopic, on_delete=models.CASCADE, related_name="topic_image")
    img = models.ImageField(upload_to="topics/images/")
    
    def __str__(self):
        
        return self.img.url
    
    
    

class ResearchLabReport(models.Model):
    
    class Type(models.TextChoices):
        RP = "RP", "Report"
        RS = "RS", "Research"
        
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    email = models.EmailField(_("Email Address"), max_length=255)
    reports = models.FileField(upload_to="reports/files/")
    pub_date = models.DateTimeField(auto_now_add=True)
    summary = models.TextField(blank=True)
    type = models.CharField(_("Paper Type"), max_length=3, choices=Type.choices, default=Type.RP)
    
    def __str__(self):
        return self.title
    
    
    
class ExamPaper(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    email = models.EmailField(_("Email Address"), max_length=255)
    reports = models.FileField(upload_to="exams/files/")
    pub_date = models.DateTimeField(auto_now_add=True)
    summary = models.TextField(blank=True)
    
    
    def __str__(self):
        return self.title
    