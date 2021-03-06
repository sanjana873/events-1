from django.urls import path
from . import views
urlpatterns=[
    path('',views.homepage,name='home'),
    path('adminlogin/',views.adminlogin,name='admin'),
    path('clublogin/',views.clublogin,name='clublog'),
    path('clubsignup/',views.clubsignup,name='clubsign'),
    path('mainadmin/',views.mainadmin,name='adminmain'),
    path('after_registration/',views.after_registration,name='after_reg'),
    path('after_clublogin/',views.after_clublogin,name='after_clublogin'),
    path('create_event/',views.create_event,name='create_event'),
    path('after_createevent/',views.after_createevent,name='created_event'),
    path('pending_requests/',views.pending_requests,name='pending_requests'),
    path('acceptdeny/',views.acceptdeny,name='acceptdeny'),
    path('show_events/',views.show_events,name='show_events'),
    path('deleteevent/',views.deleteevent,name='deleteevent'),
    path('show_clubs/',views.show_clubs,name='show_clubs'),
    path('clubhome/',views.clubhome,name='clubhome'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('admindeleteeventanduser/',views.admindeleteeventanduser,name='admindeleteeventanduser'),
    path('getevents/',views.getallevents,name='getevents'),
    path('getusers/',views.getusers,name='getusers'),
    path('getstudentsregistered/',views.getstudentsregistered,name='getstudentsregistered'),
    path('resetpassword/',views.resetpassword,name='resetpassword'),
    path('resetconf/',views.resetconf,name="resetconf"),
    path('reset/',views.reset,name="reset"),
    path('enterclubnamereset/',views.enterclubnamereset,name='enterclubnamereset'),
    path('profile/',views.profile,name="profile"),
    path('changeform/',views.changeform,name="changeform"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('getstarted/',views.getstarted,name='getstarted'),
]