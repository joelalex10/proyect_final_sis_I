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

function abrirCaja(ruta){

    var totalInput = document.getElementById("total")
    var total= totalInput.innerText
    console.log(total)
    var fecha_apertura=obtenerFechaActual()
    var hora_apertura=obtenerHoraActual()
    console.log(hora_apertura)
    $('#ModalRegistrar').load(ruta,function(){
        $(this).modal('show');
        var fecha=document.getElementById('fecha_apertura');
        fecha.innerHTML=fecha_apertura

        var hora=document.getElementById('hora_apertura');
        hora.innerHTML=hora_apertura

        var monto=document.getElementById('monto_apertura');
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

function registrarApertura(ruta,ruta2){

    console.log("datos")
    var fechaText=document.getElementById('fecha_apertura');
    console.log("la fecha es: "+fechaText.innerHTML)
    var horaText=document.getElementById('hora_apertura');
    console.log("la hora es: "+horaText.innerHTML)
    var montoText=document.getElementById('monto_apertura');
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
            "hora_apertura":hora,
            "monto_apertura":monto,
            "id_usuario":id_usuario,
            "fecha":fecha
        },
        dataType: 'json',
        success: function (data) {
            alert('APERTURA DE CAJA REALIZADA CON EXITO')
            location.href=ruta2
        }
    })



}