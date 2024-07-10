class Cliente:
    def __init__(self,nombre,direccion,telefono):
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        self.historial_compra=[]

    def actualizar_info(self,direccion=None,telefono=None):
        if direccion:
            self.direccion=direccion
        if telefono:
            self.telefono=telefono

    def registrar_compra(self,compra):
        self.historial_compra.append(compra)

    def mostrar_info(self):
        return f'Cliente: {self.nombre}, Direccion: {self.direccion}, Telefono: {self.telefono}'
        

    