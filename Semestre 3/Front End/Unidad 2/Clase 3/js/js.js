document.getElementById("formulario").addEventListener("submit", function(event) {
    event.preventDefault();
    alert("Formulario enviado correctamente");
});

document.querySelector("button[type='reset']").addEventListener("click", function() {
    document.getElementById("formulario").reset(); 
});
