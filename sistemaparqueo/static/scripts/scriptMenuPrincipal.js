function cerrarCesion(ruta){
    var opcion = confirm("ESTA SEGURO DE CERRAR SESION")
    if (opcion){
        location.href=ruta
    }
}