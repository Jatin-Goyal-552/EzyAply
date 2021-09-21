from django.shortcuts import render
from .models import *
# Create your views here.
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,ApplyForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

name=''

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login1(request):
    if request.method == 'POST':
        username  = request.POST.get('your_name')
        print(username )
        password =request.POST.get('your_pass')
        print(password)
        user = authenticate(request,username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            global name
            name=username
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    
    return render(request,'login.html')

def logout1(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    internship=Internships.objects.all()
    context={
        'name':request.user,
        'internships':internship
    }
    print(context)
    return render(request, 'home.html',context)

def apply(request):
    form=ApplyForm()
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        # data=int(form["author"].value())
        # if data == request.user.id: 
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('apply')
			
    context = {'form':form}
    return render(request, 'apply.html', context)