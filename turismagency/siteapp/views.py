import requests
import sweetify
import os

from .serializers import schedulingTravelView
from django.http.response import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from siteapp.models import schedulingTravel

# Create your views here.
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

@csrf_exempt
def submit_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(username, password)
        print(user)
        if user is not None:
            login(request, user)
            request.session['user'] = {'user_id': user.id, 'username': user.username}
            return redirect('/')
        else:
            print('entrou errado')
            messages.error(request, "Invalid username or password")
    else:
        return render(request, 'login.html')

@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('login')


@csrf_exempt
def home_hello(request):
    try:
        user = request.user
        data = {'user': [user]}
    except:
        pass
    
    return render(request, 'home.html', context=data)


@csrf_exempt
@login_required(login_url='/login/')
def register_travel(request):

    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        from_place = request.POST.get('from_place')
        to_place = request.POST.get('to_place')
        departure_date = request.POST.get('departure_date')
        arrival_date = request.POST.get('arrival_date')
        note = request.POST.get('note')

        data = {
            "user":user,
            "title":title,
            "from_place":from_place,
            "to_place":to_place,
            "departure_date":departure_date,
            "arrival_date":arrival_date,
            "note":note
        }
        print(data)
        schedulingTravel.objects.create(
                        user=user,
                        title=title,
                        from_place=from_place,
                        to_place=to_place,
                        departure_date=departure_date,
                        arrival_date=arrival_date,
                        note=note)
        return redirect('/')
    
    return render(request, 'forms/register_travel.html')


@csrf_exempt
@login_required(login_url='/login/')
def get_register_travel(request):
    user = request.user
    username = request.session['user'].get('username')
    travels = schedulingTravel.objects.filter(user=user)
    data = {'travels': travels, 'user':[username]}

    return render(request, 'view_forms/view_travels.html', context=data)