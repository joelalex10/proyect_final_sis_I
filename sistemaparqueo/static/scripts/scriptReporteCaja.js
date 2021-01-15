

function buscarPorFiltros (ruta){
    cont=0;
    $("form#buscar_filtros").submit(function() {
        cont++;
        if(cont<=1){
            console.log("EL CONTADOR ES: "+cont)
            var mesInput = $('input[name="buscar-mes"]').val().trim()
            if (mesInput) {
            $.ajax({
                url: ruta,
                data: {
                    'mes':mesInput
                },
                dataType: 'json',
                success: function (data) {

                    mostrarEnTabla(data.lista)
                    mostrarEnTablaTotal(data.sumtotal)
                }
            })
            } else {
            alert("All fields must have viewGestionDeEmpleados valid value.");
        }
        $('form#buscar_filtros').trigger("reset");
        return false
        }
    })
}
function mostrarEnTablaTotal(data){
    $("#cajaTotal > tbody > tr").remove()
    for(var item in data){

        if(data[item].diferencias<1){
            $("#cajaTotal > tbody").append(`
                <tr>
                    <td style="width: 200px"  >${data[item].monto_apertura} Bs.</td>
                    <td style="width: 200px"  >${data[item].monto_facturado} Bs.</td>
                    
                    <td style="width: 200px" >${data[item].monto_clausura} Bs.</td>
                    <td style="width: 150px; color: green">
                        ${data[item].diferencias.toFixed(1)} Bs.
                    </td>    
                </tr>
                `)
        }else{
            $("#cajaTotal > tbody").append(`
                <tr>
                    <td style="width: 200px"  >${data[item].monto_apertura} Bs.</td>
                    <td style="width: 200px"  >${data[item].monto_facturado} Bs.</td>
                    
                    <td style="width: 200px" >${data[item].monto_clausura} Bs.</td>
                    <td style="width: 150px; color: red">
                        ${data[item].diferencias.toFixed(1)} Bs.
                    </td>    
                </tr>
                `)
        }

    }
}

function mostrarEnTabla(data){
    $("#productoTable > tbody > tr").remove()
    for(var item in data){
        if(data[item].diferencias<1){
            $("#productoTable > tbody").append(
            `
            <tr>
                <td style="width: 150px"  >${data[item].fecha}</td>
                <td style="width: 275px" >${data[item].nombre}</td>
                <td style="width: 225px" >${data[item].monto_apertura} Bs.</td>
                <td style="width: 225px" >${data[item].monto_facturado} Bs.</td>
                <td style="width: 225px">${data[item].monto_clausura} Bs.</td>
                    <td style="width: 100px; color: green">
                    ${data[item].diferencias.toFixed(1)} Bs.
                    </td>
            </tr>
            `)
        }else{
            $("#productoTable > tbody").append(
            `
            <tr>
                <td style="width: 150px"  >${data[item].fecha}</td>
                <td style="width: 275px" >${data[item].nombre}</td>
                <td style="width: 225px" >${data[item].monto_apertura} Bs.</td>
                <td style="width: 225px" >${data[item].monto_facturado} Bs.</td>
                <td style="width: 225px">${data[item].monto_clausura} Bs.</td>
                    <td style="width: 100px; color: red">
                    ${data[item].diferencias.toFixed(1)} Bs.
                    </td>
            </tr>
            `)
        }

    }
}