from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import ContactForm
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.


class ContactView(View):
    template_name = "sub/contact.html"
    form_class = ContactForm
    
    def get(self, *args, **kwargs):
        context = {"form":self.form_class()}
        return render(self.request, self.template_name, context)
    
    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            message = form.cleaned_data.get("message")
            
            data = f"FROM: {email}. MESSAGE: {message}"
            
            form._send_email(message=data, from_email=settings.DEFAULT_CONTACT_EMAIL, recipient=settings.DEFAULT_RECIPIENT_EMAIL)
            form.save()
            send_mail("MESSAGED DELIVERED", f"Hello {name}, This is to confirm that your message was received successfully. Thanks and Will be in Touch", settings.DEFAULT_CONTACT_EMAIL, [email, ])
            return redirect("core:home_view")
    

contact_view_form = ContactView.as_view()
    