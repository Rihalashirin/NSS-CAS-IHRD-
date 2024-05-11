from django.shortcuts import render
from points.models import Points
from volunteer.models import Volunteer
from attendance.models import Attendance

# Create your views here.
def points(request,idd,idd1):
    obk=""
    obb=Attendance.objects.get(attendance_id=idd)

    if request.method == "POST":
        obj=Points()
        obj.volunteer_id=idd1
        obj.attendance_id=idd
        obj.percentage=request.POST.get('per')
        obj.points=request.POST.get('point')
        obj.save()
    context = {
        'g': obb
    }
    return render(request,'points/points.html',context)

def vwpoints(request):
    volunteers = Volunteer.objects.all()

    for volunteer in volunteers:
        vv = volunteer.volunteer_attendance
        vv = float(vv)  # Convert to float
        volunteer.points = (vv / 100) * 20
        print(volunteer.points)
        volunteer.save()

        f=volunteer.volunteer_id
        obv = Points.objects.filter(volunteer_id=f)
        if len(obv) > 0:
            print('jj')
        else:
            obj=Points()
            obj.points=volunteer.points
            obj.volunteer_id=volunteer.volunteer_id
            # obj.attendance=Attendanc
            obj.save()

    context = {
        'x': volunteers
    }
    return render(request, 'points/view_points.html', context)


def sviewpoint(request):
    obj=Points.objects.all()
    context={
        'x':obj
    }
    return render(request,'points/view_points_s.html',context)

def updtpoints(request,idd):
    obb=Points.objects.get(points_id=idd)
    context={
        'c':obb
    }
    if request.method == "POST":
        obj = Points.objects.get(points_id=idd)
        obj.volunteer_id = 1
        obj.attendance_id = 1
        # obj.percentage = request.POST.get('per')
        obj.points = request.POST.get('point')
        obj.save()
        return sviewpoint(request)
    return render(request,'points/update_points.html',context)


def delete(request,idd):
    obj=Points.objects.get(points_id=idd)
    obj.delete()
    return sviewpoint(request)