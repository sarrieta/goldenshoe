from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import QueryDict
from .models import product
from django.views.decorators.csrf import csrf_exempt
import json
import requests

@csrf_exempt
def index(request):

	#https://stackoverflow.com/questions/42059025/django-ajax-get
	if request.method == 'GET':

		 products = product.objects.all();
		 response_data = {}
		 response_data['id'] = list(products.values("id")) 
		 response_data['name'] = list(products.values("name"))
		 #response_data['price'] = list(products.values("price"))
		 response_data['descritpion'] = list(products.values("description"))


		 context = {'prod': products}
		 #print(context)
		 return render(request, 'productsApp/index.html', context)
		 #return render(request, 'productsApp/index.html', {'json_data': json.dumps(response_data)})
		 #return HttpResponse(json.dumps(response_data), content_type="application/json")


#return JSON
def products_list(request):
	
	if request.method == 'POST':
		prod_name = request.POST['name']
		prod_description = request.POST['description']
		prod_price = request.POST['price']

		prod = product(name = prod_name, description =  prod_description, price = prod_price)
		
		prod.save()

		response = JsonResponse([
		     prod_name,
			 prod_description,
			 prod_price

		], safe = False);

		print ("products_list view")
		
		return HttpResponse(response, content_type="application/json")
 

@csrf_exempt
def deleteProduct(request, id):
	
 	if request.method == "DELETE":
 	     product_list = product.objects.get(id=id)
 	     product_list.delete()
 	     return HttpResponse("deleted")

#return JSON
@csrf_exempt
def updateProduct(request, id):
    
    if request.method == "PUT":
	     product_list = product.objects.get(id=id)

	     data = QueryDict(request.body)

	     product_list.name = data.get("name")
	     product_list.save()

	     product_list.description = data.get("description")
	     product_list.save()

	     product_list.price = data.get("price")
	     product_list.save()

	     response = JsonResponse([
	          product_list.name,
  			  product_list.description,
  			  product_list.price
	     	], safe = False);

   
    #print(data.get("name"))
    return HttpResponse(response, content_type="application/json")



		


