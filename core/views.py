from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.translation import gettext as _

# Create your views here.


def HomePage(request):
    text = _('hi there, this is simple text!')
    return HttpResponse(text)