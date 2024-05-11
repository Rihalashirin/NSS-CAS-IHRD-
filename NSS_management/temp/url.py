from django.conf.urls import url
from temp import views
urlpatterns=[
    url('home/',views.home),
    url('principal/',views.principal),
    url('staff/',views.staff),
    url('volunteer/',views.volunteer),
    url('aaa/',views.main_home),
    url('bbb/',views.main_principal),
    url('ccc/',views.main_staff),
    url('ddd/',views.main_volunteer)
]