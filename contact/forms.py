from django import forms
from .models import Contact, Subscription
from django.core.mail import send_mail


class ContactForm(forms.ModelForm):
    name = forms.CharField(label="Full Name", required=True, widget=forms.TextInput(
        attrs={"class":"uk-input uk-form-large uk-border-rounded", 
               "placeholder":"Jeckonia Onyango"}
        ))
    email = forms.EmailField( required=True,widget=forms.EmailInput(attrs={
        "class": "uk-input uk-form-large uk-border-rounded",
        "placeholder":"example@gmail.com"
    }))
    message = forms.CharField( required=True, widget=forms.Textarea(
        attrs={"class":"uk-textarea uk-form-large uk-border-rounded", "rows":4,
               "placeholder":"Your message goes here ... "}
        ))
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        
    
    def cleaned_name(self):
        
        return self.cleaned_data.get("name")
    
    def cleaned_email(self):
        return self.cleaned_data.get("email")
    
    def cleaned_message(self):
        return self.cleaned_data.get("message")
    
    def _send_email(self, message, from_email, recipient):
        
        send_mail("NEW CONTACT MESSAGE", message=message, from_email=from_email, recipient_list=[recipient])


class SubscriptionForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "uk-search-input uk-box-shadow-large subscribe",
        "placeholder":"example@gmail.com"
        }))
    class Meta:
        model = Subscription
        fields = ['email']