const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

function seleccionarImagen(imagen) {
    const nombreComida = imagen.split('/').pop().split('.')[0];

    fetch('/comidas/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken  
        },
        body: 'tipo_comida=' + encodeURIComponent(nombreComida)
    })
    .then(response => {
        if (response.ok) {
            window.location.href = '/home/';
        } else {
            console.error('Error al guardar la selección de comida.');
        }
    })
    .catch(error => {
        console.error('Error de red:', error);
    });
}
