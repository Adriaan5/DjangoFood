from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect  
from .models import SeleccionTipoComida
from django.contrib import messages
from geopy.distance import geodesic  
import Restaurantes.models as Restaurantes


@csrf_protect
@login_required(login_url='login')
def comidas(request):
    if request.method == 'POST':
        tipo_comida = request.POST.get('tipo_comida')
        if tipo_comida:
            SeleccionTipoComida.objects.create(
                usuario=request.user,
                nombre_comida=tipo_comida
            )
            return redirect('home')  
        else:
            return JsonResponse({"error": "No se seleccionó comida."}, status=400)
    else:
        return render(request, 'comida/comida.html')


@csrf_protect
@login_required(login_url='login')
def buscar_restaurantes(request):
    if request.method == 'POST':
        nombre_comida = request.POST.get('nombre_comida')
        user_latitud = float(request.POST.get('latitud', 0))
        user_longitud = float(request.POST.get('longitud', 0))

        if not nombre_comida:
            messages.error(request, "No se selecciono ningún tipo de comida")
            return render(request, "comida/buscar_restaurantes.html")
        try:
            restaurantes = SeleccionTipoComida.objects.filter(tipo_comida__nombre_comida=nombre_comida)
            restaurantes_cercanos = []
            for restaurante in restaurantes:
                distancia = geodesic(
                    (user_latitud, user_longitud),
                    (restaurante.latitud, restaurante.longitud)
                ).km

                if distancia <= 10:
                    restaurantes_cercanos.append({
                        'nombre': restaurante.nombre,
                        'direccion': restaurante.direccion,
                    })
            if not restaurantes_cercanos:
                messages.error(request, "No se encontraron restaurantes cercanos")
                return render(request, "comida/buscar_restaurantes.html")
            
            return render(request, 'comida/buscar_restaurantes.html', {
                'restaurantes_cercanos': restaurantes_cercanos
            })

        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return render(request, 'comida/buscar_restaurantes.html')

    return render(request, 'comida/buscar_restaurantes.html')
     