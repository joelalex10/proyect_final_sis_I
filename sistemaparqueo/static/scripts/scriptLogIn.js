function validarUsuario(ruta){


    var tipoUsuarioSelect = document.getElementById("user_type")
    var tipoUsuario = tipoUsuarioSelect.value

    var nombreUsuarioInput = document.getElementById("user_name")
    var nombreUsuario = nombreUsuarioInput.value

    var passwordInput = document.getElementById("password")
    var password = passwordInput.value

    if(tipoUsuario && nombreUsuario &&  password){
        $.ajax({
            url: ruta,
            data: {
                'user_name':nombreUsuario,
                'password':password,
                'user_type':tipoUsuario
            },
            dataType: 'json',
            success: function (data) {

                if(data.id_usuario){
                    if(tipoUsuario==1){
                        location.href = data.id_usuario + rutaMenuAdmin

                    }else if(tipoUsuario==2){

                        location.href = data.id_usuario + rutaMenuEmpleado
                    }
                }else{
                    cont++
                    console.log(cont)
                    alert("DATOS INCORRECTOS")
                    if(cont>=3){
                        location.href='about:blank'
                        document.write("USTED EXCEDIO MAS DE TRES INTENTOS")
                    }
                }
            }
        })
    }else{
        alert('Debe llenar todos los campos')
    }
}