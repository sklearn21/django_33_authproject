from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignupForm
from django.http import HttpResponseRedirect


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

def sign_up_view(request):
    form = SignupForm()
    if request.method =='POST':
        form = SignupForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'testapp/signup.html', {'form':form})