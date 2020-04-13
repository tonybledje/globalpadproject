from django.shortcuts import render
from .forms import MemberForm
from .models import Member
# Create your views here.


def member_form(request):
    return render(request, "members/member_form.html")


def member_list(request):
    return render(request, "members/member_list.html")


def member_delete(request):
    return


