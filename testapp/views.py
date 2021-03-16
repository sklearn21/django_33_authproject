from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def home_page_view(request):
    return render(request, 'testapp/home.html')


@login_required
def java_exams_view(request):
    return render(request, 'testapp/javaexams.html')

@login_required
def python_exams_view(request):
    return render(request, 'testapp/pythonexam.html')

@login_required
def aptitude_exams_view(request):
    return render(request, 'testapp/aptitudeexam.html')

def logout_view(request):
    return render(request, 'testapp/logout.html')