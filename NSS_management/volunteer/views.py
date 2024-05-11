from django.db.models import Q
from django.shortcuts import render
from volunteer.models import Volunteer
from login.models import Login
# Create your views here.
def mngv(request):
    obj=Volunteer.objects.all()
    context={
        'x':obj
        
    }
    return render(request,'volunteer/manage_volunteer.html',context)

def accept(request,idd):
    obj=Volunteer.objects.get(volunteer_id=idd)
    obj.status="Accepted"
    obj.save()
    obb = Login()
    obb.username = obj.regno
    obb.password = obj.password
    obb.type = "volunteer"
    obb.u_id = obj.volunteer_id
    obb.save()
    return mngv(request)

def reject(request,idd):
    obj=Volunteer.objects.get(volunteer_id=idd)
    obj.status="rejected"
    obj.save()
    return mngv(request)



def updtv(request,idd):
    obb=Volunteer.objects.get(volunteer_id=idd)
    context={
        'c':obb
    }
    if request.method == "POST":
        obj=Volunteer.objects.get(volunteer_id=idd)
        obj.name=request.POST.get('vnm')
        obj.department=request.POST.get('vdpt')
        obj.regno=request.POST.get('vreg')
        obj.gender=request.POST.get('fml')
        obj.year=request.POST.get('vyr')
        obj.age=request.POST.get('vage')
        obj.password=request.POST.get('vpswd')
        obj.save()

        obb = Login(u_id = request.session["uid"], type = "staff")
        obb.username = obj.regno
        obb.password = obj.password
        obb.type = "volunteer"
        obb.u_id = obj.volunteer_id
        obb.save()

        return vwupdtv(request)
    return render(request,'volunteer/update_v.html',context)

def vwupdtv(request):
    ss= request.session["uid"]
    obj=Volunteer.objects.filter(volunteer_id=ss)
    context={
        'x':obj
    }

    return render(request,'volunteer/view_and_update_v.html', context)

def vltr(request):
    obk=""
    if request.method == "POST":
        a = request.POST.get('vreg')
        obv = Volunteer.objects.filter(Q(regno=a))
        if len(obv) > 0:
            obk="user"
            print('jj')
        else:
            obj=Volunteer()
            obj.name=request.POST.get('vnm')
            obj.department=request.POST.get('vdpt')
            obj.regno=request.POST.get('vreg')
            obj.gender=request.POST.get('fml')
            obj.year=request.POST.get('vyr')
            obj.age=request.POST.get('vage')
            obj.password=request.POST.get('vpswd')
            obj.attendance=0
            obj.status="Pending"
            obj.save()

            obk="ok"
    context={
        'msg':obk
    }

    return render(request, 'volunteer/volunteer.html',context)


def view_app_vol(request):
    if request.method=='POST':
        vv=request.POST.get('search')
        # sv=request.POST.get('sea')
        obj=Volunteer.objects.filter(Q(name__icontains=vv) | Q(regno__icontains=vv))
        context={
            'x':obj
        }
        return render(request,'volunteer/view_app_volunteer.html',context)
    else:
        obj=Volunteer.objects.filter(status='Accepted')
        context={
            'x':obj
        }
    return render(request,'volunteer/view_app_volunteer.html', context)

def vwandaddatt(request):
    # if request.method == 'POST':
    #     vv = request.POST.get('search')
    #     obv = Volunteer.objects.filter(name__icontains=vv)
    #     context = {
    #         'x': obv
    #     }
    #     return render(request, 'volunteer/vwandaddatt.html', context)
    # else:
    obv=Volunteer.objects.all()
    context={
         'c':obv
    }

    return render(request,'volunteer/vwandaddatt.html', context)
