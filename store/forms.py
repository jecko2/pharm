from django import forms
from .models import UnitTopic, Unit, ResearchLabReport, ExamPaper

class UnitTopicForm(forms.ModelForm):
    class Meta:
        model = UnitTopic
        fields = ['title', 'content']
    
    def __int__(self, *args, **kwargs):
        self.fields['unit'] = forms.ModelChoiceField(
            queryset=Unit.objects.all(),
            widget=forms.Select(attrs={"class": "form-control"})
        )
        
        
        
        
class ResearchLabReportUploadForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
       "class":"uk-input uk-form-large uk-border-rounded",
       "placeholder":"Title of the paper....."
    }))
    email = forms.EmailField( required=True,widget=forms.EmailInput(attrs={
        "class": "uk-input uk-form-large uk-border-rounded",
        "placeholder":"example@gmail.com"
    }))
    reports = forms.FileField(
        help_text="Upload both pdf and word document including images",
        widget=forms.FileInput(attrs={"class": "form-control"})
        )
    summary = forms.CharField(help_text="Give a little description. Not required", widget=forms.Textarea(attrs={
        "class":"uk-textarea  uk-border-rounded", "rows":4,
        "placeholder":"Brief descrioption of the paper although this i not needed"
    }))
    type = forms.ChoiceField(widget=forms.Select(attrs={
        "class":""
    }), choices=ResearchLabReport.Type.choices)
    
    class Meta:
        model = ResearchLabReport
        fields = ['title', "email", 'unit', 'type', 'reports', 'summary']
        
    def __int__(self, *args, **kwargs):
        self.fields['unit'] = forms.ModelChoiceField(
            queryset=Unit.objects.all(),
            widget=forms.Select(attrs={"class": "form-control",})
        )
        
class ExamPaperUploadForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
       "class":"uk-input uk-form-large uk-border-rounded",
       "placeholder":"Title of the paper....."
    }))
    email = forms.EmailField( required=True,widget=forms.EmailInput(attrs={
        "class": "uk-input uk-form-large uk-border-rounded",
        "placeholder":"example@gmail.com"
    }))
    reports = forms.FileField(
        help_text="Upload both pdf and word document including images",
        widget=forms.FileInput(attrs={"class": "uk-input uk-form-large uk-border-rounded"}))
    summary = forms.CharField(help_text="Give a little description. Not required", widget=forms.Textarea(attrs={
        "class":"uk-textarea uk-form-large uk-border-rounded", "rows":4,
        "placeholder":"Brief descrioption of the paper although this i not needed"
    }))
    
    class Meta:
        model = ExamPaper
        fields = ['title', "email", "unit", 'reports', 'summary']
        
    def __int__(self, *args, **kwargs):
        self.fields['unit'] = forms.ModelChoiceField(
            queryset=Unit.objects.all(),
            widget=forms.Select(attrs={"class": "form-control"})
        )
        