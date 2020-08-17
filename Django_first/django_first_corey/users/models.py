from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# We are creating a Profile of User here. Profile Pic, Bio, Other user details can be displayed here
class Profile(models.Model):       # We are inheriting models.Model to be used for Profile model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # CASCADE we are using to tell Django to delete the User profile details if user is deleted but
    # not the other way around
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # Directory to which we will upload the profile pics will be stored here

    def __str__(self):
        return f'{self.user.username} Profile'
    # This will show a heading in the profile as '{Username} Profile' under Profiles

    def save(self):  # This is a save class which we are overriding of parent class
        super().save()  # We are doing this to save the super class save

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)