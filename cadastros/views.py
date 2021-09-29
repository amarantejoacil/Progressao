from django.views.generic.edit import CreateView, UpdateView

from .models import Campo, Atividade

from django.urls import reverse_lazy

#CAMPO
class CampoCreate(CreateView):
    model = Campo
    fields = '__all__'
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class CampoUpdate(UpdateView):
    model = Campo
    fields = '__all__'
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')   



#ATIVIDADE
class AtividadeCreate(CreateView):
    model = Atividade
    fields = '__all__'
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

