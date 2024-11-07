from django.urls import path
from . import views

app_name = 'ex_app'
urlpatterns = [
    path('hello/', views.hello, name='hello'),


    path('', views.item, name='item'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('cart/', views.cart, name='cart')
]
