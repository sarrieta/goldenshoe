from django.shortcuts import render
from django.http import HttpResponse, Http404
from matchapp.models import Member, Profile, Hobby
from django.contrib.auth.hashers import make_password
#from .forms import *


appname = 'matchapp'

#should render login page but also include a signup button
def index(request):
	# Render the index page
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
	return render(request,'matchapp/register.html', {'form': form})

#once user clicks register button
#should render user registered page if unique user is entered
#need validation for email, user, dob, profile image
def register(request):

	form_class = UserForm

	if request.method == "POST":
		#form_class is class of form name NEED TO CHANGE
		form = form_class(request.POST)

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



    """if request.method == "POST":
        u = request.POST['user']
        p = request.POST['psw']

        user = Member(username=u)
        user.set_password(p)

        try:
            user.save()
        except:
            Http404("Username " + u + "is already taken")

        return render(request,'matchapp/login.html',{'form': form})

    else:
       return Http404("Data was not inserted")"""




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
	if request.method = "POST":
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
			return render(request, 'matchapp/editProfile.html', {'form': form}) 

	#return HttpResponse("user should be able to edit page")

