document.getElementById('registroForm').addEventListener('submit', function (event) {
                            event.preventDefault();
                            const formData = new FormData(event.target);
                            fetch(registrarURL, {
                                method: 'POST',
                                body: formData,
                                headers: {
                                    'X-Requested-With': 'XMLHttpRequest',
                                    'X-CSRFToken': '{{ csrf_token }}',
                                },
                            })
                                .then(response => response.json())
                                .then(data => {
                                    if (data.success) {
                                        mensaje2();
                                    } else {
                                        mensaje();
                                    }
                                })
                                .catch(error => {
                                    console.error('Error:', error);
                                });
                            });
                        
                        