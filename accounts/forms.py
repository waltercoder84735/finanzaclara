from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PerfilForm(forms.ModelForm):
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)

    class Meta:
        model = Perfil
        fields = ['avatar', 'biografia', 'fecha_nacimiento']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.usuario_id:
            self.fields['first_name'].initial = self.instance.usuario.first_name
            self.fields['last_name'].initial = self.instance.usuario.last_name

    def save(self, commit=True):
        perfil = super().save(commit=commit)
        perfil.usuario.first_name = self.cleaned_data['first_name']
        perfil.usuario.last_name = self.cleaned_data['last_name']
        perfil.usuario.save()
        return perfil