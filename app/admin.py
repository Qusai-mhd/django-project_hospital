from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.CustomUser)
admin.site.register(models.Appointment)
admin.site.register(models.Patient)
admin.site.register(models.UserType)
admin.site.register(models.Contact)


