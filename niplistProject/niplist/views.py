from datetime import *
from string import *

from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required

# Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from niplist.models import *

@login_required
def newsfeed(request):
  pass

def passwordReset(request):
  errors = ["DOES NOT WORK"]
  # STUFF
  context = {'errors' : errors}
  return render(request, 'niplist/password-reset.html', context) 
  
def recommendItemsFromItem(request):
	context = {}
	errors = []
	context['errors'] = errors
	# assume the input are good now
	
    numObjects = request.POST['k']
    amazonId = request.POST['ASIN']
    itemsList = Item.object.filter(ASIN=amazonId)
    userItemSet = UserItemSet.object.filter(itempreference__item__in=itemsList)\
                    .filter(itempreference__preference=True)# all
    profiles = []
    for userItem in userItemSet:
        profiles.append(userItemSet.profile)
    
    userItemSetList = UserItemSet.object.filter(profile__in=profiles)
    itemFrequency = {}
    for userItemSet in userItemSetList:
        tempAsin = userItemSet.itemPreference.item.ASIN
        if tempAsin not in itemFrequency.keys():
            itemFrequency[tempAsin] = 0
        newFreq = itemFrequency[tempAsin]
        newFreq = newFreq + 2 if userItemSet.itemPreference.preference == True else newFreq - 2
        itemFrequency[tempAsin] = newFreq;
    
    sorted(itemFrequency.items(), key=lambda x[1]: x, reverse=True)
    keys = itemFrequency.keys()[:numObjects]
    returnItems = Item.object.filter(ASIN__in=keys)
    context['items'] = returnItems
    return render(request, 'niplist/item.html', context)
    
  
# Adapted from Dr. Garrod's private-todo-list example
def register(request):
  """ Register's a new user and ensures the information is valid """
  context = {}

  # Just display the registration form if this is a GET request
  if request.method == 'GET':
    return render(request, 'niplist/register.html', context)
  
  errors = []
  context['errors'] = errors
  
  # Checks the validity of the form data
  if not 'email' in request.POST or not request.POST['email']:
    errors.append('A valid e-mail is required.')
  else:
    # Save the email in the request context to re-fill the email
    # field in case the form has errors
    context['email'] = request.POST['email']

  if not 'password1' in request.POST or not request.POST['password1']:
    errors.append('Password is required.')
  if not 'password2' in request.POST or not request.POST['password2']:
    errors.append('Confirm password is required.')

  if 'password1' in request.POST and 'password2' in request.POST \
     and request.POST['password1'] and request.POST['password2'] \
     and request.POST['password1'] != request.POST['password2']:
    errors.append('Passwords did not match.')

  if len(User.objects.filter(username = request.POST['email'])) > 0:
    errors.append('E-mail is already taken.')

  if errors:
    return render(request, 'niplist/register.html', context)

  # Creates the new user from the valid form data
  new_user = User.objects.create_user(username=request.POST['email'], \
                                      password=request.POST['password1'])
  new_user.save()

  # Logs in the new user and redirects to his/her todo list
  new_user = authenticate(username=request.POST['email'], \
                          password=request.POST['password1'])
  login(request, new_user)
  
  return render(request, 'niplist/my-stream.html', context)

def home(request):
  """ Displays the user's home page """
  context = {}
  errors = []
  context['errors'] = errors
  
  return render(request, "niplist/home.html", context)
