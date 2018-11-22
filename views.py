<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse, Http404
from matchapp.models import Member, Profile, Hobby
from django.contrib.auth.hashers import make_password
from .forms import *

appname = 'matchapp'

#should render login page but also include a signup button
def index(request):
	# Render the index page
	form = UserLogInForm()
	return render(request,'matchapp/login.html', {'form': form})

#user logged in
def loggedin(view):
    def mod_view(request):
        if 'username' in request.session:
            username = request.session['username']
            try: user = Member.objects.get(username=username)
            except Member.DoesNotExist: raise Http404('Member does not exist')
            return view(request, user)
        else:
            return render(request,'mainapp/not-logged-in.html',{})
    return mod_view

#terms and conditions
def tc(request):
	return render(request,'matchapp/tc.html')

#should render the signup page
def signup(request):
	form = UserRegForm()
	return render(request,'matchapp/register.html', {'form': form})

#once user clicks register button
#should render user registered page if unique user is entered
#need validation for email, user, dob, profile image
def register(request):

	form = UserRegForm()

	if request.method == "POST":
		#form_class is class of form name NEED TO CHANGE
		form = form(request.POST)

		if form.is_valid():
			#user = form.save(commit=False)

			
			#normalized data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = Member(username=username)
			user.set_password(password)

			try:
				user.save()

			except:
				Http404("Username " + u + "is already taken")

			return render(request,'matchapp/login.html',{'form': form})

	else:
		return Http404("Method was not post")






#this occurs when user presses login button from index
def login(request):
	#return HttpResponse("login")
	if 'username' in request.POST and 'password' in request.POST:
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return render(request, 'profile.html', {'form': form})

	return render(request,'matchapp/login.html')

#render logout page
def logout(request):
	return render(request, 'matchapp/login.html')

#shows another page with users that have similar interests
#order of most common hobbies first
@loggedin
def similarHobbies(request, user):
	return HttpResponse("return list of people with similar hobbies")

#filter button on similarHobbies page which generates
@loggedin
def filter(request, user):
	return HttpResponse("filter by gender and age using Ajax")

@loggedin
def displayProfile(request, username):
	#query users login
	form = UserProfile()
	Member.objects.get(username=username)
	return render(request, 'matchapp/displayProfile.html', {'form': form})
	"""try:

	if form.is_valid():
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		gender = form.cleaned_data.get("gender")
		dob = dorm.cleaned_data.get("dob")"""

#user profile edit page
#https://stackoverflow.com/questions/29246468/django-how-can-i-update-the-profile-pictures-via-modelform
#https://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example

@loggedin
def editProfile(request, user):

	"""if request.method = "POST":
		#editProfileForm = class in forms.py
	    form = editProfileForm(request.POST,request.FILES,instance=user)
        
        if form.is_valid():
			#file is the name given in forms
			if 'file' in request.FILES:
				file = request.FILES['file']

			form.save();
			return render(request, 'matchapp/editProfile.html', {'form': form}) 

		else:
			form = editProfileForm(instance=user)
			return render(request, 'matchapp/editProfile.html', {'form': form})""" 

	#return HttpResponse("user should be able to edit page")

=======
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



		


>>>>>>> ca51e7b39c1546f8fadb5dbc4588e822e28bec7d
