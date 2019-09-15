from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import UserCreationForm
from django.shortcuts import render_to_response

import logging
from django.contrib import messages
from django.views.generic.edit import FormView

logger = logging.getLogger(__name__)


class SignupView(FormView):
    template_name = "accounts/register.html"
    form_class = UserCreationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = "Sign Up"
        return context

    def get_success_url(self):
        redirect_to = self.request.GET.get("next", "/")
        return redirect_to

    def form_valid(self, form):
        response = super().form_valid(form)
        form.save()
        email = form.cleaned_data.get("email")
        raw_password = form.cleaned_data.get("password1")
        logger.info("New signup for email=%s through SignupView", email)
        user = authenticate(email=email, password=raw_password)
        login(self.request, user)
        form.send_mail()
        messages.info(self.request, "You signed up successfully.")
        return response


def logout_user(request):
    logout(request)
    messages.success(request, 'Thanks for spending some quality time with the Web site today.')
    return redirect('index')


def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response

# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'You Have Successfully Logged In')
#             return redirect('index')
#
#         else:
#             messages.success(request, 'Error Logging In - Try again....')
#             return redirect('accounts:login')
#     else:
#
#         return render(request, 'accounts/login.html', {})


# def register_user(request):
#     if request.method == 'POST':
#         form = SignUpForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'You Have Successfully Registered. Please Login to Proceed')
#             return redirect('accounts:login')
#
#     else:
#         form = SignUpForm()
#
#     return render(request, 'accounts/register.html', {'form': form})


# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         form = UserCreationForm(data=request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'You Have Successfully Updated Your Profile')
#             return redirect('index')
#     else:
#         form = UserChangeForm(instance=request.user)
#
#     return render(request, 'accounts/edit_profile.html', {'form': form})


# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(data=request.POST, user=request.user)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             messages.success(request, 'You Have Successfully Updated Your Password')
#             return redirect('index')
#     else:
#         form = PasswordChangeForm(user=request.user)
#
#     return render(request, 'accounts/change_password.html', {'form': form})
