from generico import Generico
from metodos import Metodos

def menu():
    while True :
        print(""" \n ***********************     MENU PRINCIPAL   ************************
\t1.Mostrar catalogo
\t2. Listar ventas
\t3. Registrar venta
\t4. Editar venta
\t5. Eliminar ventas 
\t6. Salir""")
        opcion=int(input(' \nIngrese una de las opciones : '))
        if opcion<1 or opcion > 6: print('Opcion invalida. Ingrese una opcion correcta ')
        if opcion == 6:
            print('¡Que tenga buen dia! \n Finaliza VENTAS DE BIKE. ')
            break
        else: opciones(opcion)

def opciones(opcion):
    generico = Generico()
    metodos = Metodos()
    if opcion ==1:
        print(""" *************************   Catalogo de las Bicicletas   *********************** """)
        bici=generico.listarBicicletas()
        metodos.listarBicis(bici)
    if opcion == 2: #-----------------------------------ListarAlumnos-----------------------------------------------
        print("\n\t LISTA DE VENTAS SEGUN FECHAS ")
        try:
            venta=generico.listarVentas() 
            if len(venta)>0:
                metodos.listarVentas(venta)
            else:
                print('No se encuentran registros')
        except:
            print('Ocurrio un error')
    if opcion == 3: #-------------------------------------------Registrar-----------------------------------------
        bici=generico.listarBicicletas()
        metodos.listarBicis(bici)
        venta = metodos.registrarVentas()
        try:
            generico.registrarVentas(venta)
        except:
            print('Ocurrior un error')
    if opcion == 4: #--------------------------ActualizarAlumnos---------------------------------------------
        venta=generico.listarVentas()
        try:
            if len(venta) > 0:
                venta=metodos.actualizarVentas(venta)
                if venta:
                    generico.actualizarVentas(venta)
                else:
                    print('No se encontro el id de la venta desea modificar')
            else: print('No se encontro venta')
        except:
            print('No es posible modificar. Vuelve al menu principal')
    if opcion == 5: #--------------------------EliminarAlumnos---------------------------------------
        try:
            venta=generico.listarVentas()
            if len(venta)>0:
                venta_Eliminar=metodos.eliminarVentas(venta)
                if venta_Eliminar != "":
                    generico.eliminarVentas(venta_Eliminar)
                else:
                    print('No se encontro id de la venta')
            else:
                print('No hay registro de ventas')
        except:
            print('Ocurrio un error al eliminar o no existe id de venta')
menu()