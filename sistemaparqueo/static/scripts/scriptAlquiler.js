function buscarAlquilerPorFiltros(ruta,id_usuario){
    var ciInput = document.getElementById("input-ci-control")
    var ci = ciInput.value
    if(ci){
        $.ajax({
            url: ruta,
            data: {
                'ci':ci,
            },
            dataType: 'json',
            success: function (data) {
                console.log(data.lista)
                mostrarDatosEnTabla(data.lista,id_usuario)
            }
        })
    }
}
function mostrarDatosEnTabla(data,id){
    $("#tabla-control-alquileres > tbody > tr").remove()
    for(item in data){
        $("#tabla-control-alquileres > tbody").append(`
        <tr>
            <td style="width: 200px" >${data[item].ci}</td>
            <td style="width: 300px" >${data[item].nombre}</td>
            <td style="width: 200px" >${data[item].placa}</td>
            <td style="width: 125px" >${data[item].estado}</td>
            <td style="width: 90px">
                <a href="/${id+ruta_estados+data[item].id}">
                    <button class=" btn botonSeleccionar"><i class="fas fa-sign-in-alt margin-boton-seleccionar"></i>VER PAGOS</button>
                </a>
            </td>
        </tr>
        `)
    }
}