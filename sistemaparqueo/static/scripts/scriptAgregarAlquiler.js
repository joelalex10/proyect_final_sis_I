

function agregarNuevoAlquiler(ruta,ruta2){
    cont=0;

    var opcion= confirm("ESTA SEGURO DE REGISTRAR ALQUILER")
    if(opcion){
        $("form#formAgregarAlquileres").submit(function() {
            cont++
            if(cont<=1){
                console.log("LOS VALORES SON")
                var ciInput =$('input[name="form_alquiler_ci"]').val().trim()
                var nombreInput =$('input[name="form_alquiler_nombre"]').val().trim()
                var placaInput =$('input[name="form_alquiler_placa"]').val().trim()
                var marcaModeloInput =$('input[name="form_alquiler_marca_modelo"]').val().trim()
                var colorInput =$('input[name="form_alquiler_color"]').val().trim()
                var tipoVehiculoInput =$('select[name="form_tipo_vehiculo"]').val().trim()
                var tarifaInput =$('select[name="form_tarifa"]').val().trim()
                var numCuotasInput =$('input[name="form_numero_cuotas"]').val().trim()
                var idCliente =$('input[name="status_ci"]').val().trim()
                var idVehiculo =$('input[name="status_vehiculo"]').val().trim()
                console.log("el id Vehiculo es: "+idVehiculo)
                if(ciInput){
                    $.ajax({
                        url: ruta,
                        data: {
                            'idCliente':idCliente,
                            'idVehiculo':idVehiculo,
                            'ci':ciInput,
                            'nombre':nombreInput,
                            'placa':placaInput,
                            'marcaModelo':marcaModeloInput,
                            'color':colorInput,
                            'tipoVehiculo':tipoVehiculoInput,
                            'tarifa':tarifaInput,
                            'numCuotas':numCuotasInput
                        },
                        dataType: 'json',
                        success: function (data) {
                            alert("ALQUILER REGISTRADO CON EXITO")
                            location.href=ruta2
                        }
                    })
                }else{
                    alert("DEBE LLENAR TODOS LOS CAMOPS")
                }
            return false
            }
        })
    }
}

function buscarCiCliente(ruta){
    $(document).ready(function (){
        cont=0
        $("input#f_ci").on("keyup",function (){
            cont++
            if(cont<=1){
                var ciInput = $(this).val()
                $.ajax({
                    url:ruta,
                    data: {
                        'ci':ciInput
                        },
                        dataType: 'json',
                        success: function (data) {
                            if(data.cliente){

                                var vehicleResultP=document.getElementById("client-result")
                                vehicleResultP.innerHTML="CLIENTE REGISTRADO"

                                $("#input_Cliente > input").remove()
                                $("#status_r_ci >input").remove()

                                $("#input_Cliente").append(`
                                <input name="form_alquiler_nombre"  value="${data.cliente["nombre"]}" type="text" class="form-control border border-secondary" placeholder="Ingrese el nombre del cliente" aria-label="Username" aria-describedby="basic-addon1">
                                `)
                                $("#status_r_ci").append(`
                                <input name="status_ci" value="${data.cliente["id_cliente"]}" class="form-control" type="hidden"/>
                                `)

                            }else{

                                var vehicleResultP=document.getElementById("client-result")
                                vehicleResultP.innerHTML=""
                                $("#input_Cliente > input").remove()
                                $("#status_r_ci >input").remove()

                                $("#input_Cliente").append(`
                                    <input name="form_alquiler_nombre"  value="" type="text" class="form-control border border-secondary" placeholder="Ingrese el nombre del cliente" aria-label="Username" aria-describedby="basic-addon1"> 
                                `)
                                $("#status_r_ci").append(`
                                <input name="status_ci" value="0" class="form-control" type="hidden"/>
                                `)
                            }
                        }
                });
                return false
            }
        });
    });
}

function buscarPlacaVehiculo(ruta){
    $(document).ready(function (){
        cont=0
        $("input#f_placa").on("keyup",function (){
            cont++
            if(cont<=1){
                var placaInput = $(this).val()
                var idClienteInput =$('input[name="status_ci"]').val().trim()
                console.log("EL id cliente es: "+idClienteInput)
                $.ajax({
                    url:ruta,
                    data: {
                        'placa': placaInput,
                        'idCliente': idClienteInput
                        },
                        dataType: 'json',
                        success: function (data) {
                            if(data.vehiculo){

                                var vehicleResultP=document.getElementById("vehicle-result")
                                vehicleResultP.innerHTML="VEHICULO REGISTRADO"

                                $("#input_marca_modelo > input").remove()
                                $("#input_color > input").remove()
                                $("#status_r_vehiculo >input").remove()

                                //document.getElementById("select_tipo").selectedIndex = data.vehiculo["id_vehiculo"];
                                document.getElementById("select_tipo").selectedIndex = data.vehiculo["tipo_vehiculo_id"];

                                $("#input_marca_modelo").append(`
                                <input name="form_alquiler_marca_modelo" value="${data.vehiculo["marca_modelo"]}" type="text" class="form-control border border-secondary" placeholder="Ingrese la marca y el modelo del vehiculo" aria-label="Username" aria-describedby="basic-addon1">
                                `)
                                $("#input_color").append(`
                                <input name="form_alquiler_color" value="${data.vehiculo["color"]}" type="text" class="form-control border border-secondary" placeholder="Ingrese el color del vehiculo" aria-label="Username" aria-describedby="basic-addon1">
                                `)
                                $("#status_r_vehiculo").append(`                                
                               <input name="status_vehiculo" value="${data.vehiculo["id_vehiculo"]}" class="form-control" type="hidden"/>
                                `)
                            }else{


                                var vehicleResultP=document.getElementById("vehicle-result")
                                vehicleResultP.innerHTML=""

                                $("#input_marca_modelo > input").remove()
                                $("#input_color > input").remove()
                                $("#status_r_vehiculo >input").remove()

                                document.getElementById("select_tipo").selectedIndex = 0;

                                $("#input_marca_modelo").append(`
                                <input name="form_alquiler_marca_modelo" value="" type="text" class="form-control border border-secondary" placeholder="Ingrese la marca y el modelo del vehiculo" aria-label="Username" aria-describedby="basic-addon1">
                                `)
                                $("#input_color").append(`
                                <input name="form_alquiler_color" value="" type="text" class="form-control border border-secondary" placeholder="Ingrese el color del vehiculo" aria-label="Username" aria-describedby="basic-addon1">
                                `)
                                $("#status_r_vehiculo").append(`                                
                               <input name="status_vehiculo" value="0" class="form-control" type="hidden"/>
                                `)
                            }
                        }
                });
                return false
            }
        });
    });
}