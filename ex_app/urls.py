from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('item/', views.item, name='item'),
    path('cart/', views.cart, name='cart')
]
