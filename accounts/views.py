from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import Profile
from posts.models import Post
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

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


class UserListView(View):
	def get(self, request):
		query = request.GET.get("q")
		if query:
			users = User.objects.all().filter(
				Q(username__icontains=query) | 
				Q(first_name__icontains=query) |
				Q(email__icontains=query))
		else:
			users = User.objects.none()

		template_name='users/list.html'
		

		context = {
		'users':users
		}

		return render(request, template_name, context)

class UserDetailView(View):
	def get(self, request, id):
		user = get_object_or_404(User, id=id)
		posts = Post.objects.all().filter(autor=user.id)

		template_name = 'users/detalle.html'

		context = {
		'user':user, 
		'posts':posts
		}
		return render(request, template_name, context)



