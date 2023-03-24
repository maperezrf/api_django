from django.views.generic import TemplateView
# Create your views here.

class ClienteView(TemplateView):
    template_name = "index.html"
