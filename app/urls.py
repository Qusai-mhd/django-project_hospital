from django.urls import path
from .views import index , contact ,book_appointment , login_doctor , login_nurse ,login_worker , logout_view \
    ,doctor_dashboard , nurse_dashboard , worker_dashboard, contact_messages , admin_dashboard , login_admin \
    ,create_user,list_of_users, delete_user

urlpatterns = [
    path('',index,name='home'),
    path('appointment',book_appointment,name='appointments'),
    path('contact',contact,name='contact'),
    path('login',login_admin,name='login-admin'),
    path('doctor/login',login_doctor,name='login-doctor'),
    path('nurse/login',login_nurse,name='login-nurse'),
    path('worker/login',login_worker,name='login-worker'),
    path('logout',logout_view,name='logout'),
    path('appointment/success',logout_view,name='app_success'),
    path('adminusser',admin_dashboard,name='admin-dash'),
    path('createuser',create_user,name='create-user'),
    path('users',list_of_users,name='list-users'),
    path(r'deleteuser/<int:pk>',delete_user,name='delete-user'),
    path('doctor',doctor_dashboard,name='doctor-dash'),
    path('nurse',nurse_dashboard,name='nurse-dash'),
    path('worker',worker_dashboard,name='worker-dash'),
    path('doctor/messages',contact_messages,name='patient-messages'),

]
