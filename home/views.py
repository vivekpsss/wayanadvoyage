from email.message import EmailMessage
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from django.utils import timezone

from home.models import Booking, Contact
from hotel import settings

from .forms import CreateUserForm
from .models import Members


# Create your views here.
def home(request):
    # return HTTPResponse("This is my HomePage(/)")
    return render(request, 'home.html')
def rooms(request):
    # return HTTPResponse("This is my RoomsPage(/)")
    return render(request, 'rooms.html')
def about(request):
    # return HTTPResponse("This is my AboutPage(/)")
    return render(request, 'about.html')
def contact(request):
    context={'success': False}
    if request.method=="POST":
        
        name=request.POST['name']
        email=request.POST['email']
        city=request.POST['city']
        country=request.POST['country']
        desc=request.POST['desc']
        # print(name, email, city, country, desc)
        contact = Contact(name=name, email=email, city=city, country=country, desc=desc)
        contact.save()
        context={'success': True}
        print("The data has been written to the db")
    # return HTTPResponse("This is my ContactPage(/)")
    return render(request, 'contact.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+ user)

            return redirect('loginPage')

    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('booking')
        else:
            messages.info(request, 'Username or password is incorrect...')
    context = {}
    return render(request, 'login.html', context)

def booking(request):

    if request.method=="POST":
        
        name=request.POST['name']
        email=request.POST['email']
        city=request.POST['city']
        state=request.POST['state']
        country=request.POST['country']
        contact=request.POST['contact']
        pin=request.POST['pin']
        person=request.POST['person']
        cin=request.POST['cin']
        cout=request.POST['cout']
        roomid=request.POST['roomid']
        # print(name, email, city, state, country, contact, pin)
        
        booking = Booking(name=name, email=email, city=city, state=state, country=country, contact=contact, pin=pin, person=person, cin=cin, cout=cout, roomid=roomid)
        
        booking.save()
        messages.success(request, 'Congratulations, booking has been confirmed!!!')
        
        print("The data has been written to the db")

    return render(request, 'booking.html')


def logoutUser(request):
    logout(request)
    return redirect('home')





def emp(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('emp.html')
  context = {
    'mymembers': mymembers
  }
  return HttpResponse(template.render(context, request))
  
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
  
def addrecord(request):
     if request.method == 'POST':
        first = request.POST.get('first')
        last = request.POST.get('last')
    
        member = Members(firstname=first, lastname=last)
        member.save()
  
        return HttpResponseRedirect(reverse('emp'))

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('emp'))
  
def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  
  
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  
  
  member.save()
  return HttpResponseRedirect(reverse('emp'))




def empsign(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('emp')
        else:
            messages.info(request, 'Username or password is incorrect...')
    context = {}
    return render(request, 'empsign.html', context)

def expirytime(request):
    now = timezone.now()
    tours = home.objects.filter(approved=True,expiry_Ite=now)
    return render(request,'home/rooms.html', {'expirytime : rooms'})