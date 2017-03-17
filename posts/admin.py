from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("nombre",)}

admin.site.register(Post, PostAdmin)


