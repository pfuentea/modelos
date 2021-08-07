from django.shortcuts import render, HttpResponse
from .models import Wizard

def index(request):
    context = {
        'saludo': 'Hola'
    }
    return render(request, 'index.html', context)


def second(request, name):
    return HttpResponse('Hola ' + name)

def wizards(request):
    magos=Wizard.objects.all()
    context={
        'wizards':magos,
        'mensaje':''
    }
    return render(request, 'wizards.html', context)

def wizardsnew(request):
    v_nombre=request.POST['nombre']
    v_casa=request.POST['casa']
    v_mascota=request.POST['mascota']
    v_year=request.POST['year']
    Wizard.objects.create(name=v_nombre, house=v_casa,pet=v_mascota,year=v_year)
    magos=Wizard.objects.all()
    context={
        'wizards':magos,
        'mensaje':'Usuario nuevo creado'
    }
    return render(request, 'wizards.html', context)

def wizardsedit(request,p_id):
    if request.method == "GET":
        target=Wizard.objects.get(id=p_id)
        context={
            'target':target        
        }
        return render(request, 'wizards_edit.html', context)
    if request.method == "POST":
        target=Wizard.objects.get(id=p_id)
        target.name=request.POST['nombre']
        target.house=request.POST['casa']
        target.pet=request.POST['mascota']
        target.year=request.POST['year']
        target.save()
        magos=Wizard.objects.all()
        context={
            'wizards':magos,
            'mensaje':'Wizard editado'
        }
        return render(request, 'wizards.html', context)
    
def wizardsdelete(request,p_id):
    if request.method == "GET":
        target=Wizard.objects.get(id=p_id)
        target.delete()
        magos=Wizard.objects.all()
        context={
            'wizards':magos,
            'mensaje':'Wizard eliminado'
        }
        return render(request, 'wizards.html', context)