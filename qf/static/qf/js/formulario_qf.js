function validarFormulario() {
    // Obtener los valores de los campos
    var nombreElem = document.getElementById('nombre');
    var rutElem = document.getElementById('rut');
    var sexoElem = document.getElementById('sexo');
    var tituloElem = document.getElementById('titu');
    var fechaNacElem = document.getElementById('fecha_nac');
    var telefonoElem = document.getElementById('telefono');
    var emailElem = document.getElementById('email');
    var universidadElem = document.getElementById('uni');
    var claveElem = document.getElementById('clave');
    var confirmarClaveElem = document.getElementById('confirmar_clave');

    // Obtener los valores de los campos
    var nombre = nombreElem.value;
    var rut = rutElem.value;
    var sexo = sexoElem.value;
    var titulo = tituloElem.value;
    var fecha_nac = fechaNacElem.value;
    var telefono = telefonoElem.value;
    var email = emailElem.value;
    var universidad = universidadElem.value;
    var clave = claveElem.value;
    var confirmar_clave = confirmarClaveElem.value;
    //mensajes de error
    var msj ='';
    
    var mensajeError = document.getElementById('mensajeError');
    mensajeError.innerHTML = ''; // Limpiar mensajes anteriores
    
    
    // Validar que los campos no estén vacíos
    
    if (rut == "" ) {
        rutElem.classList.add('error');
         //msj = 'campo incompleto';
         mensajeError.innerHTML = msj;
    //alert("Por favor, rellene el campo rut.");
     return false;
 }
    if (nombre == "" ) {
            nombreElem.classList.add('error');
            //msj = 'campo incompleto';
           
       //alert("Por favor, rellene el campo nombre.");
        return false;
    }
   
if (telefono == "" ) {
    telefonoElem.classList.add('error');
    //msj = 'campo incompleto';
    mensajeError.innerHTML = msj;
//alert("Por favor, rellene el campo telefono.");
return false;
}
if (titulo == "" ) {
    tituloElem.classList.add('error');
    //msj = 'campo incompleto';
    mensajeError.innerHTML = msj;
//alert("Por favor, rellene el campo titulo.");
return false;
}



    // Validar que las contraseñas coincidan
    if (clave !== confirmar_clave) {
        alert("Las contraseñas no coinciden.");
        return false;
    }

    // Validar el formato del correo electrónico
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert("Por favor, introduzca un correo electrónico válido.");
        return false;
    }

    // Validación exitosa
    return true;}