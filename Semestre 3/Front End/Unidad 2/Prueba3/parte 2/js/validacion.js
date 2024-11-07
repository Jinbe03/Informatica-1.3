function validaFormulario() {
    let isValid = true;

    if (!validaUsuario()) {
        isValid = false;
    }

    let nombres = document.getElementById('nombres').value;
    if (nombres === '' || !/^[A-Z\s]{1,20}$/.test(nombres)) {
        alert("El Nombre es obligatorio y debe contener solo letras mayúsculas y espacios (máximo 20 caracteres).");
        isValid = false;
    }

    let edad = document.getElementById('edad').value;
    if (edad === '' || !/^\d+$/.test(edad) || edad < 27 || edad > 53) {
        alert("La Edad es obligatoria y debe ser entre 27 y 53.");
        isValid = false;
    }

    if (!validaEmail()) {
        isValid = false;
    }

    let fecha = document.getElementById('fecha').value;
    if (fecha === '') {
        alert("La Fecha es obligatoria.");
        isValid = false;
    }

    let comuna = document.getElementById('comuna').value;
    if (comuna === '') {
        alert("La Comuna es obligatoria.");
        isValid = false;
    }

    let genero = document.querySelector('input[name="genero"]:checked');
    if (genero === null) {
        alert("El Género es obligatorio.");
        isValid = false;
    }

    return isValid;
}

function validaUsuario() {
    let usuario = document.getElementById('usuario').value;
    if (usuario === '' || !/^[a-z]{6,12}$/.test(usuario)) {
        alert("El Usuario es obligatorio y debe contener solo letras minúsculas entre 6 y 12 caracteres.");
        return false;
    }
    return true;
}

function validaEmail() {
    let email = document.getElementById('email').value;
    if (email === '') {
        alert("El Email es obligatorio.");
        return false;
    }
    return true;
}
