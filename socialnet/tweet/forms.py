from django import forms 
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField()
#     class Meta:
#         model = UserCreationForm
#         fields = ('username', 'email', 'password1', 'password2')