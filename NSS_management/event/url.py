from django.conf.urls import url
from event import views

urlpatterns = [
    url('evt/',views.evt),
    url('manage/',views.mngevt),
    url('delete/(?P<idd>\w+)',views.delete),
    url('evntupdtt/(?P<idd>\w+)',views.updevent),
    url('vwevtp/',views.vwevtp),
    url('vwevtv/',views.vwevtv),

]