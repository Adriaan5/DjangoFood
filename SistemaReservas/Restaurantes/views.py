from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import SolicitarReservaForm, ModificarReservaForm
from .models import Reserva, GenerarID

@login_required(login_url='login')  
def homepage(request):
    return render(request, 'register/home.html')

@login_required(login_url='login')
def solicitar_reserva(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        fecha_hora = request.POST.get('fecha_hora')
        num_personas = request.POST.get('num_personas')

        if not all([nombre, fecha_hora, num_personas]):
            messages.error(request, 'Por favor, completa todos los campos.')
            return render(request, 'restaurantes/solicitar_reserva.html')

        id_reserva = GenerarID()

        nueva_reserva = Reserva(
            usuario=request.user,
            fecha_hora=fecha_hora,
            num_personas=num_personas,
            id_reserva=id_reserva,
        )
        nueva_reserva.save()  

        messages.success(request, 'Reserva solicitada exitosamente.')
        return redirect('reserva_exitosa', id_reserva=id_reserva)  
    else:
        return render(request, 'restaurantes/solicitar_reserva.html')

@login_required(login_url='login')
def reserva_exitosa(request, id_reserva):
    reserva = get_object_or_404(Reserva, id_reserva=id_reserva)
    return render(request, 'restaurantes/reserva_exitosa.html', {'reserva': reserva})

@login_required(login_url='login')
def modificar_reserva(request):
    if request.method == 'POST':
        id_reserva = request.POST.get('id_reserva')

        if not id_reserva:
            messages.error(request, 'Por favor ingrese el ID de la reserva.')
            return render(request, 'restaurantes/modificar_reserva.html')

        try:
            reserva = Reserva.objects.get(id_reserva=id_reserva) 
            
            if 'fecha_hora' in request.POST and 'num_personas' in request.POST:
                reserva.fecha_hora = request.POST.get('fecha_hora')
                reserva.num_personas = request.POST.get('num_personas')
                reserva.save()  
                
                messages.success(request, 'Reserva modificada correctamente.')
                return redirect('home')  
            
            return render(request, "restaurantes/modificacion.html", {"reserva": reserva})

        except Reserva.DoesNotExist:
            messages.error(request, 'Reserva no encontrada.')
            return render(request, 'restaurantes/modificar_reserva.html')
    else:
        return render(request, 'restaurantes/modificar_reserva.html')

@login_required(login_url='login')
def modificacion(request):
    if request.method == 'POST':
        num_personas = request.POST.get('num_personas')
        fecha_hora = request.POST.get('fecha_hora')

        if not num_personas or not fecha_hora:
            messages.error(request, "Por favor rellena los campos.")
            return render(request, "restaurantes/modificacion.html")
        
        try:
            reserva = Reserva.objects.get(num_personas=num_personas, fecha_hora=fecha_hora)
            return render(request, "restaurantes/modificacion.html", {"reserva": reserva})

        except Reserva.DoesNotExist:
            messages.error(request, "Reserva no encontrada.")
            return render(request, "restaurantes/modificacion.html")
    else:
        return render(request, 'register/home.html')

@login_required(login_url='login')
def cancelar_reserva(request):
    if request.method == 'POST':
        id_reserva = request.POST.get('id_reserva')

        if not id_reserva:
           messages.error(request, "Por favor ingrese el ID de la reserva que desea cancelar.")

        try:
            reserva = Reserva.objects.get(id_reserva=id_reserva)
            
            reserva.delete()
            
            messages.success(request, "La reserva ha sido cancelada correctamente.")
            return redirect("home")
        
        except Reserva.DoesNotExist:
            messages.error(request, "Reserva no encontrada.")
            return render(request, "restaurantes/cancelar_reserva.html")
    else:
       return render(request, "restaurantes/cancelar_reserva.html")

def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('login')

