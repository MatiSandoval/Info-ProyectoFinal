// Cargar las estrellas en funcion al usuario
const estrellasInputs = document.querySelectorAll('.clasificacion input[type="radio"]');
const formulario = document.getElementById('calif');
estrellasInputs.forEach(estrellaInput => {
    estrellaInput.addEventListener('change', function () {
        formulario.submit();
    });
});
// Obtener el botón y el contenedor de puntuaciones
const verPuntuacionesBtn = document.getElementById('ver-puntuaciones');
const puntuacionesContainer = document.getElementById('puntuaciones');
// Agregar un evento al hacer clic en el botón
verPuntuacionesBtn.addEventListener('click', function () {
    puntuacionesContainer.style.display = puntuacionesContainer.style.display === 'none' ? 'block' : 'none';
});