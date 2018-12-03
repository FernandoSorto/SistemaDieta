from django.shortcuts import render, redirect

from .models import Ingrediente, Plato
import itertools
# Create your views here.

def paginaPrincipalDieta(request):
    return render(request, 'dieta/paginaPrincipal.html', {})

def paginaCrearDieta(request):
    queryset_ingredietes = Ingrediente.objects.all()
    context = {
            "object_list": queryset_ingredietes
        }
    if request.method == 'POST':
        #VARIABLES

        #FILTROS
        tipoDie = request.POST.get('tipoDieta')
        calorias = request.POST.get('calorias')
        azal = request.POST.getlist('asal')
        ingredientes = request.POST.getlist('ingredientes')

        #FILTRANDO PLATOS
        todos = Plato.objects.all()
        platos_desayuno = todos.filter(tiempoComida='Desayuno').filter(dietaCal=calorias) #filtrado por calorias y por tiempo de comida
        platos_almuerzo = todos.filter(tiempoComida='Almuerzo').filter(dietaCal=calorias)
        platos_cena = todos.filter(tiempoComida='Cena').filter(dietaCal=calorias)

        if tipoDie == '2':
            platos_desayuno = platos_desayuno.filter(tipoDieta="veget")
            platos_almuerzo = platos_almuerzo.filter(tipoDieta="veget")
            platos_cena = platos_cena.filter(tipoDieta="veget")


        if len(ingredientes)> 0:
            filDesayuno = platos_desayuno
            filAlmuerzo = platos_almuerzo
            filCena = platos_cena
            for x in range(0, len(ingredientes)):
                filDesayuno = filDesayuno.exclude(ingredientes__id=ingredientes[x])
                filAlmuerzo = filAlmuerzo.exclude(ingredientes__id=ingredientes[x])
                filCena = filCena.exclude(ingredientes__id=ingredientes[x])

            listaDes = list(filDesayuno)
            if len(listaDes)<7:
                i = 0
                while len(listaDes)<7:
                    if i>=len(filDesayuno):
                        i=0
                    listaDes.append(filDesayuno[i])
                    i+=1

            listaAlm = list(filAlmuerzo)
            if len(listaAlm)<7:
                i = 0
                while len(listaAlm)<7:
                    if i>=len(filAlmuerzo):
                        i=0
                    listaAlm.append(filAlmuerzo[i])
                    i+=1

            listaCen = list(filCena)
            if len(listaCen)<7:
                i=0
                while len(listaCen)<7:
                    if i>=len(filCena):
                        i=0
                    listaCen.append(filCena[i])
                    i+=1
            context = {
                    "desayunos_list": listaDes,
                    "almuerzo_list": listaAlm,
                    "cena_list": listaCen,
                }
            return render(request, 'dieta/dietaSemana.html', context)

        #Listas
        listaDes = list(platos_desayuno)
        if len(listaDes)<7:
            i = 0
            while len(listaDes)<7:
                if i>=len(platos_desayuno):
                    i=0
                listaDes.append(platos_desayuno[i])
                i+=1

        listaAlm = list(platos_almuerzo)
        if len(listaAlm)<7:
            i = 0
            while len(listaAlm)<7:
                if i>=len(platos_almuerzo):
                    i=0
                listaAlm.append(platos_almuerzo[i])
                i+=1

        listaCen = list(platos_cena)
        if len(listaCen)<7:
            i=0
            while len(listaCen)<7:
                if i>=len(platos_cena):
                    i=0
                listaCen.append(platos_cena[i])
                i+=1

        #PREPARANDO CONTEXTO SIN FILTRO DE INGREDIENTE
        context = {
                "desayunos_list": listaDes,
                "almuerzo_list": listaAlm,
                "cena_list": listaCen,
            }
        return render(request,'dieta/dietaSemana.html', context)
    return render(request, 'dieta/crearDieta.html', context)

def paginaDietaSemanal(request):
    return render(request, 'dieta/dietaSemana.html', {})
