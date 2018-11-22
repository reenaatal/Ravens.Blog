from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout



# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        newUser = User(username =username, email = email, first_name = first_name, last_name = last_name)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.info(request,"You have successfully registered ...")

        return redirect("index")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)

    
    
def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Incorrect Credentials")
            return render(request,"registration/login.html",context)

        messages.success(request,"Successfully logged In")
        login(request,user)
        return redirect("index")
    return render(request,"registration/login.html",context)
    
def logoutUser(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect("/login")

