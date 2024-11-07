function validaUsuario(){
    let usuario = document.getElementById("usuario")
    if(usuario.value == "" || usuario.value == null){
        //alert("Usuario es obligatorio!");
        document.getElementById("errorUsuario").innerHTML = "<strong></strong>"
        return
    }
    else{
        usuario.style.background = "white";
    }
}


function valida() {

    // Usuario es obligatorio
    let usuario = document.getElementById("usuario");
    if (usuario.value == "" || usuario.value == null){
        alert("Usuario es obligatorio");
        usuario.focus();
        return false;
    }

    // Usuario entre 4 y 12 caracteres, minusculas.
    let expUsuario = /^[a-z]{4,12}$/;
    if (!expUsuario.test(usuario.value)){
        alert("Usuario entre 4 y 12 caracteres, minusculas.");
        usuario.focus();
        return false;
    }

    // Clave es obligatoria
    let clave = document.getElementById("clave");
    if (clave.value == "" || clave.value == null){
        alert("Clave es obligatoria");
        clave.focus();
        return false;
    }

    // Clave es númerica entre 4 y 8 dígitos
    let expClave = /^[0-9]{4,8}$/;
    if (!expClave.test(clave.value)){
        alert("Clave es númerica entre 4 y 8 dígitos");
        clave.focus();
        return false;
    }

    // Nombre es obligatorio
    let nombre = document.getElementById("nombre");
    if (nombre.value == "" || nombre.value == null) {
        alert("Nombre es obligatorio");
        nombre.focus();
        return false;
    }
    // Nombre propio. Ej: Juan Antonio Esteban
    let expNombre = /^[A-ZÑ][a-zñ]+(\s[A-ZÑ][a-zñ]+)*$/;
    if (!expNombre.test(nombre.value)){
        alert("Nombre propio. \nEj: Juan Antonio Esteban");
        nombre.focus();
        return false;
    }
    // Apellido es obligatorio
    let apellido = document.getElementById("apellido");
    if (apellido.value == "" || apellido.value == null) {
        alert("Apellido es obligatorio");
        apellido.focus();
        return false;
    }
    // Apellido propio. Ej: Perez Soto
    let expApellido = /^[A-ZÑ][a-zñ]+(\s[A-ZÑ][a-zñ]+){0,1}$/;
    if (!expApellido.test(apellido.value)){
        alert("Apellido propio. \nEj: Perez Soto");
        apellido.focus();
        return false;
    }
    // Edad es obligatoria
    let edad = document.getElementById("edad");
    if (edad.value == "" || edad.value == null) {
        alert("Edad es obligatoria");
        edad.focus();
        return false;
    }
    // Edad entre 18 y 65 años
    let expEdad = /^[1][8-9]|[2-5][0-9]|[6][0-5]$/;
    if (!expEdad.test(edad.value)){
        alert("Edad entre 18 y 65 años");
        edad.focus();
        return false;
    }
    // Comuna es obligatoria
    let comuna = document.getElementById("comuna");
    if (comuna.selectedIndex == 0){
        alert("Comuna es obligatoria");
        comuna.focus();
        return false;
    }
    // Color es obligatorio
    let color = document.getElementsByName("color");
    let seleccionado = false;
    for (i = 0; i < color.length; i++){
        if (color[i].checked){
            seleccionado = true;
            break;
        }
    }
    if (seleccionado == false){
        alert("Color es obligatorio");
        return false;
    }
    // Hobbies es obligatorio. Seleccione máximo 2 hobbies.
    let hobbies = document.getElementsByName("hobbies");
    let cont = 0;
    for (i = 0; i < hobbies.length; i++){
        if(hobbies[i].checked){
            cont++;
        }
    }
    if (cont == 0 || cont > 2){
        alert("Hobbies es obligatorio. \nSeleccione máximo 2 hobbies.");
        return false;
    }

}