from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request, 'school-index.html')

def About(request):
    return render(request, 'school-about.html')

def Acting(request):
    return render(request, 'school-acting.html')

def Acting_Course(request):
    return render(request, 'school-acting_course.html')

def Application_Form(request):
    return render(request, 'school-application_form.html')

def Arts(request):
    return render(request, 'school-arts.html')

def Contact(request):
    return render(request, 'school-contact.html')

def Dance(request):
    return render(request, 'school-dance.html')

def Dance_Course(request):
    return render(request, 'school-dance_course.html')

def Finearts(request):
    return render(request, 'school-finearts.html')

def Login(request):
    return render(request, 'school-Login.html')

def Login_Index(request):
    return render(request, 'school-login-index.html')

def Music(request):
    return render(request, 'school-music.html')

def Music_Course(request):
    return render(request, 'school-music_course.html')

def Singup(request):
    return render(request, 'school-Signup.html')

def Team(request):
    return render(request, 'school-teamsipa.html')

