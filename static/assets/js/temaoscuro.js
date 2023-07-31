const btnSwitch = document.querySelector('#switch');
const body = document.body;
const switchKey = 'darkMode';

// Función para establecer el modo oscuro
function enableDarkMode() {
    body.classList.add('dark');
    btnSwitch.classList.add('active');
}

// Función para establecer el modo claro
function disableDarkMode() {
    body.classList.remove('dark');
    btnSwitch.classList.remove('active');
}

// Función para alternar entre el modo claro y oscuro
function toggleDarkMode() {
    if (body.classList.contains('dark')) {
        disableDarkMode();
        localStorage.setItem(switchKey, 'off');
    } else {
        enableDarkMode();
        localStorage.setItem(switchKey, 'on');
    }
}

// Evento click para el botón de cambio
btnSwitch.addEventListener('click', toggleDarkMode);

// Comprobar el estado almacenado en localStorage al cargar la página
document.addEventListener('DOMContentLoaded', () => {
    const darkModeState = localStorage.getItem(switchKey);

    if (darkModeState === 'on') {
        enableDarkMode();
    } else {
        disableDarkMode();
    }
});