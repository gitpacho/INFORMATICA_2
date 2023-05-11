# DATAFRAMES

# Es una estructura de datos 2D
# sirve para manejar la informacion
# de manera semejante a como se hace en excel

# Para crearlos es necesario colocar el index, columns y data

"""
Codigo    Nombre   Nota1  Nota2  Nota3  Nota4
001       Camila    1.0    2.3    5.0    5.0
002       Maria     5.0    3.5    2.5    3.2
003       José      2.2    4.0    3.2    4.1
004       Daniela   5.0    0.5    1.0    0.2
005       Esteban   4.0    5.0    0.0    0.0
"""

index = ["001","002","003","004","005"]
columns = ["Nombre",   "Nota1",  "Nota2",  "Nota3",  "Nota4"]
data = [["Camila",    1.0,    2.3,    5.0,    5.0],
        ["Maria",     5.0,    3.5,    2.5,    3.2],
        ["José",      2.2,    4.0,    3.2,    4.1],
        ["Daniela",   5.0,    0.5,    1.0,    0.2],
        ["Esteban",   4.0,    5.0,    0.0,    0.0]]

import pandas
notas = pandas.DataFrame(index=index, columns=columns, data=data)
print(notas)

"""El director del grupo preparará una salida académica, en caso de 
que se hayan cumplido las siguientes condiciones:
   * El 60% del grupo debe aprobar la materia
   * Por lo menos dos notas del grupo, deben tener un promedio mayor a 3.0
   * El promedio de los que perdieron la materia debe ser mayor a 2
¿habrá salida académica?"""

promediosEstudiantes = notas.mean(axis=1)         #axis 1 por filas
                                                  #axis 0 por columnas

promediosPorNotas = notas.mean(axis=0)

condicion1 = promediosEstudiantes[promediosEstudiantes>=3].count() >= 3
print(condicion1)
condicion2 = promediosPorNotas[promediosPorNotas>=2].count() >= 2
print(condicion2)
condicion3 = promediosEstudiantes[promediosEstudiantes<3].count() > 2
print(condicion3) 

if condicion1 and condicion2 and condicion3:
    print("Habra salida")
else:
    print("No habra salida")

import matplotlib.pyplot as plt
notas2 = notas.transpose()[1::]
notas2.columns = notas["Nombre"].values
notas2.plot(style="-o", grid="on")
plt.show()


########EJERCICIO DATAfRAMES##########


""" Seis compañeros, contratan un taxi con el objeto de movilizarse juntos a la universidad. 
El contrato es de lunes a viernes, y deben pagar al taxista $15000 por cada trayecto. 
Se prestarán dos servicios al día, uno de ida y el otro de regreso.

Sin embargo, los seis no se movilizan juntos todos los dias. Por tanto, han planteado que la tarifa
debe dividirse entre el numero de compañeros que se movilicen en cada trayecto.En caso, de que ninguno
utilice el servicio. Deben pagar al taxista una tarifa de $10000, repartidos equitativamente entre todos.
A continueación veamos el uso del servicio por parte de los compañeros en la última semana de clases:

                            IDA                             |                       REGRESO
            LUNES   MARTES  MIERCOLES   JUEVES  VIERNES     |    LUNES   MARTES  MIERCOLES   JUEVES  VIERNES
JUAN          Si        Si        Si      Si      No        |      Si        Si        Si      No       No
CAMILA        Si        No        Si      No      Si        |      Si        No        No      No       No
JOSE          Si        No        Si      Si      No        |      Si        No        Si      Si       No
MARIA         Si        Si        Si      No      No        |      No        No        Si      No       No
ESTEBAN       Si        No        No      Si      Si        |      No        No        No      Si       No
ANGIE         Si        No        Si      No      No        |      Si        No        Si      No       No

¿Cuanto debe pagar cada estudiante? 

Almacene el resultado dentro de un diccionario llamado "diccionarioPagos"
las claves deben ser los nombres de los estudiantes (en strings)
y los valores deben ser el dinero total que pagó cada uno al terminar la semana (en flotantes)
"""


index = ["JUAN","CAMILA","JOSE","MARIA","ESTEBAN","ANGIE"]
columns = ["LUNES","MARTES","MIERCOLES","JUEVES","VIERNES"]
data = [[True,  True,  True,  True,  False],
        [True,  False, True,  False, True],
        [True,  False, True,  True,  False],
        [True,  True,  True,  False, False],
        [True,  False, False, True,  True],
        [True,  False, True,  False, False]]

taxiIda = pandas.DataFrame(index=index, columns=columns, data=data)
print(taxiIda)


usuariosPorDia = taxiIda.sum(axis = 0)
cuotaPorDia = 15000/usuariosPorDia
print("\n\nusuariosPorDia =>\n", usuariosPorDia)
print("\n\ncuotaPorDia =>\n", cuotaPorDia)

cuotas = taxiIda * cuotaPorDia
print(cuotas)