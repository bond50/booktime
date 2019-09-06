from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm, \
    UserChangeForm as DjangoUserChangeForm, PasswordChangeForm
from django.contrib.auth.forms import UsernameField
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.contrib import messages

from django import forms

from django.conf import settings
from . import models

import logging

logger = logging.getLogger(__name__)


class UserCreationForm(DjangoUserCreationForm):
    class Meta(DjangoUserCreationForm.Meta):
        model = models.User
        fields = ("email",)
        field_classes = {"email": UsernameField}

    def send_mail(self):
        logger.info("Sending signup email for email=%s", self.cleaned_data["email"], )
        message = "Welcome{} ".format(self.cleaned_data["email"])
        send_mail("Welcome to BookTime"
                  , message,
                  settings.EMAIL_HOST_USER,
                  [self.cleaned_data["email"]],
                  fail_silently=True, )


class AuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(strip=False, widget=forms.PasswordInput)

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        if email is not None and password:
            self.user = authenticate(self.request, email=email, password=password)

            if self.user is None:
                raise forms.ValidationError("Invalid email/password combination.")

            logger.info("Authentication successful for email=%s", email)

            messages.success(self.request, "Login successfully.")
        return self.cleaned_data

    def get_user(self):
        return self.user

#
# class UserChangeForm(DjangoUserChangeForm):
#     email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     first_name = forms.CharField(max_length=55, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     last_name = forms.CharField(max_length=55, widget=forms.TextInput(attrs={'class': 'form-control', }))
#
#     class Meta:
#         model = User
#         fields = ("username", "first_name", "last_name", "email")
#
#     def __init__(self, *args, **kwargs):
#         super(UserChangeForm, self).__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs['class'] = 'form-control'
#         self.fields['username'].help_text = ''
