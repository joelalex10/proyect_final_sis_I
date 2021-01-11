function pagarCuota(ruta, id, estado){
    console.log(id)
    console.log(estado)
    if(estado=='PAGADO'){
        alert("ESTA CUOTA YA FUE PAGADA")
    }else{
        var status = confirm("SE GENERARA UN RECIBO POR EL PAGO ¿ESTA SEGURO DE PAGAR CUOTA?")
        if(status){
            $.ajax({
                url: ruta,
                data: {
                    'id_cuota':parseInt(id),
                    'estado':estado
                },
                dataType: 'json',
                success: function (data) {
                    data.id_factura
                    var rutaImprimirFactura = '/menuEmpleado/ControlAlquileres/pagarCuotaAlquiler/imprimirFactura/'+ data.id_factura
                    location.href=rutaImprimirFactura

                    alert("SE REGISTRO EL PAGO DE MANERA EXITOSA")
                    location.href = location.href
                }
            })
        }
    }
}