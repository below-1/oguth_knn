from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from app.forms import PenyakitForm
from app.models import Penyakit

class PenyakitListView(ListView):
    extra_context = {
      'page_title': 'Data Penyakit',
      'page_pretitle': 'Tambah Data Penyakit'
    }
    model = Penyakit
    template_name = 'app/penyakit/list.html'

class PenyakitCreateView(CreateView):
    extra_context = {
      'page_title': 'Data Penyakit',
      'page_pretitle': 'Tambah Data Penyakit'
    }
    model = Penyakit
    form_class = PenyakitForm
    template_name = 'app/commons-create.html'
    def form_valid(self, form):
        return super().form_valid(form)

class PenyakitUpdateView(UpdateView):
    extra_context = {
        'page_title': 'Ubah Data Penyakit',
        'page_pretitle': 'Data Penyakit'
    }
    model = Penyakit
    form_class = PenyakitForm
    template_name = 'app/penyakit/edit.html'

class PenyakitDeleteView(DeleteView):
    model = Penyakit
    template_name = 'app/delete-confirmation.html'
    success_url = '/app/penyakit'
