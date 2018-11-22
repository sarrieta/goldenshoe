from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from matchapp.models import Member, Profile, Hobby
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
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
"""def signup(request):
	#form = UserRegForm()
	#return render(request,'matchapp/register.html', {'form': form})
	return HttpResponse("test")"""

#once user clicks register button
#should render user registered page if unique user is entered
#need validation for email, user, dob, profile image
def register(request):

	#form = UserRegForm()

	if request.method == "POST":
		#form_class is class of form name NEED TO CHANGE
		form = UserRegForm(request.POST)

		if form.is_valid():

			#user = form.save(commit=False)
			#normalized data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = Member(username=username)
			user.set_password(password)

			try: user.save()
			except IntegrityError: raise Http404('Username '+user+' already taken: Usernames must be unique')

			return redirect('index')


	else:
		form = UserRegForm()
		return render(request,'matchapp/register.html',{'form': form})

#this occurs when user presses login button from index
def login(request):

	if request.method == "POST":
		form = UserLogInForm(request.POST)
		#return HttpResponse("login")
		if 'username' in request.POST and 'password' in request.POST:
			if form.is_valid():
				username = form.cleaned_data.get("username")
				password = form.cleaned_data.get("password")
				try: member = Member.objects.get(username=username)
			    except: Member.DoesNotExist: Http404("User does not exist")
				user = authenticate(username=username, password=password)
				if user is not None:
					if user.is_active:
						request.session['username'] = username
						request.session['password'] = password
						#login(request,user)
						return render(request,'matchapp/displayProfile.html', {'form': form})

	else:
		return render(request,'matchapp/login.html')


if not ('username' in request.POST and 'password' in request.POST):
        context = { 'appname': appname }
        return render(request,'mainapp/login.html',context)
    else:
        username = request.POST['username']
        password = request.POST['password']
        try: member = Member.objects.get(username=username)
        except Member.DoesNotExist: raise Http404('User does not exist')
        if member.check_password(password):
            # remember user in session variable
            request.session['username'] = username
            request.session['password'] = password
            context = {
               'appname': appname,
               'username': username,
               'loggedin': True
            }
            response = render(request, 'mainapp/login.html', context)
            # remember last login in cookie
            now = D.datetime.utcnow()
            max_age = 365 * 24 * 60 * 60  #one year
            delta = now + D.timedelta(seconds=max_age)
            format = "%a, %d-%b-%Y %H:%M:%S GMT"
            expires = D.datetime.strftime(delta, format)
            response.set_cookie('last_login',now,expires=expires)
            return response
        else:
            raise Http404('Wrong password')






#render logout page
def logout(request):
	request.session.flush
	return redirect("login")


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
def displayProfile(request, user):
	#query users login
	form = UserProfile()
	Member.objects.get(user=username)
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
