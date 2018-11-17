from django.shortcuts import render
from django.http import HttpResponse, Http404
from matchapp.models import Member, Profile, Hobby
from django.contrib.auth.hashers import make_password

#should render login page but also include a signup button
def index(request):
    return HttpResponse("Login page")

#user logged in
def loggedin(request):
	return HttpResponse("user logged in")

#should render the signup page
def signup(request):
	return HttpResponse("signup page")

#should render user registered page if unique user is entered
#need validation for email, user, dob, profile image 
def register(request):
	if 'username' in request.POST and 'password' in request.POST:
		u = request.POST['username']
		passw = request.POST['password']
		user = Member(username=u)
		user.set_password(passw)
		try:
			user.save()

		except: 
			Http404("Username " + u + "is already taken")

		return HttpResponse("the user has been registered rendered page")

	else:
		return HttpResponse("no data was inserted")

#this occurs when user presses login button from index
def login(request):
	return HttpResponse("login")

#render logout page
def logout(request):
	return HttpResponse("logout")

#shows another page with users that have similar interests 
#order of most common hobbies first
#@loggedin
#def similarHobbies(request):
#	return HttpResponse("return list of people with similar hobbies")

#filter button on similarHobbies page which generates
#@loggedin
#def filter(request):
#	return HttpResponse("filter by gender and age using Ajax")

#user profile edit page
#@loggedin
#def profile(request):
#	return HttpResponse("user should be able to edit page")

#@loggedin
#def upload_Image(request):
#	return HttpResponse("user should be able to upload an image")
