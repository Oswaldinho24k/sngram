from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Profile
from posts.models import Post
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, ProfileEditForm

class ProfileView(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name="perfil.html"
		posts = Post.objects.all().filter(autor=request.user).order_by('-date')
		profileform = ProfileEditForm(instance=request.user.profile)
		context = {
		'profileform':profileform,
		'posts':posts
		}
		return render(request,template_name,context)

	def post(self,request):
		template_name="accounts/perfil.html"
		profileform = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
		if profileform.is_valid():
			profileform.save()
			return redirect('accounts:profile')
		else:
			context={
			'profileform':profileform,
			}
			return render(request,template_name,context)
		

class RegistrationView(View):
	def get(self, request):
		template_name = "registration.html"
		form = UserRegistrationForm()
		context = {
		'form':form,
		}
		return render(request,template_name,context)

	def post(self,request):
		template_name = "registration.html"
		new_user_form = UserRegistrationForm(request.POST)
		if new_user_form.is_valid():
			new_user = new_user_form.save(commit=False)
			new_user.set_password(new_user_form.cleaned_data['password'])
			# perfil = Profile(instance=new_user)
			new_user.save()
			perfil = Profile()
			perfil.user = new_user
			perfil.save()
			# perfil = Profile.objects.create(user=new_user)
			return redirect('accounts:profile')
		else:
			context = {
			'form':new_user_form
			}
			return render(request,template_name,context)

