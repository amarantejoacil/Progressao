from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Campo, Atividade

from django.urls import reverse_lazy

#CAMPO
#CREATE
class CampoCreate(CreateView):
    model = Campo
    fields = '__all__'
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campo')

#UPDATE
class CampoUpdate(UpdateView):
    model = Campo
    fields = '__all__'
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campo')  

#DELETE
class CampoDelete(DeleteView):
    model = Campo   
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campo')  

#LIST
class CampoList(ListView):
    model = Campo   
    template_name = 'cadastros/listas/campo-list.html'


#ATIVIDADE
#CREATE
class AtividadeCreate(CreateView):
    model = Atividade
    fields = '__all__'
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

#UPDATE
class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

#DELETE
class AtividaDelete(DeleteView):
    model = Atividade    
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

#LIST
class AtividaList(ListView):
    model = Atividade    
    template_name = 'cadastros/listas/atividade-list.html'


