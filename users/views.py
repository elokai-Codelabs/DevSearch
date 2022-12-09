from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomUserCreationForm
from .models import Profile
from projects.models import Project

# Create your views here.
def loginUser(request):
    page = 'login'
    # prevent already loged in users from seing login page
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            # check if user exist
            user = User.objects.get(username=username)

        except:
            messages.error(request,'User not found')
        # confirm user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,'User succesfully logged in')
            return redirect('profiles')
        else:
            messages.error(request,' User or password is incorrect')
    context = {'page':page}
    return render(request,'users/login_register.html', context)   


def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    page = 'register'

    form = CustomUserCreationForm()
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,'User account was created')
            login(request, user)
            return redirect('profiles')

        else :
            messages.success(request,'An error occured during registration')

        
    context = {'page':page, 'form':form}
    return render(request,'users/login_register.html', context)   

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profile.html', context)

def userProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact='')
    otherSkills = profile.skill_set.filter(description='')
    context = {'profile': profile,'topSkills':topSkills,'otherSkills':otherSkills}
    return render(request, 'users/user-profile.html', context)

# obtaining all the skillset from profile

def userAccount(request):
    # profile = Project.objects.all()
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    print('This is a ',skills)

    context = {'profile': profile,'skills':skills,'projects':projects}
    return render(request, 'users/account.html', context)

