from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'temp/home.html')

def principal(request):
    return render(request,'temp/principal.html')

def staff(request):
    return render(request,'temp/staff.html')

def volunteer(request):
    return render(request,'temp/volunteer.html')


def main_home(request):
    return render(request,'temp/main_home.html')

def main_principal(request):
    return render(request,'temp/main_principal.html')

def main_staff(request):
    return render(request,'temp/main_staff.html')

def main_volunteer(request):
    return render(request,'temp/main_volunteer.html')