from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	nombre = models.CharField(max_length=100, null=True, blank=True)
	autor = models.ForeignKey(User, related_name='post', null=True, blank=True)
	texto = models.TextField(null=True, blank=True)
	img = models.ImageField(upload_to="postimages", null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True, db_index=True)
	slug=models.SlugField(max_length=280)

	def get_absolute_url(self):
		return reverse('posts:detalle', args=[self.slug])


	def __str__(self):
		return self.nombre

