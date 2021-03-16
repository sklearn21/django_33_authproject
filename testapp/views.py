from django.shortcuts import render

# Create your views here.


def home_page_view(request):
    return render(request, 'testapp/home.html')


def java_exams_view(request):
    return render(request, 'testapp/javaexams.html')


def python_exams_view(request):
    return render(request, 'testapp/pythonexam.html')


def aptitude_exams_view(request):
    return render(request, 'testapp/aptitudeexam.html')