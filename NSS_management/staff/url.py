from django.conf.urls import url
from staff import views

urlpatterns = [
    url('mngstff/',views.mngstf),
    url('staff/',views.staff),
    url('upstff/(?P<idd>\w+)',views.updtstf),
    url('dddd/(?P<idd>\w+)',views.delete),
    url('self/(?P<idd>\w+)',views.selfup),
    url('ss/',views.vw_slf)

]