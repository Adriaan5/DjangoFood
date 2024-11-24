document.addEventListener('DOMContentLoaded', function () {
    const formulario = document.getElementById('reserva-form');
    const mensajeConfirmacion = document.getElementById('mensaje-confirmacion');

    formulario.addEventListener('submit', function (event) {
        event.preventDefault(); // Evitar el envío del formulario por defecto

        // Mostrar mensaje de confirmación
        mensajeConfirmacion.innerText = '¡Reserva solicitada con éxito!';
        mensajeConfirmacion.style.display = 'block';

        // Limpiar el formulario
        formulario.reset();

        // Ocultar el mensaje de confirmación después de 3 segundos
        setTimeout(() => {
            mensajeConfirmacion.style.display = 'none';
        }, 3000);
    });
});
