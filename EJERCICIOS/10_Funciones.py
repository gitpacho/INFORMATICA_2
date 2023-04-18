""" funcion que retorne si un numero 
es primo """

def esPrimo(numero):
    divisores = range(2,numero)
    esNumeroPrimo = True
    for divisor in divisores:
        if numero % divisor == 0:
            esNumeroPrimo = False
            break
    return esNumeroPrimo
print(esPrimo(23))

"""Evaluar la funcion anterior con los numeros =>
5, 101, 1_001, 10_003, 1_000_001, 371_003"""

numeros = [5,101,1001,10003,1000001,371003]
for numero in numeros:
    print(numero, "¿Es primo? =>", esPrimo(numero))

"""Cree y ejecute una funcion que calcule
la suma de dos vectores:

vector1    = [1,2,3,4,5]
vector2    = [6,7,8,9,0]
sumaVector = [7,9,11,13,5]
"""

def sumarVectores(vector1, vector2):
    indices = range(0, len(vector1))
    sumaVector = []
    for indice in indices:
        suma = vector1[indice] + vector2[indice]
        sumaVector.append(suma)
    return sumaVector

vector1    = [1,2,3,4,5]
vector2    = [6,7,8,9,0]
print("Suma vector", sumarVectores(vector1, vector2))
    
"""cree y ejecute una funcion que me encuentre
el numero de vocales en una oracion

nombre: contarVocales
variables de entrada: oracion
variable de salida:   numeroVocales
"""
def contarVocales(oracion):
    numeroVocales = 0
    for letra in oracion:
        if letra in "aeiouAEIOUáéíóúÁÉÍÓÚ":
            numeroVocales += 1
    return numeroVocales

oracion = "Hola mundo crúel"
print("contar vocales en:", oracion, "=>", end=" ")
print(contarVocales(oracion))


"""cree una funcion que me sume sucesivamente los 
digitos de un numero. Ejemplo:
8917  => 25 => 7
34798 => 31 => 4
9875  => 29 => 11 => 2

nombre: sumarDigitos
entrada: numero (entero)
salida:  sumDigitos (entero)
"""


#PENDIENTE ===>

def sumarDigitos(numero):
    sumDigitos = 0
    numeroString = str(numero)
    for digito in numeroString:
        sumDigitos += int(digito)
    numeroString = str(sumDigitos)
    return sumDigitos

print(sumarDigitos(1237))

#==========================EJERCICIOS CASA==========================
#====================== EJERCICIOS DE FUNCIONES ====================

#==> EJERCICIO 1
"""Desarrolle las siguientes funciones: 
PARAMETRO DE ENTRADA     VALOR DE RETORNO       PROBLEMA
 * edad                     * booleano            * Función que determine si una persona es mayor de edad
 * nombre y salario         * string              * Función que reciba el nombre y salario de trabajador, y luego retorne una cadena con el mensaje: "hola <nombre>, su salario es <salario>"
 * numero                   * entero              * Función que calcule la suma de los digitos de un numero 
 * mensaje                  * booleano            * Función que determine si un mensaje tiene vocales o no
 * numero                   * lista               * Función que devuelva todos los divisores de un numero
 * numero                   * booleano            * Función para determinar si un número es primo
"""

#==> EJERCICIO 2
""" Realice una función que reciba una contraseña y que retorne un string que informe si la contraseña es válida o inválida
    Las condiciones de validez son las siguientes: 
          a) Debe contener Alfabeto en mayuscula
          b) Debe contener Alfabeto en minuscula
          c) Debe contener Números
          d) Debe contener Caracteres especiales
          e) Debe contener Por lo menos 8 caracteres en total"""

#==> EJERCICIO 3
""" Desarrolle una función que calcule el índice da masa 
   corporal de un deportista, como parametro de Entrada
   reciba la altura (m) y peso (Kg). Como salida, devuelva el IMC
   que se calcula como se muestra. IMC (indice de masa corporal) = peso / estatura²
   Si su IMC es mayor a 30. Muestre en pantalla,
   un mensaje advirtiendo sobrepeso"""

#==> EJERCICIO 4
"""Cree una función que retorne el salario de un vendedor de seguros, si este se calcula 
   tomando un salario base de $2000000. Más una comisión por cada seguro, teniendo en cuenta
   que el porcentaje varía teniendo en cuenta la tabla. El precio de cada seguro es de $300000
      
     Seguros [unidades]    comision
      [50-110)               10%
      [110, 200)             20%
      [200, 500)             25%
      [500, infinito]        30%
   Utilice la función para calcular el salario de los siguientes empleados
                 Unidades vendidas
   vendedor1          41
   vendedor2          110
   vendedor3          200
   vendedor4          520
"""

#==> EJERCICIO 5
"""El precio de venta de los artículos de una empresa es el siguiente:
   Codigo      Precio unitario
    A001          $ 31 000
    A011          $ 25 000
    A032          $ 43 000
    A125          $ 55 000
    B001          $ 10 000
    B005          $ 20 000
    P009          $ 30 000
    P019          $ 49 000
    R001          $ 60 000
    W307          $ 90 000
    Z052          $ 35 000
    Z025          $ 27 000
    Z278          $ 65 000
Las ventas a lo largo de un día se ha registrado en la siguiente 
base de datos:
ventas = ["A032-52Unidades", "B001-29Unidades", "A125-15Unidades", "A032-22Unidades", "P009-25Unidades", "B005-20Unidades", "B001-19Unidades", "P009-31Unidades", "B005-22Unidades", "W307-15Unidades", "A011-31Unidades", "P019-18Unidades", "A011-20Unidades", "R001-20Unidades", "P019-19Unidades", "A001-12Unidades", "A125-20Unidades", "R001-31Unidades", "Z052-52Unidades", "W307-31Unidades", "Z025-42Unidades", "Z052-10Unidades", "Z278-30Unidades", "Z025-24Unidades", "Z278-21Unidades", "A001-31unidades"]
Cree una función que reciba la base de datos 
y luego retorne el dinero recaudado a lo largo del día"""

#==> EJERCICIO 6
"""Se tiene el rendimiento académico de los estudiantes
   de un colegio como se muestra:
   Código      Nombre          Algebra Electricidad Optica Organica Cuantica Deportes Artes  
    0001   Natalia Bermudez       3.3       3.2       2.9     3.1      4.0     3.7     3.2
    0002   Jose Rodriguez         5.0       5.0       5.0     5.0      5.0     5.0     5.0    
    0003   Emilio Pineda          4.2       1.0       2.0     3.0      2.9     2.2     1.0
    0004   Camila Quiceno         5.0       3.0       2.9     4.0      3.1     5.0     1.9
    0005   Elisabeth Diaz         2.9       1.1       2.0     2.5      3.1     0.5     2.2
    0006   Andres Pineda          3.9       5.0       1.0     0.2      2.8     5.0     5.0
    0007   Esteban Buitrago       4.1       4.2       4.5     4.8      4.0     4.4     4.2
    0008   Juanita Quintero       3.2       2.3       2.9     2.1      1.9     3.2     3.0
    0009   Estefania Chacón       2.2       1.0       0.8     2.2      2.9     3.1     1.0   
    0010   Daniel Arbelaez        3.1       1.2       0.3     1.9      2.6     5.2     5.0  
    0011   María Martínez         4.2       3.9       5.0     4.5      3.8     2.0     5.0
    0012   Marco Rosero           3.0       2.9       2.5     2.2      3.1     3.5     5.0
    0013   Cristian Quesada       2.5       1.9       2.0     3.0      2.5     1.1     2.9
    0014   Sofia Bueno            2.2       5.0       5.0     3.1      3.2     3.5     0.0
    0015   Laura Tobón            1.1       2.0       2.8     1.2      3.1     2.9     3.1    
    0016   Victor Urrego          3.2       0.0       0.0     0.0      0.0     0.0     0.0
    0017   Juan Quevedo           4.1       4.0       4.2     4.3      3.9     5.0     4.5
    0018   Sebastian Castillo     3.5       3.1       3.2     3.3      4.0     1.9     5.0
    0019   Jose Rubiano           4.1       4.5       5.0     5.0      5.0     5.0     5.0
    0020   Fabio Cardenas         3.2       5.0       5.0     0.0      0.0     0.0     0.0 
    Para resolver este problema primero almacene esta información en un
    elemento de python, ya sea lista,tupla, diccionario, lista de listas, lista de enteros, strigs...,  diccionario de listas...
    o cómo prefiera. Luego realice diferentes funciones para:
    a) Realice una función que reciba un codigo de estudiante, y luego imprima un reporte de todas sus notas y su promedio. 
    b) Realice una función que reciba el nombre de una materia y luego imprima el promedio de dicha materia
    c) Realice una función que devuelva una lista con los nombres de los estudiantes que aprobaron todas sus materias.
    d) Realice una función que devuelva una lista con los nombres de los estudiantes que reprobaron todas sus materias.
    e) Realice una función que reciba un numero de materias ganadas y devuelva una lista con los nombres de los estudiantes que aprobaron esa cantidad de materias
    f) Realice una función que reciba un numero de materias perdidas y devuelva una lista con los nombres de los estudiantes que reprobaron esa cantidad de materias"""



