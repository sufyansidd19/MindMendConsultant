from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def sessions(request):
    return render(request,'sessions.html')
def services(request):
    return render(request,'service.html')
def training(request):
    return render(request,'training.html')
def profile(request):
    return render(request,'userprofile.html')
def report_gen(request):
    return render(request,'gen_report.html')
def Booking(request):
    return render(request,'Book.html')