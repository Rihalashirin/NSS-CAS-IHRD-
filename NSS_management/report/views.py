from django.db.models import Q
from django.shortcuts import render
from report.models import Report
from event.models import Event
from django.core.files.storage import FileSystemStorage
# Create your views here.
def report(request):
    obk=""
    obb=Event.objects.all()
    if request.method == "POST":
        obj=Report()
        obj.event_id=request.POST.get('evnt')
        # obj.report=request.POST.get('rfil')
        myfile=request.FILES['rfil']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.report =myfile.name
        obj.save()
        obk="ok"
    context = {
        'x': obb,
        'msg':obk
    }
    return render(request,'report/report.html',context)

def vwrptp(request):
    if request.method=="POST":
        pv=request.POST.get('ev')
        sv=request.POST.get('loc')
        try:
            ob=Report.objects.filter(Q(event__date=sv))
        except:
            ob = Report.objects.filter(Q(event__e_name__icontains=pv))
        context={
            'x':ob
        }
        return render(request,'report/view_report_p.html',context)
    else:
        obj=Report.objects.all()
        context={
           'x':obj
        }
        return render(request, 'report/view_report_p.html', context)
    return render(request,'report/view_report_p.html',context)

def vwrptv(request):
    obj=Report.objects.all()
    context={
        'x':obj
    }
    return render(request,'report/view_report_v.html',context)

def vwrpts(request):
    if request.method=="POST":
        pv=request.POST.get('search')
        # sv=request.POST.get('sea')
        ob=Report.objects.filter(event__e_name__icontains=pv)
        context={
            'x':ob
        }
        return render(request,'report/view_report_s.html',context)
    else:
        obj=Report.objects.all()
        context={
           'x':obj
        }
        return render(request, 'report/view_report_s.html', context)

    return render(request,'report/view_report_s.html',context)


def delete(request,idd):
    obj=Report.objects.get(report_id=idd)
    obj.delete()
    return render(request,'report/view_report_s.html')



