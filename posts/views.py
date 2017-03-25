from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post
from django.db.models import Q
#to fill the forms 
from .forms import PostForm
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#create the list view of the Posts

class ListView(View):
	@method_decorator(login_required)
	def get(self, request):
				#to make a filter#
		#query = request.GET.get("q")
		#if query:
		#	posts = Post.objects.all().filter(
		#		Q(autor__username__icontains=query) | 
		#		Q(nombre__icontains=query)
		#		)
		#else:
		posts = Post.objects.all().order_by('-date')
		template_name = "posts/lista.html"

		context={
		'posts':posts
		}

		return render(request, template_name, context)

#class DetailView(View):
#	def get(self, request):
		

#creating the form view fo a new post
class FormView(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'posts/formulario.html'
		form = PostForm()
		context = {'form':form}
		return render(request,template_name,context)

	def post(self,request):
		form = PostForm(request.POST,request.FILES)
		if form.is_valid():
			nuevo_post = form.save(commit=False)
			nuevo_post.slug = slugify(nuevo_post.nombre)
			nuevo_post.autor = request.user
			nuevo_post.save()
			form.save_m2m()
			messages.success(request,'Tu post se ha guardado con éxito! ')
			return redirect('posts:lista')
		else:
			messages.error(request,'No se guardo')
			return redirect('posts:nuevo')