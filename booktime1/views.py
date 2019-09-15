
from django.views.generic import ListView
from accounts.models import ImageUpload


class HomePageView(ListView):
    model = ImageUpload
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = "Home "
        return context
