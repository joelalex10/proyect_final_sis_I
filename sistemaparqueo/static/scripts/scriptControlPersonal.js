function buscarFiltrosControlEmpleados(ruta){
    var inputUsuario = document.getElementById("input-usuario")
    var inputFecha = document.getElementById("input-fecha")

    if(inputFecha.value || inputUsuario.value){
        $.ajax({
        url: ruta,
        data: {
            "ciUsuario":inputUsuario.value,
            "Fecha":inputFecha.value
        },
        dataType: 'json',
        success: function (data) {
            console.log(data.lista)
            mostarEnTabla(data.lista)
        }
    })

    }else{
        alert("DEBE LLENAR UNO DE LOS FILTROS")
    }


}

function mostarEnTabla(data){
    $("#control_horario > tbody > tr").remove()
    for(item in data){
        var tarde="";
        var colorTarde=""

        var temprano="";
        var colorTemprano=""

        if( data[item].ingreso > data[item].hora_ingreso){
            tarde="SI"
            colorTarde="red"
        }else{
            tarde="NO"
            colorTarde="green"
        }
        if( data[item].salida < data[item].hora_salida){
            temprano="SI"
            colorTemprano="red"
        }else{
            temprano="NO"
            colorTemprano="green"
        }
        $("#control_horario > tbody").append(`
        <tr>
            <td style="width: 100px"  >${data[item].fecha}</td>
            <td style="width: 250px"  >${data[item].nombre}</td>
            <td style="width: 140px" >${data[item].ingreso}</td>
            <td style="width: 125px" >${data[item].salida}</td>
            <td style="width: 150px; color: ${colorTarde}">${tarde}</td>
            <td style="width: 150px; color: ${colorTemprano}">${temprano}</td>
        </tr>
        
        `)
    }
}