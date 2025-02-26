from django.shortcuts import render, redirect
from .models import Vuelo
from django.db.models import Avg

def registrar_vuelo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        precio = request.POST.get('precio')

        if not nombre or not tipo or not precio:
            return render(request, 'registrar_vuelo.html', {'error': 'Todos los campos son obligatorios'})

        try:
            precio = float(precio)
        except ValueError:
            return render(request, 'registrar_vuelo.html', {'error': 'El precio debe ser un número'})

        vuelo = Vuelo(nombre=nombre, tipo=tipo, precio=precio)
        vuelo.save()
        return redirect('listar_vuelos')

    return render(request, 'registrar_vuelo.html')

def listar_vuelos(request):
    vuelos = Vuelo.objects.all().order_by('precio')
    return render(request, 'listar_vuelos.html', {'vuelos': vuelos})

def estadisticas_vuelos(request):
    nacionales = Vuelo.objects.filter(tipo='Nacional').count()
    internacionales = Vuelo.objects.filter(tipo='Internacional').count()

    promedio_nacional = Vuelo.objects.filter(tipo='Nacional').aggregate(Avg('precio'))['precio__avg'] or 0

    return render(request, 'estadisticas_vuelos.html', {
        'nacionales': nacionales,
        'internacionales': internacionales,
        'promedio_nacional': round(promedio_nacional, 2)
    })