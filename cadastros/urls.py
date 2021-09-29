from django.urls import path
#from .views import 


urlpatterns = [
    path('endereco', IndexView.as_view(), name='index'),
    
]