// Obtener la referencia a los inputs de estrellas y al formulario
                                const estrellasInputs = document.querySelectorAll('.clasificacion input[type="radio"]');
                                const formulario = document.getElementById('calif');

                                // Agregar un evento al cambiar el valor de un input de estrella
                                estrellasInputs.forEach(estrellaInput => {
                                    estrellaInput.addEventListener('change', function () {
                                        // Enviar el formulario automáticamente
                                        formulario.submit();
                                    });
                                });
                                // Obtener el botón y el contenedor de puntuaciones
                                    const verPuntuacionesBtn = document.getElementById('ver-puntuaciones');
                                    const puntuacionesContainer = document.getElementById('puntuaciones');

                                    // Agregar un evento al hacer clic en el botón
                                    verPuntuacionesBtn.addEventListener('click', function () {
                                        // Mostrar u ocultar el contenedor de puntuaciones al hacer clic en el botón
                                        puntuacionesContainer.style.display = puntuacionesContainer.style.display === 'none' ? 'block' : 'none';
                                    });