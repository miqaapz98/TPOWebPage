import random
class Metodos:
    def listarBicis(self,bicicletas):
        contador = 1
        print(" Codigo Bicicleta: | Tipo |Rodado | Marca | Descripcion       | Precio |")
        for bici in bicicletas:
            datos = """
    {}    |  {}   |   {}   |   {}   |   {}   |   {}  """
            print(datos.format(bici[0],bici[1],bici[2],bici[3],bici[4],bici[5]))
            contador += 1
    def listarVentas(self,venta):
        contador = 1
        for vendido in venta:
            datos = """ID_VENTA: {} , DNI: {}, NOMBRE: {}, APELLIDO: {}, TELEFONO: {}, CODIGO BICICLETA: {}
            FECHA DE COMPRA: {}, PRECIO: {} \n"""
            print(datos.format(vendido[0],vendido[1],vendido[2],vendido[3],vendido[4],vendido[5],vendido[6],vendido[7]))
            contador += 1
#----------------------------------------------------REGISTRAR -----------------------------------------
    def registrarVentas(self):
        ID_VENTA=random.randint(1,40)
        dni_Correcto = False
        while (not dni_Correcto):
            DNI = input('Ingresar dni del comprador: ')
            if len(DNI) == 8:
                dni_Correcto = True
            else:
                print('El dni es incorrecto. Dni debe tener 8 digitos.')
        NOMBRE = input('Ingrese el nombre del cliente: ')
        APELLIDO = input('Ingrese el apellido del cliente: ')
        TELEFONO = input('Ingrese el telefono del cliente: ')
        COD_BICI= input('\nIngrese el cod_Bici: ')
        COD_BICI=COD_BICI.upper()
        FECHA_VENTA =input('Ingresa la fecha de la compra: ')
        PRECIO=input('Ingrese el precio: ')
        venta=(ID_VENTA,DNI,NOMBRE,APELLIDO,TELEFONO,COD_BICI,FECHA_VENTA,PRECIO)
        return venta

#---------------------------------------ELIMINAR VENTA---------------------------------------------------------
    def eliminarVentas(self,venta):
        self.listarVentas(venta)
        ventaEliminar =int(input('Ingrese el id de venta que desea eliminar: '))
        for vendido in venta:
            if vendido[0] == ventaEliminar:
                break
        return ventaEliminar

#---------------ACTUALIZAR VENTAS---------
    def actualizarVentas(self,venta):
        self.listarVentas(venta)
        existeId = False
        ventaEditar =int(input('Ingrese el nro de venta que desea editar: '))
        for vendido in venta:
            if vendido[0] == ventaEditar:
                existeId = True
                break
        if existeId:
            dni_Correcto = False
            while (not dni_Correcto):
                DNI = input('Ingresar dni del comprador : ')
                if len(DNI) == 8:
                    dni_Correcto = True
                else:
                    print('El dni es incorrecto. Dni debe tener 8 digitos.')
            NOMBRE = input('Ingrese el nombre del cliente: ')
            APELLIDO = input('Ingrese el apellido del cliente: ')
            TELEFONO = input('Ingrese el telefono del cliente: ')
            COD_BICI= input('\nIngrese el cod_Bici: ')
            COD_BICI=COD_BICI.upper()
            FECHA_VENTA =input('Ingresa la fecha de la compra: ')
            PRECIO=input('Ingrese el precio: ')
            venta=(ventaEditar,DNI,NOMBRE,APELLIDO,TELEFONO,COD_BICI, FECHA_VENTA,PRECIO)
        else:
            print('No existe nro de venta')
        return venta
