# Useful links:
# https://docs.djangoproject.com/en/4.0/ref/forms/api/
# https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6
# https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
# https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/#redirect

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    # If it gets a POST request then it instantiates a user creation form with that POST data
    if request.method == 'POST':
        # Create a form that has the request POST data:
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account was created. You are now able to log in')
            return redirect('login')
    # With any other request it creates an empty user creation form
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):

    if request.method == 'POST':

        # https://www.youtube.com/watch?v=CQ90L5jfldw&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=9
        userUpdateForm = UserUpdateForm(request.POST, instance=request.user)
        profileUpdateForm = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if userUpdateForm.is_valid() and profileUpdateForm.is_valid():
            userUpdateForm.save()
            profileUpdateForm.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        userUpdateForm = UserUpdateForm(instance=request.user)
        profileUpdateForm = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'userUpdateForm': userUpdateForm,
        'profileUpdateForm': profileUpdateForm
    }
    return render(request, 'users/profile.html', context)
