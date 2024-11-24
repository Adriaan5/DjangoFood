function obtenerUbicacion() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(enviarUbicacion, mostrarError);
    } else {
        alert("La geolocalización no es compatible con este navegador.");
    }
}

function enviarUbicacion(position) {
    const latitud = position.coords.latitude;
    const longitud = position.coords.longitude;

    fetch('/buscar_restaurantes/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value  
        },
        body: JSON.stringify({ latitud: latitud, longitud: longitud })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);  
    })
    .catch(error => console.error('Error:', error));
}

function mostrarError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
            alert("Permiso de geolocalización denegado.");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("La información de ubicación no está disponible.");
            break;
        case error.TIMEOUT:
            alert("La solicitud de ubicación ha caducado.");
            break;
        case error.UNKNOWN_ERROR:
            alert("Se produjo un error desconocido.");
            break;
    }
}
