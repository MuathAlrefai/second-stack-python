from django.shortcuts import render, redirect
from .models import Order, Product
from . import models

def index(request):
    context = {
        "all_products": models.products_model()
    }
    return render(request, "store/index.html", context)

def checkout(request, id):
    models.total_charge(request, id)
    return redirect(f'/store/checkout/{id}')

def orderPage(request, id):
    context = {
        "product": models.product_model(id),
        "order": models.order_model(id),
        "all_products": models.products_model()
    }
    return render(request, 'store/checkout.html', context, id)


# def make(request):
#     Product.objects.create(description = "cool product 1", price = 9.99)
#     Product.objects.create(description = "cool product 2", price = 19.99)
#     Product.objects.create(description = "cool product 3", price = 29.99)
#     Product.objects.create(description = "cool product 4", price = 69.99)
#     return redirect('/')