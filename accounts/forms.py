from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(label='Repite tu contraseña',
		widget=forms.PasswordInput(attrs={'class':'form-control'}))
	username = forms.CharField(label='Nombre de Usuario',widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(label='Correo', widget=forms.EmailInput(attrs={'class':'form-control'}))
	class Meta:
		model = User
		fields = ('username', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd ['password2']:
			raise forms.ValidationError('Los passwords no coinciden')
		return cd['password2']

class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('date_of_birth','img')