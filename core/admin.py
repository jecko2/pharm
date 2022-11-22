from django.contrib import admin

# ---------------
# STORE MODELS

from store.models import Unit, TopicImage, UnitTopic, ResearchLabReport, ExamPaper
# ---------------


    
class TopicImageInline(admin.StackedInline):
    model= TopicImage
    extra = 0
    
class ResearchLabReportInline(admin.StackedInline):
    model= ResearchLabReport
    extra = 0
    
class ExamPaperInline(admin.StackedInline):
    model= ExamPaper
    extra = 0
    
@admin.register(UnitTopic)

class UnitTopicAdmin(admin.ModelAdmin):
    list_display = [
    "writer","unit","title","pub_date","updated_date","is_verified",
    ]
    inlines = [TopicImageInline, ]
    
    prepopulated_fields = {"slug": ("title", )}
    
    
    
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'pub_date', 'is_verified']    
    
    prepopulated_fields = {"slug": ("name", )}
    
    inlines = [ResearchLabReportInline, ExamPaperInline]



