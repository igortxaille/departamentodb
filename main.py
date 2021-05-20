import random
import string

import pymysql

from Usuario import Usuario



def MenuCompras():
    print("--> Menú del Departamento de Compras <--\n"
          "----- 1. Crear orden de compra\n"
          "----- 2. Editar orden de compra\n"
          "----- 3. Anular orden de compra\n"
          "----- 4. Salir\n")


def MenuVentas():
    print("--> Menú del Departamento de Ventas <--\n"
          "----- 1. Crear orden de venta\n"
          "----- 2. Editar orden de venta\n"
          "----- 3. Anular orden de venta\n"
          "----- 4. Salir\n")

def MenuProductos():
    print("--> Menú del Departamento de Productos <--\n"
          "----- 1. Crear producto\n"
          "----- 2. Borrar producto\n"
          "----- 4. Salir\n")

def Menu():
    print("1-Iniciar usuario \n"
          "2-Resgistrar usuario \n"
          "3-Salir ")
Menu()
opcion =input("elige: ")
while True:
    if opcion == '1':
        nombre = input("escribe el nombre de usuario: ")
        contraseina = input("escribe la contraseña de usuario: ")
        # Establecemos conexión con la base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="crm", port=3306)
        # Preparar el cursor
        cursor = db.cursor()
        # CONSULTA
        consulta = 'SELECT * FROM usuarios'
        # Ejecutar SQL --> es un string
        cursor.execute(consulta)

        # Recoger más de un dato con fetchall()
        # Resultados es una tupla de tuplas --> Guarda una tupla por cada registro de la tabla
        resultados = cursor.fetchall()

        encontrado = False
        for fila in resultados:

            encontrado = True

            if encontrado and fila[1] == contraseina:
                print("entra")
                if encontrado and fila[2] == "productos":

                    MenuProductos()
                    elige = input("elige: ")
                    while True :
                        if elige == '1':
                            proveedor = input("escribe el nombre del proveedor ")
                            producto = input("escribe el nombre del producto ")
                            precio = input("escribe el precio del producto ")

                            # Conexión a base de datos
                            db = pymysql.connect(host="127.0.0.1", user="root", db="crm", port=3306)
                            # Preparar el cursor
                            cursor = db.cursor()
                            # Consulta SQL para insertar datos de un empleado

                            sql = "INSERT INTO productos(producto,precio,proveedor) VALUES ('" + producto + "','precio','" + proveedor + "')"

                            try:
                                # Ejecutar el comando SQL
                                cursor.execute(sql)
                                # Aceptar cambios con commit
                                db.commit()
                            except:
                                # Rollback en caso de haber algún error
                                db.rollback()
                            exit()
                        elif elige == '2':
                            # Establecemos conexión con la base de datos
                            db = pymysql.connect(host="127.0.0.1", user="root", db="crm", port=3306)
                            # Preparar el cursor
                            cursor = db.cursor()
                            # CONSULTA
                            consulta = 'SELECT * FROM productos'
                            # Ejecutar SQL --> es un string
                            cursor.execute(consulta)

                            # Recoger más de un dato con fetchall()
                            # Resultados es una tupla de tuplas --> Guarda una tupla por cada registro de la tabla
                            resultados = cursor.fetchall()

                            encontrado = False

                            print(resultados)
                            opcion = int(input("elige un producto: "))
                            print(opcion[0])
                            sql = "Delete from productos WHERE id = 'opcion' "

                            try:
                                # Ejecutar el comando SQL
                                cursor.execute(sql)
                                # Aceptar cambios con commit
                                db.commit()
                            except:
                                # Rollback en caso de haber algún error
                                db.rollback()
                            exit()

                        elif elige == '4':
                            Menu()

                if encontrado and fila[2] == "compras":
                    MenuCompras()
                    elige = input("elige opcion: ")
                    while True:
                        if elige == '1':
                            id_productos = input("escribe el id del prodcuto ")
                            orden = input("escribe el nombre de la orden ")

                            # Consulta SQL para insertar datos de un empleado

                            sql = "INSERT INTO compras(id_productos,orden) VALUES (' id_productos ',' " + orden + "')"

                            try:
                                # Ejecutar el comando SQL
                                cursor.execute(sql)
                                # Aceptar cambios con commit
                                db.commit()
                            except:
                                # Rollback en caso de haber algún error
                                db.rollback()

                            MenuCompras()
                        if elige == '2':
                            # Establecemos conexión con la base de datos
                            db = pymysql.connect(host="127.0.0.1", user="root", db="crm", port=3306)
                            # Preparar el cursor
                            cursor = db.cursor()
                            # CONSULTA
                            consulta = 'SELECT * FROM compras'
                            # Ejecutar SQL --> es un string
                            cursor.execute(consulta)

                            # Recoger más de un dato con fetchall()
                            # Resultados es una tupla de tuplas --> Guarda una tupla por cada registro de la tabla
                            resultados = cursor.fetchall()

                            encontrado = False

                            for fila in resultados:
                                opcion = int(input("elige una compra: "))

                            editar = input(" ¿ que campo quieres editar? 1,2,3: ")
                            if editar == '1':
                                id_productos = fila[0]
                                orden = fila[1]
                                id_orden = fila[2]
                                cambio = int(input("introduce nuevo id "))
                                sql = "UPDATE compras SET orden ='cambio' WHERE id_productos = 'id_productos'"

                                try:
                                    # Ejecutar el comando SQL
                                    cursor.execute(sql)
                                    # Aceptar cambios con commit
                                    db.commit()
                                except:
                                    # Rollback en caso de haber algún error
                                    db.rollback()
                                MenuCompras()
                            if editar == '2':
                                id_productos = fila[0]
                                orden = fila[1]
                                id_orden = fila[2]
                                cambio = int(input("introduce nuevo id "))
                                sql = "UPDATE compras SET id_orden ='[cambio]' WHERE id_productos = 'id_productos'"

                                try:
                                    # Ejecutar el comando SQL
                                    cursor.execute(sql)
                                    # Aceptar cambios con commit
                                    db.commit()
                                except:
                                    # Rollback en caso de haber algún error
                                    db.rollback()
                                MenuCompras()
                        if elige == '3':
                            # Establecemos conexión con la base de datos
                            db = pymysql.connect(host="127.0.0.1", user="root", db="crm", port=3306)
                            # Preparar el cursor
                            cursor = db.cursor()
                            # CONSULTA
                            consulta = 'SELECT * FROM compras'
                            # Ejecutar SQL --> es un string
                            cursor.execute(consulta)

                            # Recoger más de un dato con fetchall()
                            # Resultados es una tupla de tuplas --> Guarda una tupla por cada registro de la tabla
                            resultados = cursor.fetchall()

                            encontrado = False

                            opcion = int(input("elige una compra: "))
                            id_productos = fila[0]
                            orden = fila[1]
                            id_orden = fila[2]
                            sql = "Delete from compras WHERE id_productos = 'opcion'"

                            try:
                                # Ejecutar el comando SQL
                                cursor.execute(sql)
                                # Aceptar cambios con commit
                                db.commit()
                            except:
                                # Rollback en caso de haber algún error
                                db.rollback()
                            MenuCompras()
                        if elige == '4':
                            Menu()

                if encontrado and fila[2] == "ventas":
                    MenuVentas()
                    elige = input("elige opcion: ")
                    while True:
                        if elige == '1':
                            id_productos = input("escribe el id del prodcuto: ")
                            id_cliente = input("escribe el id del cliente: ")
                            factura = input("nombre de la factura: ")

                            # Conexión a base de datos
                            db = pymysql.connect(host="127.0.0.1", user="root", db="crm", port=3306)
                            # Preparar el cursor
                            cursor = db.cursor()
                            # Consulta SQL para insertar datos de un empleado

                            sql = "INSERT INTO ventas(producto,id_cliente,factura) VALUES (' id_productos ','id_cliente','" + factura + "')"

                            try:
                                # Ejecutar el comando SQL
                                cursor.execute(sql)
                                # Aceptar cambios con commit
                                db.commit()
                            except:
                                # Rollback en caso de haber algún error
                                db.rollback()

                            MenuVentas()
                        elif elige == '2':
                            # Establecemos conexión con la base de datos
                            db = pymysql.connect(host="127.0.0.1", user="root", db="crm", port=3306)
                            # Preparar el cursor
                            cursor = db.cursor()
                            # CONSULTA
                            consulta = 'SELECT * FROM ventas'
                            # Ejecutar SQL --> es un string
                            cursor.execute(consulta)

                            # Recoger más de un dato con fetchall()
                            # Resultados es una tupla de tuplas --> Guarda una tupla por cada registro de la tabla
                            resultados = cursor.fetchall()

                            encontrado = False

                            for fila in resultados:
                                opcion = int(input("elige una venta: "))

                            editar = input(" ¿ que campo quieres editar? 1,2,3: ")
                            if editar == '1':
                                id_productos = fila[0]
                                id_venta = fila[1]
                                id_cliente = fila[2]
                                factura = fila[3]
                                cambio = int(input("introduce nuevo id de venta"))
                                sql = "UPDATE ventas SET id_venta ='cambio' WHERE id_cliente = 'id_cliente'"

                                try:
                                    # Ejecutar el comando SQL
                                    cursor.execute(sql)
                                    # Aceptar cambios con commit
                                    db.commit()
                                except:
                                    # Rollback en caso de haber algún error
                                    db.rollback()
                                MenuVentas()
                            if editar == '2':
                                id_productos = fila[0]
                                id_venta = fila[1]
                                id_cliente = fila[2]
                                factura = fila[3]
                                cambio = int(input("introduce nueva factura "))
                                sql = "UPDATE ventas SET factura ='cambio' WHERE id_cliente = 'id_cliente'"

                                try:
                                    # Ejecutar el comando SQL
                                    cursor.execute(sql)
                                    # Aceptar cambios con commit
                                    db.commit()
                                except:
                                    # Rollback en caso de haber algún error
                                    db.rollback()
                                MenuVentas()
                        elif elige == '3':
                            # Establecemos conexión con la base de datos
                            db = pymysql.connect(host="127.0.0.1", user="root", db="crm", port=3306)
                            # Preparar el cursor
                            cursor = db.cursor()
                            # CONSULTA
                            consulta = 'SELECT * FROM ventas'
                            # Ejecutar SQL --> es un string
                            cursor.execute(consulta)

                            # Recoger más de un dato con fetchall()
                            # Resultados es una tupla de tuplas --> Guarda una tupla por cada registro de la tabla
                            resultados = cursor.fetchall()

                            encontrado = False

                            opcion = int(input("elige una venta: "))

                            sql = "Delete from ventas WHERE id_venta = 'opcion'"

                            try:
                                # Ejecutar el comando SQL
                                cursor.execute(sql)
                                # Aceptar cambios con commit
                                db.commit()
                            except:
                                # Rollback en caso de haber algún error
                                db.rollback()
                            MenuVentas()
                        elif opcion == '4':
                            exit()



    elif opcion == '2':
        print("Elige departamento: \n"
              "1/ Productos \n"
              "2/ Compras \n"
              "3/ Ventas")
        try:
            departamento = input("elige: ")
        except:
            print("escribe un numero")
        nombre = input("escribe el nombre de usuario: ")

        lista_usuarios = []
        lista_contraseina = []
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.punctuation
        s4 = string.digits
        if nombre in lista_usuarios:
            print("el usuario ya existe")
        else:
            lista_usuarios.append(nombre)
        longitud = int(input("introduce la longitud de la contraseña"))
        minusculas = input("¿quieres minusculas? si,no").lower()
        mayusculas = input("¿quieres mayusculas? Si,No")
        simbolos = input("¿quieres simbolos? Si,No")
        numeros = input("¿quieres numeros? Si,No")

        if minusculas == "si":
            lista_contraseina.extend(list(s1))
        if mayusculas == "si":
            lista_contraseina.extend(list(s2))
        if simbolos == "si":
            lista_contraseina.extend(list(s3))
        if numeros == "si":
            lista_contraseina.extend(list(s4))
        contraseina = "".join(random.sample(lista_contraseina, longitud))

        depart = ""
        if departamento == '1':
            depart = "productos"
        elif departamento == '2':
            depart = "compras"
        elif departamento == '3':
            depart = "ventas"

        usuario = Usuario(nombre, contraseina, depart)

        # Lista de listas
        datos = [[usuario.nombre, usuario.contraseina, usuario.departamento]]
        print(nombre, ',', contraseina, ',', depart)
        # Conexión a base de datos
        db = pymysql.connect(host="127.0.0.1", user="root", db="crm", port=3306)
        # Preparar el cursor
        cursor = db.cursor()
        # Consulta SQL para insertar datos de un empleado
        sql = "INSERT INTO usuarios(nombre,password,departamento) VALUES ('" + nombre + "','" + contraseina + "','" + depart + "')"

        try:
            # Ejecutar el comando SQL
            cursor.execute(sql)
            # Aceptar cambios con commit
            db.commit()
        except:
            # Rollback en caso de haber algún error
            print("error")
            db.rollback()
    elif opcion == '3':
        exit()