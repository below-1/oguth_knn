from django.shortcuts import redirect, render
from app.forms import DiagnosaForm
from app.models import BasisKasus

def diagnosa(request):
    context = {}
    context['page_title'] = 'Hasil Diagnosa'
    context['page_pretitle'] = 'Diagnosa'
    if request.method == 'POST':
      form = DiagnosaForm(request.POST)
      if form.is_valid():
          # print(form.cleaned_data['gejala'])
          new_gs = { g.id for g in form.cleaned_data['gejala'] }
          xs = []
          for bk in BasisKasus.objects.all():
              old_gs = { g.id for g in bk.daftar_gejala.all() }
              same_gs = new_gs.intersection(old_gs)
              diff_gs = old_gs.union(new_gs).difference(same_gs)
              n_same_gs = len(same_gs)
              n_diff_gs = len(diff_gs)
              sm = n_same_gs / (n_same_gs + n_diff_gs)
              xs.append({
                'bk': bk,
                'sm': sm * 100
              })
          xs.sort(reverse=True, key=lambda t: t['sm'])
          solution = xs[0]
          context['daftar_gejala'] = form.cleaned_data['gejala']
          context['solution'] = solution
          return render(request, 'app/diagnosa/hasil.html', context)
      else:
          context['form'] = form
          return render(request, 'app/diagnosa/hasil.html', context)
    else:
      context['form'] = DiagnosaForm()
      return render(request, 'app/diagnosa/form.html', context)
