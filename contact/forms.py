from django import forms
from django.core.mail import send_mail
from django.conf import settings

import logging

logger = logging.getLogger(__name__)


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(max_length=600, widget=forms.Textarea, required=True)
    name = forms.CharField(label='Your name', max_length=100)

    def sending_mail(self):
        email_from = settings.EMAIL_HOST_USER
        logger.info("Sending email to customer service")
        data = "From: {0}\n{1}\n{2}\n{3}".format(self.cleaned_data["name"], self.cleaned_data["from_email"],
                                                 self.cleaned_data["subject"], self.cleaned_data["message"])
        send_mail(
            "Site message: BookTime",
            data,
            email_from,
            ["galavu10@gmail.com"],
            fail_silently=False,
        )

