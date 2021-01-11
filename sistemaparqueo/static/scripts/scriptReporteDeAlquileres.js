function abrirModalEstadoPagos(ruta){
    $('#modalestadoPagosAlquiler').load(ruta,function(){
        $(this).modal('show');
    });
}

function buscarAlquilerPorFiltros(ruta){
    var ciInput = document.getElementById("search-ci")
    var ci=ciInput.value
    if(ci){
        $.ajax({
            url: ruta,
            data: {
                'ci':ci
            },
            dataType: 'json',
            success: function (data) {
                console.log(data)
                mostrarEnTabla(data.lista)
            }
        })
    }else{
        alert("Debe llenar el campo ci cliente")
    }
}
function mostrarEnTabla(data){
    $("#tablaAlquileres > tbody > tr").remove()
    for(item in data){
        console.log("el")
        console.log(rutaModal + data[item].id)
        $("#tablaAlquileres > tbody").append(`
        <tr>
            <td style="width: 100px" >${data[item].ci}</td>
            <td style="width: 300px">${data[item].nombre}</td>
            <td style="width: 200px">${data[item].placa}</td>

            <td style="width: 200px">${data[item].estado}</td>
            <td style="width: 150px">
                <!--abrirModalEstadoPagos('{% url 'mostrar_estado_pagos' item.id %}')-->
                <button onclick="abrirModalEstadoPagos('${rutaModal+data[item].id}')" class="btn botonSeleccionar"><i class="fas fa-sign-in-alt margin-boton-seleccionar"></i>VER PAGOS</button>
            </td>
        </tr>
        `)

    }

}