// Cargar las estrellas en funcion al usuario
const estrellasInputs = document.querySelectorAll('.clasificacion input[type="radio"]');
const formulario = document.getElementById('calif');
estrellasInputs.forEach(estrellaInput => {
    estrellaInput.addEventListener('change', function () {
        formulario.submit();
    });
});
                            // Agregar un evento al hacer clic en el botón
                            document.getElementById('ver-puntuaciones').addEventListener('click', function () {
                                const puntuacionesContainer = document.getElementById('puntuaciones');
                                if (puntuacionesContainer.style.display === 'none') {
                                    puntuacionesContainer.style.display = 'block';
                                } else {
                                    puntuacionesContainer.style.display = 'none';
                                }
                            });
                        