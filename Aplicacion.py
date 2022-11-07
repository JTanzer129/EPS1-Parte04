import sqlite3 as sql
#Metodos del menu
def mostrar_menu(opciones):

    print('Menu opciones:')
    for clave in sorted(opciones):
        print(f'{clave}) {opciones[clave][0]}')           

def leer_opcion(opciones):
    while (a := input('Opcion:')) not in opciones:
        print('Opcion incorrecta, vuelva a intentarlo')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones,opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion,opciones)
        print() # se imprime una linea en blanco para clarificar la salida en pantalla

def menu_principal():
    opciones = {
        '1':('Registrar', registrar),
        '2':('Eliminar',eliminar),
        '3':('Editar', editar),
        '4':('Listar', listar),      
        '5':('Salir', salir)
    }       

    generar_menu(opciones,'5')
#---------------------------------------------------------------------------------------

#Metodos de opciones


def registrar():
    Codigo = input('Ingrese el codigo del nuevo producto: ')
    Nombre = input('Ingrese el nombre del nuevo prodcuto: ')
    Precio = input('Ingrese el Precio del nuevo producto: ')
    nuevo_producto(Codigo,Nombre,Precio)
    print('Producto registrado exitosamente')
def eliminar():
    eliminar_producto()
    print('Producto Eliminado exitosamente')
def editar():
    editar_producto()
    print('Produto editado correctamente')
def listar():
    print('Lista de Productos:\nidpro\tcodigo\tnombre\tprecio ')
    listar_productos()
def salir():
    print('Saliendo del sistema')

#-------------------------------------------------------
#Metodos Base de Datos
def crearBD():
    conn = sql.connect("Arones_Bravo_Huanuco_Nanquen_almacen.db")
    conn.commit()
    conn.close()
    
def crearTabla():
    conn = sql.connect("Arones_Bravo_Huanuco_Nanquen_almacen.db")
    cursor = conn.cursor()
    cursor.execute(
    """CREATE TABLE Producto (
        idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo text,
        nombre text,
        precio float 
    )"""
    )
    conn.commit()
    conn.close()

def nuevo_producto(codigo,nombre ,precio):
    conn = sql.connect("Arones_Bravo_Huanuco_Nanquen_almacen.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO Producto(codigo,nombre,precio) VALUES ('{codigo}','{nombre}',{precio})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def registrar10(lista_productos):
    conn = sql.connect("Arones_Bravo_Huanuco_Nanquen_almacen.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO Producto(codigo,nombre,precio) VALUES (?,?,?)"
    cursor.executemany(instruccion,lista_productos)
    conn.commit()
    conn.close()



def listar_productos():
    conn = sql.connect("Arones_Bravo_Huanuco_Nanquen_almacen.db")
    cursor = conn.cursor()
    instruccion = f"SELECT idproducto FROM Producto"
    cursor.execute(instruccion)
    listid = cursor.fetchall()
    instruccion = f"SELECT codigo FROM Producto"
    cursor.execute(instruccion)
    listcod = cursor.fetchall()
    instruccion = f"SELECT nombre FROM Producto"
    cursor.execute(instruccion)
    listna = cursor.fetchall()
    instruccion = f"SELECT precio FROM Producto"
    cursor.execute(instruccion)
    listpr = cursor.fetchall()
    conn.commit()
    conn.close()
    i = 0
    while i < len(listid):
        print(f'{listid[i][0]}\t{listcod[i][0]}\t{listna[i][0]}\t{listpr[i][0]}')       
        i +=1   

def eliminar_producto():
    id = input('Ingrese el id del producto a eliminar: ')
    conn = sql.connect("Arones_Bravo_Huanuco_Nanquen_almacen.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM Producto WHERE idproducto='{id}'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def editar_producto():
    id = input('Ingrese el id del producto a editar: ')
    
    Cnew=input('Nuevo codigo: ')
    Nnew=input('Nuevo nombre: ')
    Pnew=input('Nuevo precio: ')

    conn = sql.connect("Arones_Bravo_Huanuco_Nanquen_almacen.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE Producto SET codigo = '{Cnew}', nombre = '{Nnew}',precio = '{Pnew}' WHERE idproducto ='{id}'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()    





#-------------------------------------------------------------------------------------------
if __name__ == "__main__" :
    
    #crearBD()
    #crearTabla()
    menu_principal()
