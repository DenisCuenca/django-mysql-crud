from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import Agenda
from .form import CreateNewTask;
def registros(request):
    return render(request, "data.html", {
        "data": Agenda.objects.values()
    })

def form(request):
    
   if request.method == "GET":
      return render(request, "form.html",{
        "form": CreateNewTask()
        })
      
   else:
       Agenda.objects.create(nombre = request.POST["name"], description = request.POST["description"], fecha = request.POST["date"], tipo = request.POST["type_agend"])
       return redirect("/agenda")
       


def delete(request, id):
  registro = Agenda.objects.filter(id=id)
  
  
  registro.delete()
  return redirect("/agenda") 


def update(request, id):

  registro = Agenda.objects.filter(id=id)
  
  name = registro.values()[0]["nombre"]
  tipo = registro.values()[0]["tipo"]
  fecha = registro.values()[0]["fecha"]
  description = registro.values()[0]["description"]
  
  data = {
      "name": name,
      "type_agend": tipo,
      "date": fecha,
      "description": description 
  }

  return render(request, "update.html", {
      'form': CreateNewTask(data),
      "registro":  registro.values()[0]["id"]
    
    })     
  
  
def updaterecord(request, id):
    
    nombre = request.POST["name"]
    description = request.POST["description"]
    fecha = request.POST["date"]
    tipo = request.POST["type_agend"]
    registro = Agenda.objects.get(id = id)
    registro.nombre = nombre
    registro.description = description
    registro.fecha = fecha
    registro.tipo = tipo
    
    registro.save()
    
    return redirect("/agenda")    
        
    