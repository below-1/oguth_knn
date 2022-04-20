from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from app.forms import GejalaForm
from app.models import Gejala

class GejalaListView(ListView):
    extra_context = {
      'page_title': 'Data Gejala',
      'page_pretitle': 'Tambah Data Gejala'
    }
    model = Gejala
    template_name = 'app/gejala/list.html'

class GejalaCreateView(CreateView):
    extra_context = {
      'page_title': 'Data Gejala',
      'page_pretitle': 'Tambah Data Gejala'
    }
    model = Gejala
    form_class = GejalaForm
    template_name = 'app/commons-create.html'
    def form_valid(self, form):
        return super().form_valid(form)

class GejalaUpdateView(UpdateView):
    extra_context = {
        'page_title': 'Ubah Data Gejala',
        'page_pretitle': 'Data Gejala'
    }
    model = Gejala
    form_class = GejalaForm
    template_name = 'app/gejala/edit.html'

class GejalaDeleteView(DeleteView):
    model = Gejala
    template_name = 'app/delete-confirmation.html'
    success_url = '/app/gejala'
