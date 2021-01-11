function mostrarModalIncidentes(ruta){
    $('#modalIncidentes').load(ruta,function(){
        $(this).modal('show');
    });

}

function mostrarModalDescuentos(ruta){
    $('#modalDescuentos').load(ruta,function(){
        $(this).modal('show');
    });
}

function mostrarModalDetalles(ruta){
    $('#modalOpciones').load(ruta,function(){
        $(this).modal('show');
    });
}
function buscarPorFiltros(ruta){
    var fechaInput=document.getElementById("fecha-input")
    var placaInput=document.getElementById("placa-input")
    var fecha = fechaInput.value
    var placa= placaInput.value
    if(fecha || placa){
        $.ajax({
                url: ruta,
                data: {
                    'fecha':fecha,
                    'placa':placa

                },
                dataType: 'json',
                success: function (data) {
                    console.log("los datos son")
                    console.log(data.lista)
                    mostrarEnTabla(data.lista)
                }
            })
    }else{
        alert("DEBE LLENAR AL MENOS UNO DE LOS CAMPOS DE FILTROS")
    }
}
function mostrarEnTabla(data){
    $("#table-historial > tbody > tr").remove()
    for (item in data){
        $("#table-historial > tbody").append(`
        <tr>
           <td style="width: 90px"  >${data[item].placa}</td>
           <td style="width: 85px" >${data[item].sector}</td>
           <td style="width: 85px" >${data[item].posicion}</td>
           <td style="width: 175px">${data[item].entrada}</td>
           <td style="width: 175px">${data[item].salida}</td>
           <td style="width: 130px;" >
               <button type="button" onclick="mostrarModalIncidentes('${ruta_incidentes+data[item].id}')" class="btn botonIncidente">
                   <i class="fas fa-sign-in-alt margin-boton-seleccionar"></i>VER
               </button>
           </td>
           <td style="width: 130px;"  >
               <button type="button" onclick="mostrarModalDescuentos('${ruta_descuentos+data[item].id}')" class="btn botonDescuentos">
                   <i class="fas fa-sign-in-alt margin-boton-seleccionar"></i>VER
               </button>
           </td>
           <td style="width: 130px" >
               <button type="button" onclick="mostrarModalDetalles('${ruta_detalles+data[item].id}')" class="btn botonSeleccionar">
                   <i class="fas fa-sign-in-alt margin-boton-seleccionar"></i>SELECCIONAR
               </button>
           </td>
   </tr>
        
        `)
    }
}