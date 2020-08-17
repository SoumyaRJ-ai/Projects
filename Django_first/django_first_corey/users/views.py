from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# When we navigate to the page normally, it's a GET request
# POST data is going to contain the messages passed through submit button in it's body
def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(
            request.POST)  # This will work after we inherit the Django form with our new created form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get(
                'username')  # form.cleaned_data is used to convert the form data into a nice python form
            # messages.success(request, f'Account created for{username}')
            messages.success(request, f'Your account is now created! Login to continue!!')
            # return redirect('blog-home')
            return redirect('login')
    else:
        # form = UserCreationForm()  # This will create a blank form and rendering it in the next line
        form = UserRegisterForm()  # This will work after we inherit the Django form with our new created form
    return render(request, 'users/register.html', {'form': form})


# here we are using decorator with @ symbol which means that it adds the functionality to existing function
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance= request.user)  # Creating instances to call the classes
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance= request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)  # Creating instances to call the classes
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html',context)
