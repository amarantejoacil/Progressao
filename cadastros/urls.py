from cadastros.views import CampoCreate, CampoUpdate , AtividadeCreate, AtividadeUpdate
from django.urls import path
#from .views import 


urlpatterns = [
    path('cadastrar/campo', CampoCreate.as_view(), name='cadastrar-campo'),
    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),

    path('cadastrar/atividade', AtividadeCreate.as_view(), name='cadastrar-atividade'), 
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name='editar-atividade'),   
]