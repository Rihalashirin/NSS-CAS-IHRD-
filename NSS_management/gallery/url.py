from django.conf.urls import url
from gallery import views

urlpatterns = [
    url('sgal/',views.sgal),
    url('vwgalp/',views.vwgalp),
    url('vwgalv/',views.vwgalv),
    url('galupdts/(?P<idd>\w+)',views.galupdts),
    url('vwupdtgallry',views.vwupdtgallry),
    url('del/(?P<idd>\w+)',views.delete),
]