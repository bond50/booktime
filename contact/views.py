from django.core.mail import BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.views.generic.edit import FormView


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.sending_mail()
                messages.success(request, 'Email Send Successfully.We will get back to you soon')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'contact/contacts.html', {'form': form})

# class ContactUsView(FormView):
#     template_name = "contact/contacts.html"
#     form_class = ContactForm
#     success_url = "/"
#
#     def form_valid(self, form):
#         form.sending_mail()
#         return super().form_valid(form)
