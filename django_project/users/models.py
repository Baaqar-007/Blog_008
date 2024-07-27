from django.db import models
from django.contrib.auth.models import User
#One to One realtionship between profile and user


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE) # one-way cascade, profile deleted => all post deleted
	image = models.ImageField(default= 'default.jpg', upload_to = 'profile_pics')

	def __str__(self):
		return f"{self.user.username} Profile"

# make migrations to the database