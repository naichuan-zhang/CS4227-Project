from django.http import HttpResponse
from django.shortcuts import render


def show(request):
    return HttpResponse('show order here')
