#Veamos la estructura tipo serie
#Es un arreglo unidimensional tipo lista y diccionario a la vez

import pandas 

data = [31,28,31,30,31,30,31,31,30,31,30,31]
index = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sept", "Oct", "Nov", "Dic"]
serieDiasPorMes = pandas.Series(data=data, index=index)

#Serie con el numero atomico de 6 elementos quimicos
data2  = [1,2,6,8,7,73]
index2 = ["H", "He", "C", "O", "N", "Ta"]
serieNumerosAtomicos = pandas.Series(data=data2, index=index2)

# Buscar funciones que me permitan calcular sobre las series
#  La suma de cada serie
#  El media de cada serie
#  La desviacion estandar de cada serie

print("suma dias por mes =>", serieDiasPorMes.sum())
print("suma numeros atomicos =>", serieNumerosAtomicos.sum())

print("media dias por mes =>", serieDiasPorMes.mean())
print("media numeros atomicos =>", serieNumerosAtomicos.mean())

print("desviacion dias por mes =>", serieDiasPorMes.std())
print("desviacion numeros atomicos =>", serieNumerosAtomicos.std())

# Extraer los dias del mes de Mayo
# Extraer el numero atomico del Oxigeno
# Extraer aquellos meses con menos de 30 dias
# Extraer aquellos elementos con numero atomico mayor a 6


print("Dias de mayo =>", serieDiasPorMes["May"], serieDiasPorMes[4])
print("numero atomico Oxigeno =>", serieNumerosAtomicos["O"])


#crear una serie con los siguientes datos: 

"""Cod   Nombre               Cargo          Salario   
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
0013   Viviana Quesada     Guardia        $ 1.500.000"""