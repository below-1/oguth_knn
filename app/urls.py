from django.urls import path

from app.views import index, gejala, penyakit, basiskasus, diagnosa

urlpatterns = [
    path('', index, name='app'),
    path('gejala', gejala.GejalaListView.as_view(), name='list_gejala'),
    path('gejala/create', gejala.GejalaCreateView.as_view(), name='create_gejala'),
    path('gejala/<pk>/update', gejala.GejalaUpdateView.as_view(), name='update_gejala'),
    path('gejala/<pk>/delete', gejala.GejalaDeleteView.as_view(), name='delete_gejala'),
    path('penyakit', penyakit.PenyakitListView.as_view(), name='list_penyakit'),
    path('penyakit/create', penyakit.PenyakitCreateView.as_view(), name='create_penyakit'),
    path('penyakit/<pk>/update', penyakit.PenyakitUpdateView.as_view(), name='update_penyakit'),
    path('penyakit/<pk>/delete', penyakit.PenyakitDeleteView.as_view(), name='delete_penyakit'),

    path('basis-kasus', basiskasus.BasisKasusListView.as_view(), name='list_basis_kasus'),
    path('basis-kasus/create', basiskasus.BasisKasusCreateView.as_view(), name='create_basis_kasus'),
    path('basis-kasus/<pk>/update', basiskasus.BasisKasusUpdateView.as_view(), name='update_basis_kasus'),
    path('basis-kasus/<pk>/delete', basiskasus.BasisKasusDeleteView.as_view(), name='delete_basis_kasus'),

    path('diagnosa', diagnosa.diagnosa, name='diagnosa')
]
