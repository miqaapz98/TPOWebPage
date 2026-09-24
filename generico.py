from mysql.connector import Error
import mysql.connector
class Generico():
    def __init__(self):  
        try:
            self.conexion= mysql.connector.connect(
                host = '127.0.0.1', 
                port = 3306,
                user= 'root',
                password = '',
                database = 'bikes'
            )
        except Error as ex: # error de mysql
            print('No se pudo conectar la conexion:{0}'.format(ex))
#LISTAR BICICLETAS-------------------------------------------------------------------------------
    def listarBicicletas(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM bicicletas ")
                respuesta = cursor.fetchall()
                return respuesta
            except Error as ex:
                print('Error  en el intento : {0}'.format(ex))
#LISTAR VENTAS ---------------------------------------------------------------------------------------------
    def listarVentas(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM ventas ORDER BY fecha_Venta DESC")
                respuesta = cursor.fetchall()
                return respuesta
            except Error as ex:
                print('Error  en el intento : {0}'.format(ex))
#REGISTRAR ALUMNOS-----------------------------------------------------------------------------------------
    def registrarVentas(self,venta):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql = ("INSERT INTO ventas ( id_Venta,dni, nombre, apellido, telef, cod_Bici, fecha_Venta, precio) values({0},{1},'{2}','{3}',{4},'{5}','{6}',{7})") 
                cursor.execute(sql.format(venta[0],venta[1],venta[2],venta[3],venta[4],venta[5],venta[6],venta[7]))
                self.conexion.commit()
                print('La compra se registro correctamente')
            except Error as ex:
                print('Error  en el intento : {0}'.format(ex))    

#ElIMINAR VENTAS-------------------------------------------------------------------------------------------
    def eliminarVentas(self,ventaEliminar):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql = 'DELETE FROM ventas WHERE id_Venta = {0}' 
                cursor.execute(sql.format(ventaEliminar))
                self.conexion.commit()
                print('La venta se ha eliminado')
            except Error as ex:
                print('Error en el intento :{0}'.format(ex))
#ACTUALIZAR VENTAS-------------------------------------------------------------------------------
    def actualizarVentas(self,venta):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql = "UPDATE ventas SET dni={1}, nombre='{2}',apellido='{3}',telef={4},cod_Bici='{5},fecha_Venta='{6}',precio={7} where id_Venta={0}"   
                cursor.execute(sql.format(venta[0],venta[1],venta[2],venta[3],venta[4],venta[5],venta[6],venta[7]))
                self.conexion.commit()
                print('Se actualizo correctamente')
            except Error as ex:
                print('Error  en el intento : {0}'.format(ex))
