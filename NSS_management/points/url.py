from django.conf.urls import url
from points import views

urlpatterns = [
    url('points/(?P<idd>\w+)/(?P<idd1>\w+)',views.points),
    url('pointsviewww/',views.vwpoints),
    url('svwpoint/',views.sviewpoint),
    url('updt/(?P<idd>\w+)',views.updtpoints),
    url('del/(?P<idd>\w+)',views.delete)


]