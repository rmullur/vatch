from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Video,UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm,NewItem
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User

def homepage(request):
    video = Video.objects.all()
    return render(request = request,
                   template_name='smain_2/home.html',context={"videos":video})

def init_video(user):
    video = Video(username=user,stream_key=user.profile.user_streamkey)
    video.save()

def init_profile(user):
    profile = UserProfile(username=user)
    profile.save()


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
           user = form.save()
           username = form.cleaned_data.get('username')
           #user.profile.user_streamkey = 'Lorem1'
           user.save()
           messages.success(request,f"New account created:{username}")
           login(request,user)
           init_video(user)
           init_profile(user)
           return redirect("smain_2:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            return render(request = request,
                          template_name='smain_2/register.html',
                          context={"form":form})
    form = NewUserForm
    return render(request = request,
                  template_name='smain_2/register.html',
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request,"Logged out succesfully")
    return redirect("smain_2:homepage")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                Video.username = username
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        #else:
        #    messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request = request,
                   template_name='smain_2/login.html',
                   context={"form":form})
def help_request(request):
    return render(request = request,
                       template_name='smain_2/help.html')

def account_request(request,username):
    user = User.objects.get(username=username)
    profile = UserProfile.objects.get(username=user)
    return render(request = request,
                       template_name='smain_2/account.html',context={"profile":profile})

def post(request,stream_key):
      video   = get_object_or_404(Video,stream_key=stream_key)
      video.views += 1
      video.save()
      return render(request = request,
                       template_name='smain_2/video.html',context={"video":video})

def watch_video(request,stream_key):
      video   = get_object_or_404(Video,stream_key=stream_key)
      video.views += 1
      video.save()
      return render(request = request,
                       template_name='smain_2/watch_video.html',context={"video":video})

def stream(request,username):
    user = User.objects.get(username=username)
    video = Video.objects.get(stream_key=user.profile.user_streamkey)
    return render(request = request,
                       template_name='smain_2/video.html',
                           context={"video":video})
