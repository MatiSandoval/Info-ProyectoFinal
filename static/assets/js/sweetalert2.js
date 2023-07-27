document.getElementById('loginForm').addEventListener('submit', function (event) {
                event.preventDefault();
                const formData = new FormData(event.target);
                fetch(loginURL, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                        'X-CSRFToken': '{{ csrf_token }}',
                    },
                })
                    .then(response => {
                        if (response.ok) {
                            mensaje();
                        } else {
                            mensaje2();
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
            });