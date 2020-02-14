from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.
from gallery.models import galleryUpload


@login_required(login_url='/login')
def show(request):
    if request.method=="POST":
        if request.POST.get('uploadData'):
            user=request.user
            img=request.FILES['file']
            captionn=request.POST['caption']
            date=datetime.now()
            fs=FileSystemStorage()
            fs.save(img.name,img)
            obj=galleryUpload(user=user,img=img.name,caption=captionn,date=date)
            obj.save()
        else:
            imgid=request.POST['id']
            updatepic=galleryUpload.objects.get(id=imgid)
            updatepic.caption=request.POST['caption']
            updatepic.img=request.FILES['file']
            updatepic.date=datetime.now()
            updatepic.save()
    posts=galleryUpload.objects.filter(user=request.user)
    return render(request,"gallery.html",{"Post":posts})

def delete(request, pid):
    obj=galleryUpload.objects.get(id=pid)
    obj.delete()
    return redirect('/gallery')
