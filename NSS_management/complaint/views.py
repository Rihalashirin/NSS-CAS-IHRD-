from django.shortcuts import render
from complaint.models import Complaint
from volunteer.models import Volunteer
import datetime
# Create your views here.
def comp(request):
    ss=request.session["uid"]
    obk=""
    if request.method == "POST":
        obj=Complaint()
        obj.volunteer_id=ss
        obj.complaint=request.POST.get('cmpl')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.reply="Pending"
        obj.save()
        obk="kk"
    context={
        'msg':obk
    }
    return render(request,'complaint/complaint.html',context)

def rep(request,idd):
    if request.method=="POST":
        obj=Complaint.objects.get(complaint_id=idd)
        obj.reply=request.POST.get('rply')
        obj.save()
        return vwcmplt(request)
    return render(request,'complaint/reply.html')


def vwcmplt(request):
    obj=Complaint.objects.all()
    context={
        'x':obj
    }

    return render(request,'complaint/view_cmplt_and_reply.html',context)

def vwrply(request):
    ss=request.session['uid']
    obj=Complaint.objects.filter(volunteer_id=ss)
    context={
        'x':obj
    }
    return render(request,'complaint/view_reply_v.html',context)

