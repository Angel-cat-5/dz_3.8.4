from django.shortcuts import render
from django.http import HttpResponse

def rp(request):
    return HttpResponse("Домашка по 4-му занятию")
