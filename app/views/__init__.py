from django.core import serializers
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Count
from app.models import BasisKasus

def index(request):
    context = {}
    qs = BasisKasus.objects.all().values('penyakit__nama').annotate(total=Count('penyakit'))
    items = [
        { 'nama': q['penyakit__nama'], 'total': q['total']  }
        for q in qs
    ]
    context['items'] = items
    return render(request, 'app/index.html', context)

