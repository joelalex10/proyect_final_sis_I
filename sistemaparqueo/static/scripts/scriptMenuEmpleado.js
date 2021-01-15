function verificarAperturaCaja(ruta,ruta2){
    $.ajax({
        url: ruta,
        data: {
        },
        dataType: 'json',
        success: function (data) {
            if(data.estado){
                location.href=ruta2
            }else{
                alert("DEBE HACER UNA APERTURA DE CAJA PARA ACCEDER A ESTA OPCION")
            }
        }
    })
}

function verificarClausuraCaja(ruta,ruta2){
    $.ajax({
        url: ruta,
        data: {
        },
        dataType: 'json',
        success: function (data) {
            if(data.estado){
                location.href=ruta2
            }else{
                alert("PARA CERRAR SESION DEBE HACER CIERRE DE CAJA")
            }
        }
    })
}

function cerrarCesion(ruta, ruta2){
    $.ajax({
        url: ruta,
        data: {
        },
        dataType: 'json',
        success: function (data) {
            if(data.estado){
                var opcion = confirm("ESTA SEGURO DE CERRAR SESION")
                if (opcion){
                    location.href=ruta2
                }
            }else{
                alert("DEBE HACER UN CIERRE DE CAJA PARA ACCEDER A ESTA OPCION")
            }
        }
    })

}