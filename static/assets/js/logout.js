document.getElementById('logout-button').addEventListener('click', function () {
                    fetch('{% url "apps.usuario:logout" %}', {
                        method: 'POST',
                        headers: {
                            'X-CSRFToken': '{{ csrf_token }}',
                        },
                    })
                        .then(response => response.json())
                        .then(data => {
                            if (data.success) {
                                // Mostrar Sweet Alert de éxito

                                var x = "{% url 'index' %}";
                                Swal.fire({
                                    icon: 'success',
                                    title: '¡Sesión cerrada!',
                                    text: '',
                                    showCancelButton: false,
                                    confirmButtonColor: '#3085d6',
                                    confirmButtonText: 'OK',
                                }).then((result) => {
                                    // El usuario hizo clic en el botón "Ir a Iniciar Sesión"
                                    if (result.isConfirmed) {
                                        // Redirige a la página de inicio de sesión
                                        window.location.href = x;
                                    }
                                });

                            }
                        })
                        .catch(error => {
                            console.error('Error:', error);
                        });
                });