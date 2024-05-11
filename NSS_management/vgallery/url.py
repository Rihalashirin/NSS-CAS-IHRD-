from django.conf.urls import url
from vgallery import views

urlpatterns = [
    url('galv/',views.galv),
    url('mnggal/',views.mnggal),
    url('accept/(?P<idd>\w+)',views.accept),
    url('reject/(?P<idd>\w+)',views.reject),
    url('aaaa/',views.vounteer),
    url('volunteer/',views.vounteer),
    url('staff/',views.staff),
    url('princi/', views.pr_view)

]