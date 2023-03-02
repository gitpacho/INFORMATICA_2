'''
Ejecutar cada una de las funciones
integradas mostradas en el el archivo 
05_FuncionesIntegradas.txt

Nota: Busque la manera para poder ejecutarlas
'''

#Entrada y salida
print("==========funcion entrada y salida==========")

#x = input("Por favor ingrese un numero: ") #Recibe strings
#x_num = int(x)
#print("El numero ingresado fue: ", x_num, type(x_num))

#Ayuda

print("==========funcion ayuda==================")
datos = [1,2,3,4]

print("typo de dato =>", type(datos))  # Retorna el tipo de dato que se usa
print("directorio => ", dir(datos))      # Devuelve las funcionalidades
#help(str)         #Devuelve una ventana interactiva, para salir presionar <q>

print("================Conversiones====================")
conv1 = int(19.9999)   # devuelve el 19
conv2 = float("25")    # devuelve el 25.0
conv3 = bool(1)        # devuelve True
conv4 = list("hola")   # devuelve una lista: ["h", "o", "l", "a"]
conv5 = tuple([1,2,3]) # devuelve una tupla: (1,2,3)
conv6 = dict([(1, "uno"), (2, "dos"), (3, "tres")]) 
conv7 = set("abcdefghijklmnopqrstuvwxyz")  #Devuelve {"a", "b", "c",..."z"}




















