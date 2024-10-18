from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.


def hello(request):
    return HttpResponse("hello world")


def item(request):
    item_list = Item.objects.all()
    response = ','.join([Item.item_name for Item in item_list])
    return HttpResponse(response)


def cart(request):
    return HttpResponse('This is cart')
