from django.urls import path
from . import views
from .views import AddPatientView,PatientDetailView, PatientListView
from django.views.generic import TemplateView
urlpatterns=[ 
    path("",PatientListView.as_view(),name="patient_list"),
    path("add_patient", AddPatientView.as_view(),name="add-patient"),
    path("<int:pk/", PatientDetailView.as_view(),name="people-detail"),
    path("dash", views.base,name="base.html"),
    


    
]  