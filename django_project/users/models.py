from django.db import models
from django.contrib.auth.models import User
from PIL import Image
#One to One realtionship between profile and user


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE) # one-way cascade, profile deleted => all post deleted
	image = models.ImageField(default= 'default.jpg', upload_to = 'profile_pics')

	def __str__(self):
		return f"{self.user.username} Profile"

	def save(self): # to add some fucntionality
		super().save()

		img = Image.open(self.image.path)
		if img.height > 500 or img.width > 500 :
			output_size = (500,500)
			img.thumbnail(output_size, Image.LANCZOS) # resizing the image ; filter for smoothing the reduced file
			img.save(self.image.path)


# make migrations to the database