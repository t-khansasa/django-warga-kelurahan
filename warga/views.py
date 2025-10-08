from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Warga, Pengaduan

class WargaListView(ListView):
    model = Warga


class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'  
    context_object_name = 'object_list' 

# Create your views here.
