from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# Here we are going to create a form which will inherit UserCreationForm
# this email simply adds up to the inherited form of Django
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Meta classes are used to specify that the Model 'User' is going to be affected with the below
    # fields and the data are going to be stored in the specified model
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']  # For now we are only letting user to update name and email


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
