from cadastros.views import CampoCreate, AtividadeCreate
from django.urls import path
#from .views import 


urlpatterns = [
    path('cadastrar/campo', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/atividade', AtividadeCreate.as_view(), name='cadastrar-atividade'),    
]