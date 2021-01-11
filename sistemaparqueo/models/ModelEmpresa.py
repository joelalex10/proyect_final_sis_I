from db.models import Empresa


class ModelEmpresa():
    def __init__(self):
        self.__nit=None
        self.__nombre=None
        self.__razon_social=None
        self.__direccion=None
        self.__contacto=None

    def set_nit(self,nit):
        self.__nit=nit
    def get_nit(self):
        return self.__nit

    def set_nombre(self,nombre):
        self.__nombre=nombre
    def get_nombre(self):
        return self.__nombre

    def set_razon_social(self,razon_social):
        self.__razon_social=razon_social
    def get_razon_social(self):
        return self.__razon_social

    def set_direccion(self,direccion):
        self.__direccion=direccion
    def get_direccion(self):
        return self.__direccion

    def obtenerDatosPorIdEmpresa(self,empresa_id):
        obj_empresa = Empresa.objects.get(
            id_empresa=empresa_id
        )
        return obj_empresa