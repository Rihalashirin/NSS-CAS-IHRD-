from django.shortcuts import render
from vgallery.models import Vgallery
from volunteer.models import Volunteer
from event.models import Event
from django.core.files.storage import FileSystemStorage
from datetime import datetime as dtime
import datetime

# Create your views here.
def galv(request):
    ss=request.session["uid"]
    ovv = Volunteer.objects.get(volunteer_id=ss)
    obk=""
    now = dtime.now()
    date_time = now.strftime("%Y-%m-%d")
    obb1=Event.objects.all()
    if request.method == "POST":
        obj=Vgallery()
        obj.volunteer_id=ss
        obj.event_id=request.POST.get('evnt')
        obj.status="pending"
        obj.classes=request.POST.get('cs')
        obj.date=datetime.datetime.today()

        # obj.images=request.POST.get('img')
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        obj.images = myfile.name
        obj.images3=''
        obj.images2=''
        obj.videos=''

        try:

            myfile = request.FILES['gg']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            obj.images2 = myfile.name
        except:
            pass
        try:


            myfile = request.FILES['img3']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            obj.images3 = myfile.name
        except:
            pass
        try:

            # obj.videos=request.POST.get('vid')
            myfile = request.FILES['vid']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            obj.videos = myfile.name
        except:
                pass
        obj.save()
        obk="ok"
    context = {
        'x': obb1,
        'msg':obk,
        'dt': date_time,
        'p':ovv

    }
    return render(request,'vgallery/gallery_v.html',context)

def mnggal(request):
    obj=Vgallery.objects.all()
    context={
        'x':obj
    }
    return render(request,'vgallery/manage_gallery.html',context)

def vounteer(request):
    ss=request.session['uid']
    obj=Vgallery.objects.filter(status='Accepted',volunteer_id=ss)
    context={
        'x':obj
    }
    return render(request,'vgallery/volunteer_gallery_view.html',context)


def pr_view(request):
    # ss=request.session['uid']
    obj=Vgallery.objects.filter(status='Accepted')
    context={
        'x':obj
    }
    return render(request,'vgallery/princi_view.html',context)

def staff(request):
    obj=Vgallery.objects.filter(status='Accepted')
    context={
        'x':obj
    }
    return render(request,'vgallery/staff_vw_gallery.html',context)

def accept(request,idd):
    obj=Vgallery.objects.get(vgallery_id=idd)
    obj.status="Accepted"
    obj.save()
    return mnggal(request)
def reject(request,idd):
    obj=Vgallery.objects.get(vgallery_id=idd)
    obj.status="Rejected"
    obj.save()
    return mnggal(request)

