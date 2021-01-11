function valores(ruta){
    var bill200 = 200* obtenerValor(document.getElementById("bill-200"))
    var bill100 = 100* obtenerValor(document.getElementById("bill-100"))
    var bill50 = 50* obtenerValor(document.getElementById("bill-50"))
    var bill20 = 20* obtenerValor(document.getElementById("bill-20"))
    var bill10 = 10* obtenerValor(document.getElementById("bill-10"))
    sum=bill200 + bill100 + bill50 + bill20 + bill10
    document.getElementById("efectivo-billetes").innerHTML=sum + " Bs."

    var mon5 = 5* obtenerValor(document.getElementById("mon-5"))
    var mon2 = 2* obtenerValor(document.getElementById("mon-2"))
    var mon1 = obtenerValor(document.getElementById("mon-1"))
    var mon05 = 0.5* obtenerValor(document.getElementById("mon-0.5"))
    var mon02 = 0.2* obtenerValor(document.getElementById("mon-0.2"))
    var mon01 = 0.1* obtenerValor(document.getElementById("mon-0.1"))

    sumMonedas=mon5 + mon2 + mon1 + mon05 + mon02 + mon01
    document.getElementById("efectivo-monedas").innerHTML=sumMonedas.toFixed(2) + " Bs."
    sumTotal = sum+sumMonedas
    document.getElementById("total").innerHTML=sumTotal.toFixed(2)

    var aperturaInput=document.getElementById("input-monto-apertura")
    var apertura=parseFloat(aperturaInput.value)

    var facturadoInput=document.getElementById("input-facturado")
    var facturado=parseFloat(facturadoInput.value)

    var diferenciasInput= document.getElementById("input-diferencia")
    diferencias = apertura + facturado - sumTotal.toFixed(2)
    diferenciasInput.value= diferencias.toFixed(2)



    $.ajax({
        url: ruta,
        data: {
            'total':sumTotal,
        },
        dataType: 'json',
        success: function (data) {
            document.getElementById("literal_valor").innerHTML=data.literal
        }
    })
}

function obtenerValor(element){
    if(element.value==false){
        element.value=0
    }
    return parseInt(element.value)
}

function limpiar(){
    document.getElementById("bill-200").value=0
    document.getElementById("bill-100").value=0
    document.getElementById("bill-50").value=0
    document.getElementById("bill-20").value=0
    document.getElementById("bill-10").value=0
    document.getElementById("mon-5").value=0
    document.getElementById("mon-2").value=0
    document.getElementById("mon-1").value=0
    document.getElementById("mon-0.5").value=0
    document.getElementById("mon-0.2").value=0
    document.getElementById("mon-0.1").value=0

    document.getElementById("efectivo-monedas").innerHTML=0 + " Bs."
    document.getElementById("efectivo-billetes").innerHTML=0 + " Bs."
    document.getElementById("total").innerHTML=0
    document.getElementById("literal_valor").innerHTML="CON 00/100 BOLIVIANOS"
}


function cerrarCaja(ruta){

    $('#ModalCierreCaja').load(ruta,function(){
        $(this).modal('show');

        var totalInput = document.getElementById("total")
        var total= totalInput.innerText
        var fecha_apertura=obtenerFechaActual()
        var hora_apertura=obtenerHoraActual()

        var fecha=document.getElementById('fecha_clausura');
        fecha.innerHTML=fecha_apertura

        var hora=document.getElementById('hora_clausura');
        hora.innerHTML=hora_apertura

        var monto=document.getElementById('monto_clausura');
        monto.innerHTML=total
    });
}
function obtenerFechaActual(){
    var hoy = new Date()
    var fecha = hoy.getFullYear() + '-' + (hoy.getMonth() +1) + '-' + hoy.getDate()
    return (fecha)

}
function obtenerHoraActual(){
    var hoy = new Date()
    var hora = hoy.getHours() + ':' + hoy.getMinutes() + ':'+hoy.getSeconds()
    return (hora)
}

function registrarClausura(ruta,ruta2){
    console.log("datos")
    var fechaText=document.getElementById('fecha_clausura');
    console.log("la fecha es: "+fechaText.innerHTML)
    var horaText=document.getElementById('hora_clausura');
    console.log("la hora es: "+horaText.innerHTML)
    var montoText=document.getElementById('monto_clausura');
    console.log("el monto es: "+montoText.innerHTML)
    var id_usuario_Text=document.getElementById('id_usuario');
    console.log("el usuario es: "+id_usuario_Text.value)

    var fecha=fechaText.innerHTML
    var hora=horaText.innerHTML
    var monto=parseFloat(montoText.innerHTML).toFixed(2)
    var id_usuario=id_usuario_Text.value

    $.ajax({
        url: ruta,
        data: {
            "hora_clausura":hora,
            "monto_clausura":monto,
            "id_usuario":id_usuario,
            "fecha":fecha
        },
        dataType: 'json',
        success: function (data) {
            alert('CIERRE DE CAJA REALIZADA CON EXITO')
            location.href=ruta2
        }
    })
}