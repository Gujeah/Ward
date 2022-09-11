from django.contrib import admin
#from patients.models import User
from patients.models import Doctor, Tracking,Patient,Hierachy, Analysis

# Register your models here.
#admin.site.unregister(User) 
admin.site.register(Doctor) 
admin.site.register(Patient)
admin.site.register(Hierachy)
admin.site.register(Analysis)   
admin.site.register(Tracking)
