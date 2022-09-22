from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from .models import Student
from .forms import StudentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# Create your views here.
'''
BOILERPLATE FUNCTION
def home(r):
    context = {}
    return render(r, 'home.html', context)


    '''
def loginUser(r):
    page = 'login'
    if r.method == "POST":
        username = r.POST.get('sign-username')
        password = r.POST.get('sign-password')
        
        try:
            user = User.objects.get(username=username)
        
        except:
            return HttpResponse("INVALID USERNAME")

        user = authenticate(r, username=username, password=password)

        if user is not None:
            login(r, user)
            return redirect('home')


    return render(r, 'login_register.html')

@login_required(login_url='login')
def logoutUser(r):
    logout(r)
    return redirect('home')



def home(r):
    q = r.GET.get('q') if r.GET.get('q') != None else ''
    students = Student.objects.filter(

        Q(name__icontains=q) |
        Q(score__icontains=q) |
        Q(grade__icontains=q) |
        Q(manager__username__icontains=q) |
        Q(section__icontains=q) 

    ).order_by("name")

    context = {'students': students}
    return render(r, 'home.html', context)

@login_required(login_url='login')
def create_student(r):

    if r.method == "POST":
        form = StudentForm(r.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.manager = r.user
            student.save()
            return redirect("home")

    form = StudentForm()
    context = {'form': form}
    return render(r, 'studentform.html', context)


@login_required(login_url='login')
def delete_student(r, pk):
    student = Student.objects.get(id=pk)
    if r.method == "POST":
        student = Student.objects.filter(id=pk)
        student.delete()
        return redirect("home")
    context = {"obj": student}
    return render(r, 'deleteobj.html', context)


@login_required(login_url='login')
def update_student(r, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(r.POST or None, instance=student)
    
    if form.is_valid():
        student = form.save(commit=False)
        student.manager = r.user
        student.save()
        return redirect("home")

    context = {'form': form}
    return render(r, 'studentform.html', context)