# Useful links:
# https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6
# https://docs.djangoproject.com/en/4.0/ref/forms/api/
# https://docs.djangoproject.com/en/4.0/ref/forms/fields/

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # A class to specify the model the form is going to interact with
    # https://docs.djangoproject.com/en/4.0/topics/db/models/#meta-options-1
    # https://stackoverflow.com/a/10344231/11627241
    class Meta:
        model = User

        # Fields wanted in the form and in what order:
        fields = ['username', 'email', 'password1', 'password2']


# A model form is a form that allows the creation of a form that will work with a specific database model
class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
