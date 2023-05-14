from django import forms
from django.forms import DateInput, TimeInput
from .models import Patient, Appointment, Contact , UserType

class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone = forms.CharField(max_length=10)
    date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    time = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'timepicker'}))
    department = forms.ChoiceField(choices=Appointment.DEPARTMENT_CHOICES)


    def save(self):
        patient, created = Patient.objects.get_or_create(
            phone=self.cleaned_data['phone'],
            defaults={
                'name': self.cleaned_data['name'],
                'email': self.cleaned_data['email'],
            }
        )

        appointment = Appointment.objects.create(
            patient=patient,
            date=self.cleaned_data['date'],
            time=self.cleaned_data['time'],
            department=self.cleaned_data['department']
        )
        return appointment
    

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30,required=True)
    email = forms.EmailField(required=True)
    message=forms.CharField(widget=forms.Textarea, required=True)

    def save(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        contact = Contact(name=name, email=email, message=message)
        contact.save()



class UserForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=30)
    user_type = forms.ModelChoiceField(queryset=UserType.objects.all(),empty_label=None, label="User Type")

