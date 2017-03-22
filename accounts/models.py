from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User)
	img = models.ImageField(upload_to="userimage", blank=True, null=True)
	date_of_birth = models.DateField(blank=True,null=True)

class Contact(models.Model):
	user_from = models.ForeignKey(User, related_name='rel_from_set')
	user_to = models.ForeignKey(User, related_name='rel_to_set')
	created = models.DateTimeField(auto_now_add=True, db_index=True)

	class Meta: 
		ordering = ('-created',)

	def __str__(self):
		return '{} follows {}'.format(self.user_from, self.user_to)

#adding a new method to the User Model

User.add_to_class('following', 
	models.ManyToManyField('self', 
		through=Contact, 
		related_name='followers', 
		symmetrical=False))
	
