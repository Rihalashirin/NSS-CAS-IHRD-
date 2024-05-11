from django.shortcuts import render
from attendance.models import Attendance
from volunteer.models import Volunteer
from event.models import Event
from django.db.models import Count, Sum, Q
from datetime import datetime

# Create your views here.

def attendance(request,idd):
    ook=""
    obk=Event.objects.all()
    obc=Volunteer.objects.get(volunteer_id=idd)
    # context={
    #     'k':obk,
    #     'b':obc,
    # }
    if request.method == "POST":
        ook='post'
        a = request.POST.get('ne')
        # b = Attendance.objects.get(volunteer_id=idd)
        obv=Attendance.objects.filter(Q(event_id=a) | (Q(volunteer_id=idd)))
        if len(obv) > 0:
            ook="vv"
            # print('jj')
        else:
            obj=Attendance()
            obj.event_id=request.POST.get('evt')
            obj.volunteer_id=idd
            obj.attendance=request.POST.get('att')
            obj.performance=request.POST.get('pr')
            obj.date=request.POST.get('dt')
            obj.save()

            student = obj.volunteer_id
            print(student)
            total_attendance = Attendance.objects.filter(volunteer=student).count()
            events_attended = Event.objects.filter(attendance=student).annotate(attendance_count=Count('attendance'))
            print(events_attended)
            total_events = Event.objects.count()
            print(total_events)
            ook = "ok"
            if total_events > 0:
                attendance_percentage = (total_attendance / total_events) * 100
                print(attendance_percentage)
            else:
                attendance_percentage = 0
                print(attendance_percentage ,"0")

                pp = attendance_percentage
                obb = Volunteer.objects.get(volunteer_id=idd)
                obb.volunteer_attendance = "0"
                obb.save()

    context = {
        'k': obk,
        'b': obc,
        'msg':ook,
    }

    return render(request,'attendance/attendance.html',context)



def update_atte(request,idd):
    obb=Attendance.objects.get(attendance_id=idd)
    now = obb.date
    date_time = now.strftime("%Y-%m-%d")
    context={
        'c':obb,
        'dt': date_time,
    }
    if request.method=="POST":
        obj=Attendance.objects.get(attendance_id=idd)
        obj.event_id=1
        obj.volunteer_id=1
        obj.attendance=request.POST.get('mprsnt')
        obj.percentage=request.POST.get('per')
        obj.save()
        return vw_att_s(request)
    return render(request,'attendance/update_attendance.html',context)

# def delete(request,idd):
#     obj=Attendance.objects.get(attendance_id=idd)
#     obj.delete()
#     return vw_att_s(request)
def delete(request,idd):
    obj=Attendance.objects.get(attendance_id=idd)
    obj.delete()
    return vw_att_s(request)


def vw_att_s(request):
    obj=Attendance.objects.all()
    context={
        'x':obj
    }
    return render(request,'attendance/view_attendance_s.html',context)

def vw_att_v(request):
    ss=request.session["uid"]
    volunteers=Volunteer.objects.filter(volunteer_id=ss)
    for volunteer in volunteers:
        volunteer_id = volunteer.volunteer_id
        # print(student)
        total_attendance = Attendance.objects.filter(volunteer=volunteer_id,attendance="present").count()
        events_attended = Event.objects.filter(attendance__volunteer=volunteer_id).annotate(attendance_count=Count('attendance'))
        print(events_attended)
        total_events = Event.objects.count()
        print(total_events)
        if total_events > 0:
            attendance_percentage = (total_attendance / total_events) * 100
            print(attendance_percentage)
        else:
            attendance_percentage = 0
            print(attendance_percentage, "0")

        volunteer.volunteer_attendance = attendance_percentage
        volunteer.save()

    context = {
        'x': volunteers
    }
    return render(request, 'attendance/view_attpercentage_v.html', context)


def vw_a_s(request):
    # ss=request.session["uid"]
    volunteers=Volunteer.objects.all()
    for volunteer in volunteers:
        volunteer_id = volunteer.volunteer_id
        # print(student)
        total_attendance = Attendance.objects.filter(volunteer=volunteer_id,attendance="present").count()
        events_attended = Event.objects.filter(attendance__volunteer=volunteer_id).annotate(attendance_count=Count('attendance'))
        print(events_attended)
        total_events = Event.objects.count()
        print(total_events)
        if total_events > 0:
            attendance_percentage = (total_attendance / total_events) * 100
            print(attendance_percentage)
        else:
            attendance_percentage = 0
            print(attendance_percentage, "0")

        volunteer.volunteer_attendance = attendance_percentage
        volunteer.save()

    context = {
        'x': volunteers
    }
    return render(request, 'attendance/view_attendance_s.html', context)


def perf(request):
    # ss=request.session["uid"]
    volunteers = Volunteer.objects.all()
    max_volunteer = None  # Variable to store the volunteer with the maximum performance
    max_performance = 0
    for volunteer in volunteers:
        volunteer_id = volunteer.volunteer_id

        # Calculate the sum of performance for the volunteer
        total_performance = Attendance.objects.filter(volunteer=volunteer_id).aggregate(Sum('performance'))[
            'performance__sum']

        # Calculate the number of events attended by the volunteer
        events_attended = Event.objects.filter(attendance__volunteer=volunteer_id).annotate(
            attendance_count=Count('attendance'))
        print(events_attended)

        # Get the total number of events
        total_events = Event.objects.count()
        print(total_events)

        if total_events > 0:
            print(total_performance)
        else:
            total_performance = 0
            print(total_performance, "0")

        # Set the total_performance to volunteer.volunteer_attendance
        volunteer.performance = total_performance
        volunteer.save()

        if total_performance is not None and total_performance > max_performance:
            max_volunteer = volunteer
            max_performance = total_performance

    context = {
        'x': volunteers,
        'max_volunteer': max_volunteer  # Pass the volunteer with the highest performance to the template

    }

    return render(request,'attendance/view_performance.html',context)


def apo(request,idd):
    obj=Attendance.objects.get(attendance_id=idd)
    obj.save()
    return render(request,'points/points.html')



def abb(request):
    ss=request.session["uid"]
    obj=Attendance.objects.filter(volunteer_id=ss)
    context={
        'x':obj
    }
    return render(request,'attendance/view_attendnce_v.html',context)



def perf1(request):
    ss = request.session["uid"]
    volunteers = Volunteer.objects.filter(volunteer_id=ss)
    max_volunteer = None  # Variable to store the volunteer with the maximum performance
    max_performance = 0
    for volunteer in volunteers:
        volunteer_id = volunteer.volunteer_id

        # Calculate the sum of performance for the volunteer
        total_performance = Attendance.objects.filter(volunteer=volunteer_id).aggregate(Sum('performance'))[
            'performance__sum']

        # Calculate the number of events attended by the volunteer
        events_attended = Event.objects.filter(attendance__volunteer=volunteer_id).annotate(
            attendance_count=Count('attendance'))
        print(events_attended)

        # Get the total number of events
        total_events = Event.objects.count()
        print(total_events)

        if total_events > 0:
            print(total_performance)
        else:
            total_performance = 0
            print(total_performance, "0")

        # Set the total_performance to volunteer.volunteer_attendance
        volunteer.performance = total_performance
        volunteer.save()

        if total_performance is not None and total_performance > max_performance:
            max_volunteer = volunteer
            max_performance = total_performance

    context = {
        'x': volunteers,
        'max_volunteer': max_volunteer  # Pass the volunteer with the highest performance to the template

    }

    return render(request,'attendance/view_performance_v.html',context)