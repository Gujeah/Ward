from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.views.generic import ListView, DetailView,CreateView
from .models import Patient,Hierachy,Analysis,Tracking
from django.contrib import messages

# Create your views here.
class PatientListView(ListView):
    model=Patient 
class PatientDetailView(DetailView):
    model=Patient
class AddPatientView(CreateView):
    model=Patient
    fields='_all_'

def base(request):
    baselist=Patient.object.all()
    return render(request, "base.html",{baselist:'baselist'})
def form(request):
    context={}
    return render(request,"form.html")
                                  
def register(request):
    if request.method=='POST':
        first_name=request.POST[first_name]
        last_name=request.POST[last_name]
        email=request.POST[email]
        password1=request.POST[password1]
        password2=request.POST[password2]

        user=User.objects.create_user(password=password1,email=email,first_name=first_name,last_name=last_name,)
        user.save();
        print("user created")
        return redirect('/')
    else:

        return render(request,'form.html')
  