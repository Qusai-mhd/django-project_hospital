from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Appointment, Contact , CustomUser
from .forms import AppointmentForm , ContactForm , UserForm
# Create your views here.


def index(request):
    return render(request,'index.html')


def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_success')
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})


def appointment_success(request):
    return render(request, 'appointment_success.html')

def login_admin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            if user.user_type.user_type=='admin':
                login(request,user)
                return redirect('admin-dash')
        else:
            messages.error(request,"Invalid email or password")
            return render(request,'failure_message.html',{"messages": messages.get_messages(request)})
    return render(request,'login_admin.html')

def admin_dashboard(request):
    if not request.user.user_type.user_type=='admin':
        return HttpResponseForbidden()
    appointments=Appointment.objects.all()
    return render(request,'admin_dashboard.html',{"appointments":appointments})

def contact_messages(request):
    if not request.user.user_type.user_type=='admin':
        return HttpResponseForbidden()
    messages=Contact.objects.all()
    return render(request,'contact_messages.html',{'messages':messages})


def login_doctor(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            if user.user_type.user_type=='doctor':
                login(request,user)
                return redirect('doctor-dash')
        else:
            messages.error(request,"Invalid email or password")
            return render(request,'failure_message.html',{"messages": messages.get_messages(request)})
    return render(request,'login_doctor.html')

def doctor_dashboard(request):
    if not request.user.user_type.user_type=='doctor':
        return HttpResponseForbidden()
    appointments=Appointment.objects.all()
    return render(request,'doctor-dashboard.html',{"appointments":appointments})




def login_nurse(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            if user.user_type.user_type=='nurse':
                login(request,user)
                return redirect('nurse-dash')
        else:
            messages.error(request,"Invalid email or password")
            return render(request,'failure_message.html',{"messages": messages.get_messages(request)})
    return render(request,'login_nurse.html')

def nurse_dashboard(request):
    if not request.user.user_type.user_type=='nurse':
        return HttpResponseForbidden()
    appointments=Appointment.objects.all()
    return render(request,'nurse-dashboard.html',{"appointments":appointments})

def login_worker(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            if user.user_type.user_type=='worker':
                login(request,user)
                return redirect('worker-dash')
        else:
            messages.error(request,"Invalid email or password")
            return render(request,'failure_message.html',{"messages": messages.get_messages(request)})
    return render(request,'login_worker.html')

def worker_dashboard(request):
    if not request.user.user_type.user_type=='worker':
        return HttpResponseForbidden()
    appointments=Appointment.objects.all()
    return render(request,'worker-dashboard.html',{"appointments":appointments})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'contact_suucess.html')
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form':form})


def create_user(request):
    if not request.user.user_type.user_type=='admin':
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            user_type = form.cleaned_data['user_type']
            user = CustomUser.objects.create_user(email=email, password=password, name=name, user_type=user_type)
            return render(request,'user_created_success.html')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

def list_of_users(request):
    if not request.user.user_type.user_type=='admin':
        return HttpResponseForbidden()
    current_user = request.user
    users=CustomUser.objects.exclude(id=request.user.id)
    return render(request,'list_of_users.html',{"users":users})

def delete_user(request,pk):
    if not request.user.user_type.user_type=='admin':
        return HttpResponseForbidden()
    if request.method == 'POST':
        user=CustomUser.objects.get(id=pk)
        # render(request,'confirm_delete_user.html')
        user.delete()
        return render(request,'user_deleted_success.html',{"user":user})
    return render(request,'confirm_delete_user.html')

    
    


def logout_view(request):
    logout(request)
    return redirect('home')