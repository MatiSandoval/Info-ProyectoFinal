
from django.views.generic import TemplateView

# def index(request):
#     return render(request, 'index.html')

class IndexViews(TemplateView):
    template_name = 'base.html'