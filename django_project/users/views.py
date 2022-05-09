# Useful links:
# https://docs.djangoproject.com/en/4.0/ref/forms/api/
# https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6
# https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
# https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/#redirect

from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegisterForm

# Create your views here.


def register(request):
    # If it gets a POST request then it instantiates a user creation form with that POST data
    if request.method == 'POST':
        # Create a form that has the request POST data:
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('blog-home')
    # With any other request it creates an empty user creation form
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
