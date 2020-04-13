from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm


# Create your views here.


# def register(request):
# form = UserCreationForm()
# return render(request, 'users/register.html', {'form': form})


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})
