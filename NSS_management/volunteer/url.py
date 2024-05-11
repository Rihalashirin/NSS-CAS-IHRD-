from django.conf.urls import url
from volunteer import views


urlpatterns=[
    url('mngv/',views.mngv),
    url('accept/(?P<idd>\w+)',views.accept),
    url('reject/(?P<idd>\w+)',views.reject),
    url('updtv/(?P<idd>\w+)',views.updtv),
    url('viewu/',views.vwupdtv),
    url('vltr/',views.vltr),
    url('vw_approved/',views.view_app_vol),
    url('vatt/',views.vwandaddatt),

]