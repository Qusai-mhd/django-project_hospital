from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin , Permission , Group


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class UserType(models.Model):
    DOCTOR = 'doctor'
    NURSE = 'nurse'
    WORKER = 'worker'
    ADMIN = 'admin'

    USER_TYPE_CHOICES = [
        (DOCTOR, 'Doctor'),
        (NURSE, 'Nurse'),
        (WORKER, 'Worker'),
        (ADMIN, 'Admin'),
    ]
    user_type = models.CharField(choices=USER_TYPE_CHOICES,max_length=30,default=WORKER)

    def __str__(self):
        return self.user_type


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'user_type']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# Create your models here.

class Patient(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    Dentistry ='Dentistry'
    ENT='Ear, nose and throat (ENT)'
    General_surgery='General surgery'
    Internal_medicine='Internal Medicine'
    Ophthalmology ='Ophthalmology'
    Orthopedics='Orthopedics'
    Neurology='Neurology'
    General_practitioner='General Practitioner'
    
    DEPARTMENT_CHOICES=[
        (Dentistry,'Dentistry'),
        (ENT,'Ear, nose and throat (ENT)'),
        (General_surgery,'General surgery'),
        (Internal_medicine,'Internal Medicine'),
        (Ophthalmology,'Ophthalmology'),
        (Orthopedics,'Orthopedics'),
        (Neurology,'Neurology'),
        (General_practitioner,'General Practitioner')
    ]

    patient=models.ForeignKey(Patient,on_delete=models.PROTECT, blank=False, null=False)
    date=models.DateField(blank=False, null=False)
    time=models.TimeField(blank=False, null=False)
    department=models.CharField(choices=DEPARTMENT_CHOICES,max_length=30,default=General_practitioner)

    def __str__(self):
        return f'{self.patient.name} in  {self.date}'
    
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    message=models.TextField()

    def __str__(self):
        return self.name


