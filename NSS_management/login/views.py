from django.http import HttpResponseRedirect
from django.shortcuts import render
from login.models import Login

# Create your views here.
def login(request):
    if request.method == "POST":
        eml = request.POST.get("unm")
        passw = request.POST.get("psw")
        obj = Login.objects.filter(username=eml,password=passw)
        print(len(obj))
        tp = ""
        for ob in obj:
            tp = ob.type
            uid = ob.u_id
            if tp == "principal":
                request.session["uid"]=uid
                return HttpResponseRedirect('/temp/principal/')
            elif tp == "staff":
                request.session["uid"]=uid
                return HttpResponseRedirect('/temp/staff/')
            elif tp == "volunteer":
                request.session["uid"]=uid
                return HttpResponseRedirect('/temp/volunteer/')
        objlist = "email or password incorrect.....please try again....!"
        context = {
            'msg':objlist,
        }
        return render(request,'login/login.html',context)

    return render(request,'login/login.html')

