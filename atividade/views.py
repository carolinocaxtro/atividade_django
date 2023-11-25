
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Hospedagem
from .forms import HospedagemForm
from django.urls import reverse_lazy
from django.shortcuts import redirect

class HospedagemCreateView(CreateView):
    model = Hospedagem
    form_class = HospedagemForm
    template_name = 'cadastro_hospedagem.html'
    success_url = reverse_lazy('lista_hospedagens')

class ListaHospedagensView(ListView):
    model = Hospedagem
    template_name = 'lista_hospedagens.html'
    context_object_name = 'hospedagens'

class DetalheHospedagemView(DetailView):
    model = Hospedagem
    template_name = 'detalhe_hospedagem.html'
    context_object_name = 'hospedagem'

class EditarHospedagemView(UpdateView):
    model = Hospedagem
    form_class = HospedagemForm
#    fields = ['cliente', 'quarto', 'data_entrada', 'data_saida', 'valor']
    template_name = 'cadastro_hospedagem.html'
    success_url = reverse_lazy('lista_hospedagens') 

class RemoverHospedagemView(DeleteView):
    model = Hospedagem
    template_name = 'remove_hospedagem.html'
    success_url = reverse_lazy('lista_hospedagens')

def index(request):
    
    return redirect('lista_hospedagens')


    
