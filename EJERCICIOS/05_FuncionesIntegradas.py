'''
Ejecutar cada una de las funciones
integradas mostradas en el el archivo 
05_FuncionesIntegradas.txt

Nota: Busque la manera para poder ejecutarlas
'''

# Entrada y salida
print("==========funcion entrada y salida==========")

# x = input("Por favor ingrese un numero: ") #Recibe strings
#x_num = int(x)
#print("El numero ingresado fue: ", x_num, type(x_num))

# Ayuda

print("==========funcion ayuda==================")
datos = [1, 2, 3, 4]

print("typo de dato =>", type(datos))  # Retorna el tipo de dato que se usa
print("directorio => ", dir(datos))      # Devuelve las funcionalidades
# help(str)         #Devuelve una ventana interactiva, para salir presionar <q>

print("================Conversiones====================")
conv1 = int(19.9999)   # devuelve el 19
conv2 = float("25")    # devuelve el 25.0
conv3 = bool(1)        # devuelve True
conv4 = list("hola")   # devuelve una lista: ["h", "o", "l", "a"]
conv5 = tuple([1, 2, 3])  # devuelve una tupla: (1,2,3)
conv6 = dict([(1, "uno"), (2, "dos"), (3, "tres")])
conv7 = set("abcdefghijklmnopqrstuvwxyz")  # Devuelve {"a", "b", "c",..."z"}

# Conversiones entre sistemas numericos
print("entero 11 a binario     ", bin(11))
print("entero 11 a octal       ", oct(11))
print("entero 11 a hexadecimal ", hex(11))

print("binario 111 a  entero     ", "?")
print("octal 88 a  entero        ", "?")
print("hexadecimal AA a  entero  ", "?")

print("================Secuencias====================")

rango = range(1, 10, 1)  # Esto es una secuencia range(inicio, fin, salto)
print(list(rango))  # Se debe convertir a lista para poder imprimir el rango
# Devuelve [1,2,3,4,5,6,7,8,9] el 10 no se toma

"Crear las secuencias mostradas  =>"
"   10,  13,  16,  19, ..., 100  "
" -100, -99, -98, -97, ..., 7, 8, 9, 10  "
"  -10,  -9,  -8,  -7, ..., 0  "
print("------------")
print(list(range(10, 101, 3)))
print(list(range(-100, 11, 1)))  # por defecto el salto es 1
print(list(range(-10, 1)))  # Se puede omitir si el salto es 1


####################################################


"""Realizar las siguientes conversiones:
     a) Los decimales 512, 8, 128         ==>   a binario, octal, hexadecimal,
     b) Los binarios 1000, 10, 101        ==>   a decimal
     c) Los octales 563, 8, 64            ==>   a decimal
     d) Los hexadecimales ABC, 10A2, 9FF  ==>   a decimal"""

""" Crear las siguientes secuencias: 
       a) 1,2,3,4,5,6,...500
       b) 2,4,6,8,10,12...200
       c) 100, 99, 98, ..., 0
       d) -100, -95, -90, ... 100
       Use range(<inicio>, <fin>, <salto>), para visualizarlo utilice list(<secuencia>)"""

secuencia1 = range(1, 501, 1)
secuencia2 = range(2, 201, 2)
secuencia3 = range(100, -1, -1)
secuencia4 = range(-100, 101, 5)

print("SECUENCIA 1 => ", list(secuencia1))
print("SECUENCIA 2 => ", list(secuencia2))
print("SECUENCIA 3 => ", list(secuencia3))
print("SECUENCIA 4 => ", list(secuencia4))


"""Formatear  los siguientes elementos:
      a) 0.52941, 2.389, 3.5, 200000 ==> entero
                                         flotante 2 decimales, 
                                         flotante 5 decimales,
                                         notación científica 2 decimales, 
"""

num1 = 0.52941
num2 = 2.389
num3 = 3.5
num4 = 200000

print("numero1 => ", num1, int(num1), round(num1, 2), round(num1, 5), format(num1, ".2E"))
print("numero5 => ", num4, int(num4), round(num4, 2), round(num4, 5), format(num4, ".2E"))                   



''' 
utilizar el listado [1, 10, 20, 10.4, 20.05,  3]
luego ejecute las siguientes funciones integradas sobre dicho listado
len(), 
sum(), 
max(), 
min(), 
sorted() '''


lista = [1, 10, 20, 10.4, 20.05,  3]
print("lista ===== ", lista)

print("tamaño =>", len(lista))
print("sumar =>", sum(lista))
print("maximo =>", max(lista))
print("minimo =>", min(lista))
print("ordenar =>", sorted(lista))












