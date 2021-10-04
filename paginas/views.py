from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index2.html'


class SobreView(TemplateView):
    template_name = 'sobre.html'
