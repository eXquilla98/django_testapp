from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader
# Create your views here.


def hello(request):
    return HttpResponse("hello world")


def item(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'ex_app_templates/index.html', context)


def detail(request, item_id):
    Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'ex_app_templates/detail.html', context)


def cart(request):
    return HttpResponse('This is cart')
