from django.shortcuts import render, redirect
from .models import Ruta
from .forms import RutaForm
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.db.models import Count, Sum
from .models import Ruta
import json

def home(request):
    return render(request, 'rutas/home.html')

def about(request):
    return render(request, 'rutas/about.html')

def panel_control(request):
    # Traemos todas las rutas registradas en el sistema
    rutas = Ruta.objects.all()
    return render(request, 'rutas/panel_control.html', {'rutas': rutas})

def crear_ruta(request):
    if request.method == 'POST':
        form = RutaForm(request.POST)
        if form.is_valid():
            form.save() # Guarda los datos en la base de datos de forma segura
            return redirect('panel_control') # Nos regresa al panel de la tabla
    else:
        form = RutaForm() # Formulario vacío para el método GET
    
    return render(request, 'rutas/crear_ruta.html', {'form': form})

def editar_ruta(request, pk):
    # Buscamos la ruta por su ID, si no existe lanza un error 404
    ruta = get_object_or_404(Ruta, pk=pk)
    
    if request.method == 'POST':
        # Pasamos los datos del formulario pero vinculados a la instancia de la ruta existente
        form = RutaForm(request.POST, instance=ruta)
        if form.is_valid():
            form.save()
            return redirect('panel_control')
    else:
        form = RutaForm(instance=ruta) # Carga el formulario con los datos actuales de la ruta
        
    return render(request, 'rutas/crear_ruta.html', {'form': form, 'editando': True})

def eliminar_ruta(request, pk):
    ruta = get_object_or_404(Ruta, pk=pk)
    if request.method == 'POST':
        ruta.delete() # Borra el registro físicamente de la base de datos
        return redirect('panel_control')
        
    return render(request, 'rutas/confirmar_eliminar.html', {'ruta': ruta})



def panel_control(request):
    rutas = Ruta.objects.all()

    destinos_populares = Ruta.objects.values('destino').annotate(total_salidas=Count('id')).order_by('-total_salidas')[:5]
    destinos_ingresos = Ruta.objects.values('destino').annotate(total_ingresos=Sum('precio_pasaje')).order_by('-total_ingresos')[:5]

    labels_populares = [item['destino'] for item in destinos_populares]
    data_populares = [item['total_salidas'] for item in destinos_populares]

    labels_ingresos = [item['destino'] for item in destinos_ingresos]
    data_ingresos = [float(item['total_ingresos'] or 0) for item in destinos_ingresos]

    # ¡LA SOLUCIÓN! Convertimos a JSON estricto desde Python
    context = {
        'rutas': rutas,
        'labels_populares': json.dumps(labels_populares),
        'data_populares': json.dumps(data_populares),
        'labels_ingresos': json.dumps(labels_ingresos),
        'data_ingresos': json.dumps(data_ingresos),
    }

    return render(request, 'rutas/panel_control.html', context)