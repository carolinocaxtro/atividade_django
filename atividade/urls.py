from django.urls import path
from .views import HospedagemCreateView, ListaHospedagensView, DetalheHospedagemView, EditarHospedagemView, RemoverHospedagemView, index

urlpatterns = [
    path('cadastrar_hospedagem/', HospedagemCreateView.as_view(), name='cadastrar_hospedagem'),
    path('lista_hospedagens/', ListaHospedagensView.as_view(), name='lista_hospedagens'),
    path('detalhe_hospedagem/<int:pk>/', DetalheHospedagemView.as_view(), name='detalhe_hospedagem'),
    path('editar_hospedagem/<int:pk>/', EditarHospedagemView.as_view(), name='editar_hospedagem'),
    path('remover_hospedagem/<int:pk>/', RemoverHospedagemView.as_view(), name='remover_hospedagem'),
    path('', index, name='index')
    
]