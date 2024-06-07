from django.shortcuts import render
import requests


def inicio(request):
    return render(request, 'inicio.html')

def museos(request):
    url = "https://www.cultura.gob.ar/api/v2.0/museos"
    response = requests.get(url)
    datos_museos = response.json()  
    museos = datos_museos['results']  
    return render(request, 'museos.html', {'museos': museos})

def tramites(request):
    url = "https://www.cultura.gob.ar/api/v2.0/tramites" 
    response = requests.get(url)
    datos_tramites = response.json() 
    tramites = datos_tramites['results'] 
    return render(request, 'tramites.html', {'tramites': tramites})

def institutos(request):
    url = "https://www.cultura.gob.ar/api/v2.0/institutos" 
    response = requests.get(url)
    datos_institutos = response.json() 
    institutos = datos_institutos['results'] 
    return render(request, 'institutos.html', {'institutos': institutos})
