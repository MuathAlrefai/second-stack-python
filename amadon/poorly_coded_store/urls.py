from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checkout/<int:id>', views.checkout),
    path('store/checkout/<int:id>', views.orderPage),
    # path('make', views.make)
]
