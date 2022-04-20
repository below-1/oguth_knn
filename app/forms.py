from django import forms
from django.forms import ModelForm, DateInput, ModelChoiceField, Form
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from app.models import Gejala, Penyakit, BasisKasus

class AnggotaChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.nama}"

class GejalaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Simpan'))

    class Meta:
        model = Gejala
        exclude = ['created_at', 'updated_at']

class PenyakitForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Simpan'))

    class Meta:
        model = Penyakit
        exclude = ['created_at', 'updated_at']
        widgets = {
            'tindakan': forms.Textarea(attrs={'rows': 10})
        }

class BasisKasusForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Simpan'))

    class Meta:
        model = BasisKasus
        exclude = ['created_at', 'updated_at']

class DiagnosaForm(forms.Form):
    gejala = forms.ModelMultipleChoiceField(Gejala.objects.all(), widget=forms.CheckboxSelectMultiple)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Diagnosa'))
