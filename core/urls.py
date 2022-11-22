from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("academics/", views.content_list_view, name="academic_list"),
    path("academics/<str:slug>/", views.content_detail_view, name="content_detail_view"),
    path("research-lab-reports/reports/", views.list_research_lab_reports, name="list_research_lab_reports"),
    path("examination-past-papers/revision-papers/", views.list_examination_papers, name="list_examination_papers"),
    path("academics/<int:pk>/<str:slug>/", views.topic_detail_view, name="topic_detail_view"),
    
    path("uploads/report-research-paper/", views.research_report_upload_view, name="research_report_upload_view"),
    path("uploads/past-examination-papers/", views.exam_past_paper_upload_view, name="exam_past_paper_upload_view"),
    
    
    # search
    
    path("search/", views.search_list_view, name="search_list_view"),
    
]
