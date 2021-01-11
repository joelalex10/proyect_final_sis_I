function agregarTarifaRegistro(ruta){
    cont=0;
    $("form#agregar_tarifa_registro").submit(function() {
        cont++;
        if(cont<=1){

            var horasInput =$('input[name="f_horas"]').val().trim()
            var diasInput =$('input[name="f_dias"]').val().trim()
            var precioInput =$('input[name="f_precio"]').val().trim()

            if(horasInput && diasInput && precioInput){
                $.ajax({
                    url: ruta,
                    data: {
                        'hora':horasInput,
                        'dia':diasInput,
                        'precio':precioInput
                    },
                    dataType: 'json',
                    success: function (data) {
                        console.log("los datos son")
                        console.log(data)
                        $('form#agregar_tarifa_registro').trigger("reset");
                        location.href=location.href
                        return true
                    }
                });
            }else{
                alert("DEBE LLENAR TODOS LOS CAMPOS")
            }
        return false
        }
    });
}

function agregarTarifaAlquiler(ruta){
    cont=0;
    $("form#f_tarifa_alquiler").submit(function() {
        cont++;
        if(cont<=1){

            var mesInput =$('input[name="f_mes"]').val().trim()
            var precioAlquilerInput =$('input[name="f_precio_alquiler"]').val().trim()

            if(mesInput && precioAlquilerInput){
                $.ajax({
                    url: ruta,
                    data: {
                        'mes':mesInput,
                        'precio':precioAlquilerInput
                    },
                    dataType: 'json',
                    success: function (data) {
                        console.log("los datos son")
                        console.log(data)
                        $('form#agregar_tarifa_registro').trigger("reset");
                        location.href=location.href
                        return true
                    }
                });
            }else{
                alert("DEBE LLENAR TODOS LOS CAMPOS")
            }
        return false
        }
    });
}

function abrirModalTarifaAlquiler(ruta){
    $('#modalTarifaRegistro').load(ruta,function(){
        $(this).modal('show');
    });
}

function editarTarifaAlquiler(ruta){
    cont=0;
    $("form#form_edit_tarifa_alquiler").submit(function() {
        cont++;
        if(cont<=1){
            var edIdAlInput =$('input[name="f_id_a_tarifa"]').val().trim()
            var edMesesAlInput =$('input[name="f_meses_a_tarifa"]').val().trim()
            var edPrecioAlInput =$('input[name="f_precio_a_tarifa"]').val().trim()
            if(edIdAlInput){
                $.ajax({
                    url: ruta,
                    data: {
                        'id':edIdAlInput,
                        'meses':edMesesAlInput,
                        'precio':edPrecioAlInput
                    },
                    dataType: 'json',
                    success: function (data) {
                        console.log("los datos son")
                        console.log(data)
                        $('form#form_edit_tarifa_alquiler').trigger("reset");
                        location.href=location.href
                        return true
                    }
                });
            }else{
                alert("LAS CONTRASEÑAS DEBEN SER IGUALES")
            }
        return false
        }
    });
}

function abrirModalTarifaRegistro(ruta){

    $('#modalTarifaAlquiler').load(ruta,function(){
        $(this).modal('show');
    });
}

function editarTarifaRegistro(ruta){

    cont=0;
    $("form#form_edit_tarifa").submit(function() {
        cont++;
        if(cont<=1){
            var edIdInput =$('input[name="f_id_registro"]').val().trim()
            var edHorasInput =$('input[name="f_ed_horas"]').val().trim()
            var edDiasInput =$('input[name="f_ed_dias"]').val().trim()
            var edPrecioInput =$('input[name="f_precio_registro"]').val().trim()
            console.log(edDiasInput)
            console.log(edHorasInput)
            if(edIdInput){
                $.ajax({
                    url: ruta,
                    data: {
                        'id':edIdInput,
                        'horas':edHorasInput,
                        'dias':edDiasInput,
                        'precio':edPrecioInput
                    },
                    dataType: 'json',
                    success: function (data) {
                        console.log("los datos son")
                        console.log(data)
                        $('form#editarCliente').trigger("reset");
                        location.href=location.href
                        return true
                    }
                });
            }else{
                alert("LAS CONTRASEÑAS DEBEN SER IGUALES")
            }
        return false
        }
    });

}