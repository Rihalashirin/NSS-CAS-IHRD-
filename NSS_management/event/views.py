from django.shortcuts import render
from event.models import Event
from datetime import datetime
# import datetime
# Create your views here.

# now = datetime.now()
# date_time = now.strftime("%Y-%m-%d")
# context={
#     'dt':date_time,
# }

def evt(request):
    obk=""
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d")
    # context = {
    #     'dt': date_time
    # }
    if request.method == "POST":
        a = request.POST.get('nevt')
        b = request.POST.get('ne')
        c = request.POST.get('swdate')

        obv = Event.objects.filter(e_name=a, e_nature=b, date=c)
        if len(obv) > 0:
            print('jj')
        else:

            obj=Event()
            obj.e_name=request.POST.get('nevt')
            obj.e_nature=request.POST.get('ne')
            obj.venue=request.POST.get('swven')
            obj.date=request.POST.get('swdate')
            obj.time=request.POST.get('swtim')
            obj.save()
            obk = "ok"
    context = {
        # 'x': obb,
        'msg': obk,
        'dt': date_time
    }

    return render(request,'event/event.html',context)

def mngevt(request):
    obj=Event.objects.all()
    context={
        'x':obj
    }
    return render(request,'event/manage_event.html',context)

def updevent(request,idd):
    obb=Event.objects.get(event_id=idd)
    now = obb.date
    to=obb.time
    time = to.strftime("%H:%M:%S")
    date_time = now.strftime("%Y-%m-%d")
    context={
        'c':obb,
        'dt':date_time,
        'tt':time,
    }
    if request.method == "POST":
        obj=Event.objects.get(event_id=idd)
        obj.e_name=request.POST.get('swrk')
        obj.e_nature=request.POST.get('ne')
        obj.venue=request.POST.get('swven')
        obj.date=request.POST.get('swdate')
        obj.time=request.POST.get('swtim')
        obj.save()
        return mngevt(request)
    return render(request,'event/update _event.html',context)

def delete(request,idd):
    obj=Event.objects.get(event_id=idd)
    obj.delete()
    return mngevt(request)

def vwevtp(request):
    obj=Event.objects.all()
    context={
        'x':obj
    }
    return render(request,'event/view_event_p.html',context)

def vwevtv(request):
    obj=Event.objects.all()
    context={
        'x':obj
    }
    return render(request,'event/view_event_v.html',context)
