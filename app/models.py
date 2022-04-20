from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Gejala(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nama = models.CharField(max_length=256)

    def get_absolute_url(self):
        return f'/app/gejala/{self.id}/update'

    def __str__(self):
        return self.nama

class Penyakit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nama = models.CharField(max_length=256)
    tindakan = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return f'/app/penyakit/{self.id}/update'

    def __str__(self):
        return self.nama

class BasisKasus(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    daftar_gejala = models.ManyToManyField(Gejala)
    penyakit = models.ForeignKey(Penyakit, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f'/app/basis-kasus/{self.id}/update'

    def __str__(self):
        return 'basis kasus #' + str(self.id)
