from django.conf.urls import url
from report import views

urlpatterns = [
    url('report/',views.report),
    url('vwreptp/',views.vwrptp),
    url('vwreptv/',views.vwrptv),
    url('vwrepts/',views.vwrpts),
    url('delete/(?P<idd>\w+)',views.delete)


]