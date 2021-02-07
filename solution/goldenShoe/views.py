from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Product
from .cart import *
# tracking imports
from datetime import date, timedelta




def add_to_cart(request, product_id, quantity):

    product = Product.objects.get(product_id=product_id)
    cart = Cart(request)
    cart.add(product, product.unit_price, quantity)

    return men(request)

def remove_from_cart(request, product_id):
    print ("removing from to cart")
    product = Product.objects.get(product_id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return get_cart(request)

def get_cart(request):
    print ("obtain")
    orderID = Cart(request).cart.order_trans_id
    print(orderID)
    return render(request, 'get_cart.html', {'cart': Cart(request),'orderID':orderID})


def index(request):
    if request.method == 'GET':
        return render(request, "index.html")
    if request.method == 'POST':
        print("test")

def FAQ(request):
    if request.method == 'GET':
        return render(request, "FAQ.html")




def men(request):

    if request.method == 'GET':

        products = Product.objects.filter(quantity__gt=0)

        context={
          'products':products
        }

        return render(request, "men.html", context)
def women(request):

    if request.method == 'GET':

        products = Product.objects.all()

        context={
          'products':products
        }

        return render(request, "women.html", context)

def tracking(request):

    if request.method == 'GET':
        today = date.today()

        date2 = today + timedelta(days=5)
        date2 = date2.strftime("%B %d, %Y")
        context={
          'date2':date2
        }
        return render(request, "tracking.html",context)

def about_us(request):

    if request.method == 'GET':
        return render(request, "about_us.html")

def contact_us(request):

    if request.method == 'GET':
        return render(request, "contact_us.html")
