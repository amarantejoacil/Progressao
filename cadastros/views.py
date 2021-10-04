from django import urls
from django.http import request
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Campo, Atividade

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import GroupRequiredMixin

#usar o edita e excluir
from django.shortcuts import get_object_or_404


#CAMPO
#CREATE
class CampoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"grupo2"]
    model = Campo
    fields = ['nome', 'descricao', 'contador']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campo')


    #passando context personalizado
    #enviado dados para form.html
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro de Campos'
        context['botao'] = 'Cadastrar'
        #enviando um html para view... 
        #anotação no formhtml autoscape força intepretar o html
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        return context


        

    def form_valid(self, form):
        #obs1. antes do super o objeto com dados não foi criado
        

        #pegando a instancia do meu usuario do models na hora do formulario
        form.instance.usuario = self.request.user


        #super = força a chamar o form_valid do createview
        url = super().form_valid(form)
        #obs2. depois do super o objeto com os dados foi criado

        self.object.contador += 1
        self.object.save()



        return url


#UPDATE
class CampoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"grupo2"]
    model = Campo
    fields = ['nome', 'descricao', 'contador']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campo')

    #passando context personalizado
    #enviado dados para form.html
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Alterar de Campos'
        context['botao'] = 'Salvar'
        return context


    def form_valid(self, form):
        #obs1. antes do super o objeto com dados não foi criado
    

        #pegando a instancia do meu usuario do models na hora do formulario
        form.instance.usuario = self.request.user


         #super = força a chamar o form_valid do createview
        url = super().form_valid(form)
        #obs2. depois do super o objeto com os dados foi criado

        self.object.contador += 1
        self.object.save()



        return url

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
    paginate_by = 3
    


#ATIVIDADE
#CREATE
class AtividadeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo', 'arquivo']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('listar-atividade')


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro de Atividade'
        context['botao'] = 'Cadastrar'
        #enviando um html para view... 
        #anotação no formhtml autoscape força intepretar o html
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        return context

    def form_valid(self, form):
        #obs1. antes do super o objeto com dados não foi criado
    

        #pegando a instancia do meu usuario do models na hora do formulario
        form.instance.usuario = self.request.user


         #super = força a chamar o form_valid do createview
        url = super().form_valid(form)
        #obs2. depois do super o objeto com os dados foi criado

        return url

#UPDATE
class AtividadeUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo', 'arquivo']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('listar-atividade')


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Alterar de Atividade'
        context['botao'] = 'Salvar'
        #enviando um html para view... 
        #anotação no formhtml autoscape força intepretar o html
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        return context


    def get_object(self, queryset=None):
        #kwargs pega o valor referenciado digitado o codigo da url
        # usuario n consegue acessar pela url, dados de outros...
        # exemplo alterar dados por parametro url
        
        #não deixa acessar
        #self.object = Atividade.objects.get(pk=self.kwargs['pk'], usuario=self.request.user) 


        #nao deixa acessar e redireciona para 404... futuramente podendo tratar
        self.object = get_object_or_404(Atividade,pk=self.kwargs['pk'], usuario=self.request.user)      
        return self.object

#DELETE
class AtividaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Atividade    
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-atividade')

#LIST
class AtividaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Atividade    
    template_name = 'cadastros/listas/atividade-list.html'


    def get_queryset(self):
        #self.object_lista = Atividade.objects.all()
        self.object_lista = Atividade.objects.filter(usuario=self.request.user)
        return self.object_lista


