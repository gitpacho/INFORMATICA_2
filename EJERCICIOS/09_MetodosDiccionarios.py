#===========================EJERCICIOS CLASE==============================
"""--------------diccionarios--------------
Extraccion: items(), keys(), values(), get(key)
Eliminar: pop(key)
Almacenamiento: clear(), copy()
Indexado: [key]"""

#Se compone por pares clave-valor 
#y se separa por comas

#Diccionario español-inglés
diccTraduccion = {"silla": "chair",
                  "cara": "face",
                  "amarillo": "yellow"}

#Diccionario con atomo-masa
diccAtomico = {"Hidrogeno":1,
               "Azufre"   :32,
               "Carbono"  :12,
               "Oxigeno"  :16}

#Diccionario con estudiantes-nota
diccEstudiantes = {"Juan Chica":       4.2,
                   "Manuela Segura":   3.5,
                   "Santiago Tabares": 3.0,
                   "Cristian Pachon":  2.0}

print("claves del diccAtomico  => ", diccAtomico.keys())
print("valores del diccAtomico => ", diccAtomico.values())
diccTraduccion.pop("amarillo")
print("eliminar amarillo de diccTraduccion => ", diccTraduccion)
print("indexado para diccEstudiantes => ", diccEstudiantes["Santiago Tabares"])

# Teniendo en cuenta los metodos anteriores
# Agregue 3 nuevos elementos a diccEstudiantes

diccEstudiantes["Miguel Gomez"] = 4.5
diccEstudiantes["Juan Aya"] = 3.9
diccEstudiantes["Andrey Rodriguez"] = 3.8
print("Estudiantes insertados => ", diccEstudiantes)

# Haga un ciclo for para recorrer todo diccEstudiantes 
# impriman los pares clave-valor

#Recorrer claves
for clave in diccEstudiantes.keys():
    print(clave)
#Recorrer valores
for valor in diccEstudiantes.values():
    print(valor)
#Recorrer clave-valor
for clave in diccEstudiantes.keys():
    print(clave,"==>", diccEstudiantes[clave])
#Recorrer clave-valor
for clave, valor in diccEstudiantes.items():
    print(clave," : " ,valor)



#====================== EJERCICIOS MÉTODOS DE DICCIONARIOS ====================

#==> EJERCICIO 1
""" Cree el siguiente diccionario =>
    Calificaciones = {"Juan": 5.0, "David": 2.4, "Maria": 2.9, "Esteban": 2.2, "Daniela": 2.0, "Mario": 3.1, "Juanita": 2.1, "José": 3.0, "Sebastian": 2.3, "Cristian": 2.0, "Alberto": 3.9, "Angélica": 4.2, "Angel": 2.0, "Marly": 2.5, "Mariana": 4.5, "Josefina": 2.7}
     
       a) Extraiga los keys y values del diccionario, almacenelos en las variables claves, valores, respectivamente
       b) Corrija en el diccionario las calificaciones de Marly (4.3), Angel (3.1) y Juanita (3.5)
       c) Elimine a les estudiantes Josefina y Juan.
       d) Cree una copia y llamela reprobados, elimine todos aquellos con calificación mayor o igual a 3
       e) Muestre en pantalla la mejor calificación, para ello utilice indexing
       f) Muestre en pantalla la peor calificación, para ello utilice indexing 
       g) Utilice indexado para agregar dos nuevos estudiantes: Marco(3.0) Alejandra(5.0)"""


#==> EJERCICIO 2
""" Utilizando diccionarios cree una base de datos de empleados de una empresa,
la base de datos se debe llamar empleadosMabe. Debe contener la siguiente información

Cod   Nombre               Cargo          Salario   
0001   Cristian Pachon     Ingeniero      $ 3.200.000
0002   Daniela Pineda      Programador    $ 4.300.000
0003   Esteban Murcia      Programador    $ 4.600.000
0004   Jose Guzman         Ingeniero      $ 3.900.000
0005   Camilo Rodriguez    Ensamblador    $ 1.200.000
0006   Mariana Londoño     Ensamblador    $ 1.100.000
0007   Estefania Muños     Ensamblador    $ 1.700.000
0008   Cristian Rodriguez  Ingeniero      $ 3.100.000
0009   Natalia Alzate      Ensamblador    $ 2.200.000
0010   Juan Sanabria       Diseñador      $ 5.100.000
0011   Juanita Calderon    Ensamblador    $ 1.300.000
0012   Laura Quintero      Administrador  $ 2.500.000
0013   Viviana Quesada     Guardia        $ 1.500.000

A partir de la base de datos, busque una manera de:
    a) Encontrar la persona con mayor salario
    b) Encontrar la persona con menor salario
    c) Calcular el gasto total de la empresa por motivo salarios
    d) Calcular el promedio de lo que ganan los programadores
    e) Calcular el promedio de lo que ganan los ensambladores"""














