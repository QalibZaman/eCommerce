from tkinter.messagebox import NO
from django.shortcuts import render, redirect
from .forms import UserForm, UserDetailsForm, SharingForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import UserDetails, Sharing
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    details = None
    form = SharingForm
    posts = Sharing.objects.all()

    if request.user.is_authenticated: 
        details = UserDetails.objects.get(user=request.user)

    if request.method == 'POST':
        form = SharingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    
    dict = {'form': form,
           "details": details,
           "posts": posts,
           }

    return render(request,'index.html', dict)

def register(request):
    form = UserForm
    dict = {"form": form, "name": "register"}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect ('details')
        else:
            return render(request, "login-register.html", {'form':form, "name": "register"}) 


    return render(request, 'login-register.html', dict)

@login_required(login_url='login/')
def logoutPage(request):
    logout(request)
    return redirect("home")

def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)

        try:
            user = User.objects.get(username=username)
        
        except:
            messages.error(request, 'No such username')


        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

        else:
            messages.error(request, 'Wrong Password')

    return render(request, "login-register.html", {"name": "login"})

@login_required(login_url='login/')
def details(request):
    form = UserDetailsForm
    if request.method =='POST':
        form = UserDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            details = form.save(commit=False)
            details.user = request.user
            details.save()
            return redirect('home')
    return render(request, "details.html", {"form": form})


def store(request):
    return render(request, "store.html")

