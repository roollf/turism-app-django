from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from siteapp.models import schedulingTravel
from siteapp.models import travelInsurance
from siteapp.models import commentsAngency

@csrf_exempt
def register(request):
    """
    Handles the registration of a user.
    If the request method is POST, it saves the user creation form and redirects to the login page.
    If the request method is GET, it renders the registration form.
    """
    user = request.user
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    data = {'user': [user], 'form': form}
    return render(request, 'register.html', context=data)

@csrf_exempt
def submit_login(request):
    """
    Handles the user login.
    If the request method is POST, it authenticates the user and redirects to the home page.
    If the request method is GET, it renders the login form.
    """
    user = request.user
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['user'] = {'user_id': user.id, 'username': user.username}
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password")
    else:
        data = {'user': [user]}
        return render(request, 'login.html', context=data)

@csrf_exempt
def logout_view(request):
    """
    Handles the user logout and redirects to the login page.
    """
    logout(request)
    return redirect('login')


@csrf_exempt
def home_hello(request):
    """
    Renders the home page and retrieves all comments from the commentsAngency model.
    """
    all_comments = commentsAngency.objects.all()
    try:
        user = request.user
        data = {'user': [user], 'comments': all_comments}
    except:
        pass
    return render(request, 'home.html', context=data)


@csrf_exempt
@login_required(login_url='/login/')
def register_travel(request):
    """
    Handles the registration of a travel.
    If the request method is POST, it creates a new schedulingTravel object and redirects to the home page.
    If the request method is GET, it renders the travel registration form.
    """
    user = request.user
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        from_place = request.POST.get('from_place')
        to_place = request.POST.get('to_place')
        departure_date = request.POST.get('departure_date')
        arrival_date = request.POST.get('arrival_date')
        note = request.POST.get('note')

        schedulingTravel.objects.create(
            user=user,
            title=title,
            from_place=from_place,
            to_place=to_place,
            departure_date=departure_date,
            arrival_date=arrival_date,
            note=note
        )
        return redirect('/')
    data = {'user': [user]}
    return render(request, 'forms/register_travel.html', context=data)


@csrf_exempt
@login_required(login_url='/login/')
def register_travel_insurance(request):
    """
    Handles the registration of travel insurance.
    If the request method is POST, it creates a new travelInsurance object and redirects to the home page.
    If the request method is GET, it renders the travel insurance registration form.
    """
    user = request.user
    if request.method == 'POST':
        user = request.user
        passport = request.POST.get('passport')
        birthday = request.POST.get('birthday')
        type_trip = request.POST.get('type_trip')

        travelInsurance.objects.create(
            user=user,
            passport=passport,
            birthday=birthday,
            type_trip=type_trip
        )
        
        return redirect('/')
    data = {'user': [user]}    
    return render(request, 'forms/register_travel_insurance.html', context=data)


@csrf_exempt
def register_comment(request):
    """
    Handles the registration of a comment.
    If the request method is POST, it creates a new commentsAngency object and redirects to the home page.
    If the request method is GET, it renders the comment registration form.
    """
    user = request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        title = request.POST.get('title')
        comment = request.POST.get('comment')

        commentsAngency.objects.create(
            name=name,
            title=title,
            comment=comment,
        )
        
        return redirect('/')
    data = {'user': [user]}   
    return render(request, 'forms/register_comment.html', context=data)


@csrf_exempt
@login_required(login_url='/login/')
def view_info_travels(request):
    """
    Retrieves and displays the travel information for the logged-in user.
    """
    user = request.user
    
    travels = schedulingTravel.objects.filter(user=user)
    travel_insurance = travelInsurance.objects.filter(user=user)
    
    data = {'travels': travels, 'user':[user], 'travel_insurance': travel_insurance}

    return render(request, 'view_forms/view_travels.html', context=data)

