from django.conf.urls import url
from attendance import views

urlpatterns = [
    url('attendance/(?P<idd>\w+)',views.attendance,),
    url('update_att/(?P<idd>\w+)',views.update_atte),
    url('vw_att_s/',views.vw_att_s),
    url('vw_att_v/',views.vw_att_v),
    url('dellll/(?P<idd>\w+)',views.delete),
    url('per/',views.perf),
    url('view_abb/',views.abb),
    url('pp/', views.perf1),
    url('rih/',views.vw_a_s)

]