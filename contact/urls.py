from django.urls import path

from . import views
from django.views.generic import TemplateView


app_name = 'contact'

urlpatterns = [
    path("about-us/", TemplateView.as_view(template_name="contact/about_us.html"), name="about_us", ),
    path("pricing/", TemplateView.as_view(template_name="contact/pricing.html"), name="pricing", ),
    path('email/', views.contact_us, name='contact', ),
]