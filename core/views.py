from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.views.generic import View
from django.http import HttpResponse
from account.models import Profile
from store.models import Unit, UnitTopic, TopicImage, ResearchLabReport, ExamPaper
from account.models import Profile
from contact.forms import SubscriptionForm
from django.contrib import messages
from contact.models import Subscription
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from store.forms import UnitTopicForm, ResearchLabReportUploadForm, ExamPaperUploadForm
from django.db.models import Q

class HomePageVew(View):
    template_name = "index.html"
    subscription_form = SubscriptionForm
    
    def get(self, *args, **kwargs):
        users = get_list_or_404(Profile, is_cleared=True)
        context = {
            "users":users,
            "subscribeForm":self.subscription_form()
            }
        
    
        return render(self.request, self.template_name, context)
    
    def post(self, *args, **kwargs):
        current_site = get_current_site(self.request).site_name
        if "subscription" in self.request.POST:
            form = self.subscription_form(self.request.POST)
            if form.is_valid():
                is_subscribed = Subscription.objects.filter(email=form.cleaned_data.get("email"))
                if is_subscribed:
                    messages.error(self.request, "You're already subscribed to our emailing list!")
                form.save()
                messages.success(self.request, "You subscription was added successfully")
                send_mail("SUBSCRIPTION SUCCESSFUL", f"Your subscription to {current_site} wass successful", settings.DEFAULT_CONTACT_EMAIL, [email, ])
                return redirect("core:home_view")
            messages.error(self.request, "You subscription could not be added. Unknown Error occured")
            return redirect("core:home_view")
                
    

home_view = HomePageVew.as_view()

class ContentListView(View):
    
    template_name = "content_list.html"
    
    def get(self, request, *args, **kwargs):
        context = {
            "academics": Unit.objects.filter(is_verified=True).all()
            }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')
    
    
content_list_view = ContentListView.as_view()


class ContentDetailView(View):
    template_name = "unit.html"
    
    def get(self,request, *args, **kwargs):
        unit = Unit.objects.get(slug=kwargs.pop("slug"))
        unittopics = get_list_or_404(UnitTopic, unit=unit)
        context = {"unit": unit, 'unittopics':unittopics}
        print(request.resolver_match.view_name)
        return render(request, self.template_name, context)
    
content_detail_view = ContentDetailView.as_view()


class TopicDetailView(View):
    
    template_name = "unit.html"
    
    def get(self,request, *args, **kwargs):
        unittopic = get_object_or_404(UnitTopic,pk=kwargs.pop("pk"), slug=kwargs.pop("slug", None))
        unittopics = get_list_or_404(UnitTopic, unit=unittopic.unit)
        context = {'unittopic':unittopic,  'unittopics':unittopics}
        return render(request, self.template_name, context)
    
topic_detail_view = TopicDetailView.as_view()
    
    
    
class ListResearchReportPapersView(View):
    template_name = "reports.html"
    
    def get(self, *args, **kwargs):
        
        # unit = get_object_or_404(Unit, slug=kwargs.pop("slug"))
        reports = ResearchLabReport.objects.all()
        
        # build the context
        
        context = {"reports":reports}
        
        return render(self.request, self.template_name, context)
    
    
    
list_research_lab_reports = ListResearchReportPapersView.as_view()



class ListExaminationPapersView(View):
    template_name = "reports.html"
    
    def get(self, *args, **kwargs):
        
        # unit = get_object_or_404(Unit, slug=kwargs.pop("slug"))
        papers = ExamPaper.objects.all()
        
        # build the context
        
        context = {"papers":papers}
        
        return render(self.request, self.template_name, context)

    
list_examination_papers = ListExaminationPapersView.as_view()
    

# creation 

class TopicCreateView(View):
    template_name = UnitTopic
    form_class = UnitTopicForm
    
    def get(self, *args, **kwargs):
        return render(self.request, self.template)
    
    def post(self, *args, **kwargs):
        return render(self.request)


class ResearchReportUploadView(View):
    template_name = "sub/upload/report.html"
    form_class = ResearchLabReportUploadForm
    
    def get(self, *args, **kwargs):
        context = {"form":self.form_class()}
        return render(self.request, self.template_name, context)
    
    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST, self.request.FILES)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            title = form.cleaned_data.get("title")
            send_mail("SUBMISSION SUCCESSFUL", f"""Your paper  title [{title}] was successfully submitted""", 
                      settings.DEFAULT_CONTACT_EMAIL, [email, ])
            form.save()
            return redirect("core:research_report_upload_view")
        return redirect("core:research_report_upload_view")
    
research_report_upload_view = ResearchReportUploadView.as_view()

    
class ExamPastPaperUploadView(View):
    template_name = "sub/upload/exam.html"
    form_class = ExamPaperUploadForm
    
    def get(self, *args, **kwargs):
        
        context = {"form":self.form_class()}
        return render(self.request, self.template_name,context )
    
    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST, self.request.FILES)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            title = form.cleaned_data.get("title")
            send_mail("SUBMISSION SUCCESSFUL", f"""Your paper title [{title}] was successfully submitted""", 
                      settings.DEFAULT_CONTACT_EMAIL, [email, ])
            form.save()
            return redirect("core:exam_past_paper_upload_view")
        return redirect("core:exam_past_paper_upload_view")
    
exam_past_paper_upload_view  = ExamPastPaperUploadView.as_view()


class ResearchResultView(View):
    template_name = "sub/search_results.html"
    def get(self, *args, **kwargs):
        q = self.request.GET.get("q")
        context = {}
        unit_results =  Unit.objects.filter(Q(name__icontains=q)|Q(descr__icontains=q )|Q(body__icontains=q)).all()
        topic_results = UnitTopic.objects.filter(Q(title__icontains=q)|Q(content__icontains=q )).all()
        reports = ResearchLabReport.objects.filter(title__icontains=q)
        exams = ExamPaper.objects.filter(title__icontains=q)
        if unit_results or exams:
            context.update({
                "unit_results":unit_results,
            })
            
        if topic_results:
            context.update({
                "topic_results":topic_results,
            })
            
        if reports:
            context.update({
                "reports":reports,
            })
            
        if exams:
            context.update({
                "exams":exams,
            })
        return render(self.request, self.template_name, context)
    
    


search_list_view = ResearchResultView.as_view()
            
            
       
        
        
def get_page_404(request, exception):
    return render(request, "404.html")