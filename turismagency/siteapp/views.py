from django.http.response import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def submit_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(username, password)
        print(user)
        if user is not None:
            login(request, user)
            return HttpResponse("Hello World!")
        else:
            print('entrou errado')
            messages.error(request, "Invalid username or password")
    else:
        return render(request, 'login.html')


def homeHello(request):
    return HttpResponse("Hello World!")