function agregarEmpleado (ruta){
    cont=0;
    $("form#registro_usuarios").submit(function() {
        cont++;
        if(cont<=1){
            var ciInput =$('input[name="form_ci"]').val().trim()
            var nombreInput =$('input[name="form_nombre"]').val().trim()
            var usuarioInput =$('input[name="form_usuario"]').val().trim()
            var passwordInput =$('input[name="form_password"]').val().trim()
            var passwordConfirmInput =$('input[name="form_password_confirm"]').val().trim()
            var horaIngresoInput =$('input[name="form_hora_ingreso"]').val().trim()
            var horaSalidaInput =$('input[name="form_hora_salida"]').val().trim()

            if(passwordInput==passwordConfirmInput){
                $.ajax({
                    url: ruta,
                    data: {
                        'ci':ciInput,
                        'nombre':nombreInput,
                        'usuario':usuarioInput,
                        'password':passwordInput,
                        'horaIngreso':horaIngresoInput,
                        'horaSalida':horaSalidaInput
                    },
                    dataType: 'json',
                    success: function (data) {
                        console.log("los datos son")
                        console.log(data)
                        $('form#registro_usuarios').trigger("reset");
                        location.href=location.href
                        return true
                    }
                });
            }else{
                alert("LAS CONTRASEÑAS DEBEN CONICIDIR")
            }
        return false
        }
    });
}

function abrirModalEdicionCliente(ruta) {
    $('#edicionCliente').load(ruta,function(){
        $(this).modal('show');
    });
}

function editarDatosCliente(ruta){

    cont=0;
    $("form#editarCliente").submit(function() {
        cont++;
        if(cont<=1){
            var idInput =$('input[name="form_id"]').val().trim()
            var ciInput =$('input[name="forms_ci"]').val().trim()
            console.log(idInput)
            console.log(ciInput)

            var nombreInput =$('input[name="forms_nombre"]').val().trim()
            var usuarioInput =$('input[name="forms_usuario"]').val().trim()
            var passwordInput =$('input[name="forms_password"]').val().trim()
            var passwordConfirmInput =$('input[name="forms_password_confirm"]').val().trim()
            var horaIngresoInput =$('input[name="forms_hora_ingreso"]').val().trim()
            var horaSalidaInput =$('input[name="forms_hora_salida"]').val().trim()

            if(passwordInput == passwordConfirmInput){
                $.ajax({
                    url: ruta,
                    data: {
                        'id':idInput,
                        'ci':ciInput,
                        'nombre':nombreInput,
                        'usuario':usuarioInput,
                        'password':passwordInput,
                        'horaIngreso':horaIngresoInput,
                        'horaSalida':horaSalidaInput
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