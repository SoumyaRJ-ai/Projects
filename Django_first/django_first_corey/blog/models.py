from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# We are creating a Post table
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # date_posted = models.DateTimeField(auto_now=True) # This will update every time the post is updated
    # date_posted = models.DateTimeField(auto_now_add=True) # This will update the time when post is created
    date_posted = models.DateTimeField(default=timezone.now)  # In case we want to update it sometime,
    # it will take our system timezone to update
    # now we need to create a user model to import authors but Django has already created a user model
    # which we wll be importing here
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Multiple posts can have single Author that's why it's being treated as foreign key from the User table
    # on_delete option is simply telling the Django what to do if the user is deleted, so here the CASCADE will
    # delete their posts as well.
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
        # so here we told Django to go to the post-detail route with the specified primary key from self
