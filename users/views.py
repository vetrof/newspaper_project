from django.http import HttpResponse
from django.shortcuts import render


def testView(request):
    return HttpResponse('test ok')
