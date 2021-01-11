function abrirModalDescuentos(ruta, ruta2, id){

    $.ajax({
        url: ruta2,
        data: {
            'id_parqueo':id,
        },
        dataType: 'json',
        success: function (data) {
            if(data.verif_alquiler){
                alert("EL VEHICULO TIENE ALQUILER EN CURSO Y NO PUEDE TENER DESCUENTOS")
            }else{
                $('#modalDescuentos').load(ruta,function(){
                    $(this).modal('show');
                });
            }
        }
    })
}
function registrarIncidentes(ruta, registroId){
    var descripcionText= document.getElementById("text-incidentes")
    var descripcion = descripcionText.value
    if(descripcion){
        $.ajax({
            url: ruta,
            data: {
                'id_parqueo':registroId,
                'descripcion':descripcion
            },
            dataType: 'json',
            success: function (data) {
                alert("DESCUENTO REGISTRADO CON EXITO")
                location.href=location.href
            }
        })
    }else{
        alert("DEBE LLENAR LOS CAMPOS")
    }
}
function registrarDescuentos(ruta, registroId){
    var montoInput = document.getElementById("descuento-monto")
    var descripcionText = document.getElementById("descuento-descripcion")

    var monto = montoInput.value
    var descripcion = descripcionText.value

    if(monto && descripcion){
        var opcion = confirm("ESTA SEGURO DE REGISTRAR DESCUENTO");
        if(opcion==true){
            $.ajax({
                url: ruta,
                data: {
                    'id_parqueo':registroId,
                    'monto':monto,
                    'descripcion':descripcion
                },
                dataType: 'json',
                success: function (data) {
                    alert("DESCUENTO REGISTRADO CON EXITO")
                    location.href=location.href
                }
            })
        }
    }else {
        alert("DEBE LLENAR LOS CAMPOS")
    }

}

function abrirModalIncidentes(ruta){
    console.log("la ruta es")
    console.log(ruta)

    $('#modalIncidente').load(ruta,function(){
        $(this).modal('show');


    });
}
function abrirModalRegistrarSalida(ruta){
    $('#modalIncidente').load(ruta,function(){
        $(this).modal('show');
    });
}

function registrarSalida(ruta, idRegistro, fecha_salida, id_tarifa, idEspacio, monto){

    console.log("EL ID REGISTRO ES: "+idRegistro)
    console.log("LA FECHA SALIDA ES: "+fecha_salida)
    console.log("EL ID TARIFA ES: "+id_tarifa)
    console.log("EL ID REGISTRO ES: "+idEspacio)
    console.log("EL MONTO ES: "+monto)

    var opcion = confirm("SE IMPRIMIRA EL TICKET DE SALIDA ESTA SEGURO DE REGISTRAR LA SALIDA")
    if(opcion){
        $.ajax({
            url: ruta,
            data: {
                'id_registro':idRegistro,
                'fecha_salida':fecha_salida,
                'id_tarifa':id_tarifa,
                'idEspacio':idEspacio,
                'monto':monto

            },
            dataType: 'json',
            success: function (data) {
                var rutaImprimirTicket='/menuEmpleado/SalidaVehiculos/imprimirTicketSalida/'
                location.href=rutaImprimirTicket+data.id_registro
                alert("SALIDA REGISTRADA CON EXITO")
                location.href=location.href

            }
        })
    }
}
function buscaralidaPorFiltro(ruta){
    var placaInput = document.getElementById("input-placa-filtro")
    var placa = placaInput.value
    if(placa){
        $.ajax({
            url: ruta,
            data: {
                'placa':placa
            },
            dataType: 'json',
            success: function (data) {
                console.log(data.lista)
                mostarEnTabla(data.lista)
            }
        })
    }else{
        alert("DEBE LLENAR EL CAMPO DE BUSQUEDA")
    }

}
function mostarEnTabla(data){
    $("#table-salida-vehiculos > tbody > tr").remove()
    for(item in data){
        $("#table-salida-vehiculos > tbody").append(`
        <tr>
            <td style="width: 125px" >${data[item].placa}</td>
            <td style="width: 125px" >${data[item].sector} - ${data[item].posicion}</td>
            <td style="width: 200px" >${data[item].entrada}</td>
            <td style="width: 125px" >${data[item].tipo}</td>
            <td style="width: 175px" >
                <button type="button" onclick="abrirModalDescuentos('${rutaModalDescuentos+data[item].id}','${rutaVerificarAlquiler}',${data[item].id})" class="btn botonSeleccionar">
                    <i class="fas fa-sign-in-alt margin-boton-seleccionar"></i>AGREGAR
                </button>
            </td>
            <td style="width: 175px" >

                <button type="button" onclick="abrirModalIncidentes('${rutaModalIncidentes+data[item].id}')" class="btn botonIncidente">
                    <i class="fas fa-sign-in-alt margin-boton-seleccionar"></i>REGISTRAR
                </button>
            </td>
            <td style="width: 175px" >
                <button type="button" onclick="abrirModalRegistrarSalida('${rutaModalSalida+ data[item].id}')" class="btn botonSalida">
                    <i class="fas fa-sign-in-alt margin-boton-seleccionar"></i>REGISTRAR
                </button>
            </td>
        </tr>
        `)
    }

}