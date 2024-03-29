from django.contrib import admin

from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from . import views

handler404 = 'accounts.views.handler404'


from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  # path('', TemplateView.as_view(template_name="index.html"), name='index'),
                  path('', views.HomePageView.as_view(), name='index'),
                  path('accounts/', include("accounts.urls")),
                  path('contact/', include("contact.urls")),
                  path('main/', include("main.urls")),
                  path('address/', include("address.urls")),
                  path('basket/', include("basket.urls")),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
