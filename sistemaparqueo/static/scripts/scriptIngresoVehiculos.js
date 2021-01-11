
function definirEspacio(idSector, valueSector, valueEspacio, tipo_espacio){
    var input=document.getElementById("input_espacio")
    input.value=""+valueSector+"-"+valueEspacio

    var input=document.getElementById("status_espacio")
    input.value=idSector

    var input=document.getElementById("id_tipo_espacio")
    input.value=tipo_espacio

}

function buscarPlaca(ruta){
    var placaInput=document.getElementById("input-placa")
    var placaValue=placaInput.value
    $.ajax({
        url:ruta,
        data: {
            'placa':placaValue
            },
            dataType: 'json',
            success: function (data) {
                if(data.vehiculoAlquiler){


                    var inputColor=document.getElementById("input-color")
                    inputColor.value = data.vehiculoAlquiler["color"]

                    var inputId=document.getElementById("status_placa")
                    inputId.value = data.vehiculoAlquiler["id_vehiculo"]
                    var inputstatus=document.getElementById("status")
                    inputstatus.value="VEHICULO REGISTRADO ANTERIORMENTE"

                }else{
                    var inputId=document.getElementById("status_placa")
                    inputId.value = 0

                    var inputColor=document.getElementById("input-color")
                    inputColor.value = ""

                    var inputstatus=document.getElementById("status")
                    inputstatus.value=""

                }

            }
    });
}
function registrarEntrada(ruta, ruta2, ruta3){
    var idEspacioInput =$('input[id="status_espacio"]').val().trim()
    var idPlacaVehiculoInput=$('input[id="status_placa"]').val().trim()
    var idUsuarioInput=$('input[id="status_usuario"]').val().trim()
    var idtipoEspacioInput=$('input[id="id_tipo_espacio"]').val().trim()

    var idTipoVehiculoSelect=$('select[id="select_tipo_vehiculo"]').val().trim()
    var placaInput=$('input[id="input-placa"]').val().trim()
    var colorInput=$('input[id="input-color"]').val().trim()

    if((idtipoEspacioInput== idTipoVehiculoSelect) && (placaInput && colorInput)){
        var opcion = confirm("Esta seguro de registrar entrada");
        if(opcion==true){
            $.ajax({
                url:ruta,
                data: {
                    'idEspacio':idEspacioInput,
                    'idPlaca':idPlacaVehiculoInput,
                    'idTipoVehiculo':idTipoVehiculoSelect,
                    'placa':placaInput,
                    'color':colorInput,
                    'usuario':idUsuarioInput
                    },
                    dataType: 'json',
                    success: function (data) {
                        location.href=ruta3+data.new_id_registro
                        alert("ENTRADA REGISTRADA CON EXITO")
                        location.href = location.href

                }
            });

            $('form#form-registro-entrada').trigger("reset");

        }
    }else{
        alert("EL TIPO DE VEHICULO DEBER SER EL MISMO QUE EL DEL ESPACIO o DEBE LLENAR TODOS LOS CAMPOS")
    }
}
