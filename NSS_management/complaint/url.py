from django.conf.urls import url
from complaint import views

urlpatterns = [
    url('comp/',views.comp),
    url('replay/(?P<idd>\w+)',views.rep),
    url('vw_com/',views.vwcmplt),
    url('vw_rep/',views.vwrply),


]