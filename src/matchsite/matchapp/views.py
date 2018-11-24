from django.shortcuts import render, redirect
from django.db.models import Count
from django.http import HttpResponse, Http404
from matchapp.models import Member, Profile, Hobby
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from .forms import *

# REST imports
from rest_framework import viewsets
from .serializers import ProfileSerializer, MemberSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    # API endpoint for listing and creating profiles
    queryset = Profile.objects.order_by('user')
    serializer_class = ProfileSerializer


class MemberViewSet(viewsets.ModelViewSet):
    # API endpoint for listing and creating members
    queryset = Member.objects.order_by('username')
    serializer_class = MemberSerializer


appname = 'matchapp'

# should render login page but also include a signup button


def index(request):
	# Render the index page
	form = UserLogInForm()
	return render(request, 'matchapp/index.html', {'form': form})

# user logged in


def loggedin(view):
    def mod_view(request):
        if 'username' in request.session:
            username = request.session['username']
            try: user = Member.objects.get(username=username)
            except Member.DoesNotExist: raise Http404('Member does not exist')
            return view(request, user)
        else:
            return render(request, 'mainapp/not-logged-in.html', {})
    return mod_view

# terms and conditions


def tc(request):
	return render(request, 'matchapp/tc.html')


# should render the signup page
"""def signup(request):
	# form = UserRegForm()
	# return render(request,'matchapp/register.html', {'form': form})
	return HttpResponse("test")"""

# once user clicks register button
# should render user registered page if unique user is entered
# need validation for email, user, dob, profile image


def register(request):

	# form = UserRegForm()

	if request.method == "POST":
		# form_class is class of form name NEED TO CHANGE
		form = UserRegForm(request.POST)

		if form.is_valid():

			# user = form.save(commit=False)
			# normalized data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = Member(username=username)
			user.set_password(password)

			try: user.save()
			except IntegrityError: raise Http404('Username '+user+' already taken: Usernames must be unique')

			return redirect('index')

	else:
		form = UserRegForm()
		return render(request, 'matchapp/register.html', {'form': form})

# this occurs when user presses login button from index


def login(request):

    if request.method == "POST":
        form = UserLogInForm(request.POST)
        if 'username' in request.POST and 'password' in request.POST:
            if form.is_valid():

                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")

                user = authenticate(username=username, password=password)

                if user is not None:
                    if user.is_active:
                        request.session['username'] = username
                        request.session['password'] = password
                        form = UserProfile()
                        person = Member.objects.get(id=user.id); print(person)
                        hobby = Hobby.objects.all()

                        context = {
                            'appname':appname,
                            'form': form,
                            'user': person,
                            'hobbies': hobby
                        }
						# login(request,user)
                        return render(request, 'matchapp/displayProfile.html', context)

                # return HttpResponse("<span> User or password is wrong </span")

                else:
                    raise Http404('User or password is incorrect')
                    # return render(request,'matchapp/index.html', {'message':'Invalid Password','form': form})
    else:
        return render(request, 'matchapp/index.html')

# render logout page


@loggedin
def logout(request, user):
	request.session.flush()
	return redirect("/")

# shows another page with users that have similar interests
# order of most common hobbies first


@loggedin
def similarHobbies(request, user):
    # Get all the other users exclude current logged in user
    exclude = Member.objects.exclude(id=user.id)
    # Filter based on the current logged in user on same hobbies
    common = exclude.filter(hobbies__in=user.hobbies.all())
    # Get the number of hobbies of other users
    hobbies = common.annotate(hob_count=Count('hobbies'))
    # Process the matches in decending
    match = hobbies.filter(hob_count__gt=1).order_by('-hob_count')

    context = {
        'appname': appname,
        'matches': match,
        'loggedIn': True
        }
    return render(request, '#', context)

# filter button on similarHobbies page which generates

@loggedin
def filter(request, user):
	return HttpResponse("filter by gender and age using Ajax")


@loggedin
def displayProfile(request, user):
	# query users login
    form = UserProfile()
    person = Member.objects.get(id=user.id); print(person)
    hobby = Hobby.objects.all()

    context = {
        'appname':appname,
        'form': form,
        'user': person,
        'hobbies': hobby
    }
    return render(request, 'matchapp/displayProfile.html', context)
"""try:

if form.is_valid():
	username = form.cleaned_data.get("username")
	email = form.cleaned_data.get("email")
	gender = form.cleaned_data.get("gender")
	dob = dorm.cleaned_data.get("dob")"""
      
# user profile edit page
# https://stackoverflow.com/questions/29246468/django-how-can-i-update-the-profile-pictures-via-modelform
# https://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example

@loggedin
def editProfile(request, user):

	"""if request.method = "POST":
		# editProfileForm = class in forms.py
	    form = editProfileForm(request.POST,request.FILES,instance=user)

        if form.is_valid():
			# file is the name given in forms
			if 'file' in request.FILES:
				file = request.FILES['file']

			form.save();
			return render(request, 'matchapp/editProfile.html', {'form': form})

		else:
			form = editProfileForm(instance=user)
			return render(request, 'matchapp/editProfile.html', {'form': form})"""

	# return HttpResponse("user should be able to edit page")
