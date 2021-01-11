from datetime import datetime

from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

from db.models import PagosAlquileres, RegistroCaja
from sistemaparqueo.models.ModelAlquiler import ModelAlquiler
from sistemaparqueo.models.ModelEmpresa import ModelEmpresa
from sistemaparqueo.models.ModelFactura import ModelFactura


class PagarCuotas(View):
    def get(self,request):
        f_id_cuota=request.GET.get('id_cuota')
        f_estado = request.GET.get('estado')

        print("LOS DATOS SON")
        print(f_estado)

        alquiler =ModelAlquiler()
        id_aquiler,monto_couta=alquiler.pagarCuotaAlquiler(f_id_cuota)

        print("EL ID DE LA CUOTA ES: "+str(f_id_cuota))
        print("EL ID ALQUILER ES: "+str(id_aquiler))
        print("EL MONTO PAGADO ES: " + str(monto_couta))

        empresa = ModelEmpresa()
        obj_empresa = empresa.obtenerDatosPorIdEmpresa(1)
        print (obj_empresa)

        factura = ModelFactura()
        nro_factura = str(id_aquiler)+str(f_id_cuota)
        fecha = format(datetime.now().strftime("%Y%m%d"))
        total = str(int(monto_couta))
        key = 'zZ7Z]xssKqkEf_6K9uH(EcV+%x+u[Cca9T%+_$kiLjT8(zr3T9b5Fx2xG-D+_EBS'
        codigo = factura.generarCodigoControl(str(obj_empresa.autorizacion),str(obj_empresa.nit),nro_factura,fecha,total,key)

        print("EL CODIGO ES")
        print(codigo)
        factura.set_codigo_control(codigo)
        factura.set_numero_factura(nro_factura)
        obj_factura = factura.agregarFacturaAlquiler(id_aquiler)

        data = {'id_alquiler':id_aquiler, 'id_cuota':f_id_cuota, 'id_factura':obj_factura.id_factura}

        return JsonResponse(data)

class ImprimirFacturaPagosAlquileres(View):
    def get(self, request, *args, **kwargs):
        print(kwargs)
        template = get_template('reportes/facturaAlquiler.html')

        factura = ModelFactura()
        datos = factura.obtenerDatosParaFactura(kwargs['fpk'])
        print(datos)

        context = {'datos_factura':datos[0]}
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="factura_alquiler.pdf"'

        pisStatus = pisa.CreatePDF(
            html, dest=response
        )
        if pisStatus.err:
            return HttpResponse("OCURRIO UN ERROR")
        return response