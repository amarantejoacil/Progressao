from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Campo, Atividade

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import GroupRequiredMixin


#CAMPO
#CREATE
class CampoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"grupo2"]
    model = Campo
    fields = '__all__'
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campo')

#UPDATE
class CampoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"grupo2"]
    model = Campo
    fields = '__all__'
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campo')  

#DELETE
class CampoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"grupo2"]
    model = Campo   
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campo')  

#LIST
class CampoList(LoginRequiredMixin, ListView):
    #verificar se o usuario esta logado
    login_url = reverse_lazy('login')
    model = Campo   
    template_name = 'cadastros/listas/campo-list.html'
    


#ATIVIDADE
#CREATE
class AtividadeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = '__all__'
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

#UPDATE
class AtividadeUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

#DELETE
class AtividaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Atividade    
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

#LIST
class AtividaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Atividade    
    template_name = 'cadastros/listas/atividade-list.html'


