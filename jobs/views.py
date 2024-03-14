from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from jobs.models import Job
import json

# Create your views here.

def home(request): 
    job_list = Job.objects.all().values()

    context = {
        "jobs": job_list
    }
    return render(request,"index.html", context)

def job_list(request):
    return HttpResponse("La liste des emplois disponibles")

def create_job(request):
    return HttpResponse("Ajout d'un nouvel emploi")

def show_job(request, pk):
    return HttpResponse(f"détails sur l'emplois ID n° {pk}")

def update_job(request, pk):
    return HttpResponse(f"Modification de l'emplois ID N° {pk}")

def delete_job(request, pk):
    return HttpResponse(f"Suppression de l'emplois ID N° {pk}")