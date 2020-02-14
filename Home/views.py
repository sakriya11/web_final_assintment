from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from Home.models import slider, service, photoupload, news


@login_required(login_url='/login')
def show(request):
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['Email']
        telephone = request.POST['Telephone']
        subject = request.POST['Subject']
        message = request.POST['Message']
        newsletter = news(Name=name, Email=email, Telephone=telephone,
                                        Subject=subject, Message=message)
        newsletter.save()

    carousel = slider.objects.all()
    apple = service.objects.all()
    pic=photoupload.objects.all()
    return render(request, "index.html", {'carousel': carousel, 'apple': apple,'UserPic':pic})


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                        password=password1, email=email)
        user.save()
        return redirect('/login')

    else:

        return render(request, "register.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/user")
        else:
            return HttpResponse("error")
    else:
        return render(request, 'login.html')
    # return HttpResponse("ok")

@login_required
def user(request):
    return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('/login')
