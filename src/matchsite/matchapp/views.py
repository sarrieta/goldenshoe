from django.shortcuts import render, redirect
from django.db.models import Count
from django.http import HttpResponse, Http404
from matchapp.models import Member, Profile, Hobby
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.http import QueryDict
from django.views.decorators.csrf import csrf_exempt
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
                        person = Member.objects.get(id=user.id)
                        hobby = Hobby.objects.all()

                        context = {
                            'appname':appname,
                            'form': form,
                            'user': person,
                            'hobbies': hobby,
                            'loggedIn': True
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
    # Note to self do not need the gt thing check first
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

    if request.method == "GET":
        form = UserProfile()
        person = Member.objects.get(id=user.id)
        hobby = Hobby.objects.all()

        context = {
            'appname':appname,
            'form': form,
            'user': person,
            'hobbies': hobby,
            'loggedIn': True
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

#remove csrf_exempt
@csrf_exempt
@loggedin
def editProfile(request, user):
    
    
    # Profile : GENDER , EMAIL , [can add a hobby to the member] 
    # Member : list of hobbies

    if request.method == "PUT":
        try: member = Member.objects.get(id=user.id)
        except Member.DoesNotExist: raise Http404("Member does not exist")        
        profile = Profile.objects.get(user=member.id)

        data = QueryDict(request.body)
        
        #debugging to see if there's anything in request.files but is empty as of 26/11/2018 20:13 :@
        print("request.FILES: " + str(request.FILES))

        #not going to this if statement
        #id for the file type in html
        if 'profile-image-upload' in request.FILES:
            upload_image = request.FILES['profile-image-upload']
            profile.image = upload_image
            profile.save()
            return JsonResponse({'message': 'Uploaded Successfully'})

        else:
        	return JsonResponse({'message': 'Error while uploading file'})

        profile.gender = data['gender']
        profile.email = data['email']
        profile.dob = data['dob']
       
        profile.save()

        response = {
             'gender': profile.gender,
             'dob': profile.dob, 
             'email': profile.email

        }
        return JsonResponse(response)


        

        hobbies = data['hobbies']
        hobbies = hobbies.split(" ")


        #if hobbies not ''
        #   for hobby in hobbies:
        #       member.hobbies.add(Hobby.objects.get(hobby=hobby))
        #       member.save()

        

        #return JsonResponse(response)

    else:
        raise Http404("PUT request was not used")

@loggedin
def upload_image(request, user):
    print("out here")
    member = Member.objects.get(id=user.id)
    profile = Profile.objects.get(user = member.id)
    if 'profile-image-upload' in request.FILES:
        image_file = request.FILES['profile-image-upload']
        profile.image = image_file
        profile.save()
        return HttpResponse(user.profile.image.url)
    else:
        raise Http404('Image file not received')
