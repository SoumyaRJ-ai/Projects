from django.contrib import admin
from .models import Post

# This is where we can register our models so that they will show up in the Admin page

admin.site.register(Post)


