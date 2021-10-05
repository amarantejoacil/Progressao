from cadastros.views import CampoCreate, CampoUpdate , CampoDelete, CampoList, ProdutoList
from cadastros.views import AtividadeCreate, AtividadeUpdate, AtividaDelete, AtividaList
from django.urls import path
#from .views import 


urlpatterns = [
    path('cadastrar/campo', CampoCreate.as_view(), name='cadastrar-campo'),
    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),
    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name='excluir-campo'),
    path('listar/campo/', CampoList.as_view(), name='listar-campo'),

    path('cadastrar/atividade', AtividadeCreate.as_view(), name='cadastrar-atividade'), 
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name='editar-atividade'),   
    path('excluir/atividade/<int:pk>/', AtividaDelete.as_view(), name='excluir-atividade'),   
    path('listar/atividade/', AtividaList.as_view(), name='listar-atividade'),  
    
    path('listar/produto/', ProdutoList.as_view(), name='listar-produto'), 
]