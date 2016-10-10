from django.views.generic import TemplateView
from django.views import generic
from django.template.response import TemplateResponse

class HomeView(TemplateView):
    template_name='index.html'
