from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm
from django.contrib import messages


# Create your views here.

def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('login-user')
    context={}
    return render(request, 'chat/chatPage.html', context={})

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("LoginPage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="chat/register.html", context={"register_form":form})
