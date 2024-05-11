from django.shortcuts import render
from gallery.models import Gallery
from event.models import Event
from django.core.files.storage import FileSystemStorage
from datetime import datetime
# Create your views here.
def sgal(request):
    obk=""
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d")
    obb=Event.objects.all()
    if request.method == "POST":
        obj=Gallery()
        obj.event_id=request.POST.get('evnt')
        # obj.images=request.POST.get('img')
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.images= myfile.name
        obj.images3=''
        obj.images2=''

        try:

            myfile = request.FILES['img2']
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
        'x': obb,
        'msg':obk,
        'dt':date_time
    }
    return render(request,'gallery/gallery_s.html',context)

def vwgalp(request):
    obj=Gallery.objects.all()
    context={
        'x':obj
    }
    return render(request,'gallery/view_gallery_p.html',context)

def vwgalv(request):
    obj=Gallery.objects.all()
    context={
        'x':obj
    }
    return render(request,'gallery/view_gallery_v.html',context)

def galupdts(request,idd):
    obk=Event.objects.all()
    obb=Gallery.objects.get(gallery_id=idd)

    if request.method=="POST":
        obj=Gallery.objects.get(gallery_id=idd)
        obj.event_id=request.POST.get('evnt')
        # obj.images = request.POST.get('img')
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.images = myfile.name
        obj.images3=''
        obj.images2=''
        obj.videos=''

        try:

             myfile = request.FILES['img2']
             fs = FileSystemStorage()
             filename = fs.save(myfile.name, myfile)
             obj.images2 = myfile.name

             myfile = request.FILES['img3']
             fs = FileSystemStorage()
             filename = fs.save(myfile.name, myfile)
             obj.images3 = myfile.name

             # obj.videos = request.POST.get('vid')
             myfile = request.FILES['vid']
             fs = FileSystemStorage()
             filename = fs.save(myfile.name, myfile)
             obj.videos = myfile.name

        except:
                pass
        obj.save()
        obk="ok"
    context = {
        'c': obb,
        'u': obk
    }
     # return vwupdtgallry(request)
    return render(request,'gallery/updt_gallry_s.html',context)

def vwupdtgallry(request):
    obj=Gallery.objects.all()
    context={
        'j':obj
    }
    return render(request,'gallery/vw_updt_gllry.html',context)

def delete(request,idd):
    obj=Gallery.objects.get(gallery_id=idd)
    obj.delete()
    return vwupdtgallry(request)