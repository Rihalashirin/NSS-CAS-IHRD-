from django.db.models import Q
from django.shortcuts import render
from staff.models import Staff
from login.models import Login

# Create your views here.
def mngstf(request):
    obj=Staff.objects.all()
    context={
        'x':obj
    }
    return render(request,'staff/manage_staff.html',context)

def staff(request):
    obk=""
    if request.method == "POST":
        a = request.POST.get('smail')
        b = request.POST.get('scno')
        # c = request.POST.get('swdate')
        obv = Staff.objects.filter(Q(email=a) | (Q(contact=b)))
        if len(obv) > 0:
            obk="user exist"
        else:

            obj=Staff()
            obj.name=request.POST.get('snm')
            obj.department=request.POST.get('sdpt')
            obj.email=request.POST.get('smail')
            obj.contact=request.POST.get('scno')
            obj.password=request.POST.get('spswd')
            obj.save()

            obb = Login()
            obb.username = obj.email
            obb.password = obj.password
            obb.type = "staff"
            obb.u_id = obj.staff_id
            obb.save()
            obk = "ok"

    context={
        'msg':obk
    }

    return render(request, 'staff/staff.html',context)



def updtstf(request,idd):
    obb=Staff.objects.get(staff_id=idd)
    context={
        'c':obb
    }
    if request.method == "POST":
        obj=Staff.objects.get(staff_id=idd)
        obj.name = request.POST.get('snm')
        obj.department = request.POST.get('sdpt')
        obj.email = request.POST.get('smail')
        obj.contact = request.POST.get('scno')
        obj.password = request.POST.get('spswd')
        obj.save()

        obb = Login.objects.get(u_id=request.session["uid"],type = "staff")
        obb.username = obj.email
        obb.password = obj.password
        obb.u_id = obj.staff_id
        obb.save()
        return mngstf(request)
    return render(request,'staff/updatestaff.html',context)


def vw_slf(request):
    ss=request.session['uid']
    obn=Staff.objects.filter(staff_id=ss)
    context={
        'd':obn
    }
    return render(request,'staff/vw_self.html',context)

def selfup(request,idd):
    obb=Staff.objects.get(staff_id=idd)
    context={
        'v':obb
    }
    if request.method == "POST":
        obj=Staff.objects.get(staff_id=idd)
        obj.name = request.POST.get('snm')
        obj.department = request.POST.get('sdpt')
        obj.email = request.POST.get('smail')
        obj.contact = request.POST.get('scno')
        obj.password = request.POST.get('spswd')
        obj.save()

        obb = Login.objects.get(u_id=request.session["uid"], type="staff")
        obb.username = obj.email
        obb.password = obj.password
        obb.u_id = obj.staff_id
        obb.save()
        obk = "ok"
        return vw_slf(request)
    return render(request,'staff/self.html',context)

def delete(request,idd):
    obj=Staff.objects.get(staff_id=idd)
    obj.delete()
    return mngstf(request)