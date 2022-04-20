from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from app.forms import BasisKasusForm
from app.models import BasisKasus

class BasisKasusListView(ListView):
    extra_context = {
      'page_title': 'Data Basis Kasus',
      'page_pretitle': 'Tambah Data Basis Kasus'
    }
    model = BasisKasus
    template_name = 'app/basis-kasus/list.html'

class BasisKasusCreateView(CreateView):
    extra_context = {
      'page_title': 'Data Basis Kasus',
      'page_pretitle': 'Tambah Data Basis Kasus'
    }
    model = BasisKasus
    form_class = BasisKasusForm
    template_name = 'app/commons-create.html'
    def form_valid(self, form):
        return super().form_valid(form)

class BasisKasusUpdateView(UpdateView):
    extra_context = {
        'page_title': 'Ubah Data Basis Kasus',
        'page_pretitle': 'Data Basis Kasus'
    }
    model = BasisKasus
    form_class = BasisKasusForm
    template_name = 'app/basis-kasus/edit.html'

class BasisKasusDeleteView(DeleteView):
    model = BasisKasus
    template_name = 'app/delete-confirmation.html'
    success_url = '/app/basis-kasus'
