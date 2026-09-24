from flask import Flask , render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

import random

app = Flask(__name__)

#mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bikes'
mysql = MySQL(app)

#settings
app.secret_key = 'mysecretkey'

@app.route('/')
def home():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM bicicletas')
    dato=cur.fetchall()
    cur.execute('SELECT * from ventas')
    data=cur.fetchall()
    return render_template('home.html', bici=dato, ventas=data,)


@app.route('/agregarVentas', methods=['POST'])
def agregarVentas():
    if request.method == 'POST':
        id_Venta=random.randint(1,100)
        dni=request.form['dni']
        nombre=request.form['nombre']
        apellido=request.form['apellido']
        telefono=request.form['telef']
        cod_Bici=request.form['cod_Bici']
        fecha=request.form['fecha_Venta']
        precio=request.form['precio']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO ventas (id_Venta,dni,nombre,apellido,telef,cod_Bici,fecha_Venta,precio) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(id_Venta,dni,nombre,apellido,telefono,cod_Bici,fecha,precio))
        mysql.connection.commit()
        flash('Los datos se agregaron correctamente')
        return redirect(url_for('home'))

@app.route('/eliminarVenta/<string:id_Venta>')
def eliminarVentas(id_Venta):
    cur=mysql.connection.cursor()
    cur.execute('DELETE FROM ventas WHERE id_venta={0}'.format(id_Venta))
    mysql.connection.commit()
    flash('La venta eliminado')
    return redirect(url_for('home'))

@app.route('/editVenta/<id_Venta>')
def editar(id_Venta):
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM ventas WHERE id_Venta=%s'% (id_Venta))
    datos=cur.fetchall()
    return render_template('editar.html',venta=datos[0])


@app.route('/actualizaVenta/<id>',methods = ['POST'])
def actualizar(id):
    if request.method == 'POST':
        dni=request.form['dni']
        nombre=request.form['nombre']
        apellido=request.form['apellido']
        telefono=request.form['telef']
        cod_Bici=request.form['cod_Bici']
        fecha=request.form['fecha_Venta']
        precio=request.form['precio']
        cur=mysql.connection.cursor()
        cur.execute("""
            UPDATE ventas
            SET dni=%s,
                nombre = %s,
                apellido = %s,
                telef = %s,
                cod_Bici = %s,
                fecha_Venta =%s,
                precio = %s
            WHERE id_Venta= %s
        """ ,(dni,nombre,apellido,telefono,cod_Bici ,fecha,precio, id))
        mysql.connection.commit()
        flash('¡VENTA EDITADA!')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port = 5000, debug=True)