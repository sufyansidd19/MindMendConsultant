# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')


def sessions(request):
    return render(request, 'sessions.html')


def services(request):
    return render(request, 'service.html')


def training(request):
    return render(request, 'training.html')


def profile(request):
    return render(request, 'userprofile.html')


def report_gen(request):
    return render(request, 'gen_report.html')


def Booking(request):
    return render(request, 'Book.html')

def auth(request):
    return render(request,"auth.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('/sessions')  # Replace 'home' with the URL name of your home page
        else:
            messages.error(request, 'Invalid login credentials.')

    return redirect('/')  # Redirect to the home page if not a POST request or if login fails
