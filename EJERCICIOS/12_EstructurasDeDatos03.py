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






