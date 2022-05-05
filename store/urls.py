from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [

    path('', views.store, name='store'),
    path('cart/', views.cart, name = 'cart'),
    path('checkout', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_Order/', views.processOrder, name='process_Order'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
   ]
