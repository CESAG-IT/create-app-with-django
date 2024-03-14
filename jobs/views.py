from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request): 
    return HttpResponse("Bienvenue sur obonjob")

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