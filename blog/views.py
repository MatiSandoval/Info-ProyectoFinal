
from django.views.generic import TemplateView


class IndexViews(TemplateView):
    template_name = 'base.html'