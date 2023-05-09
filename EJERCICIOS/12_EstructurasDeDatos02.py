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


#-----------------------EJERCICIO----------------------

#crear una serie con los siguientes datos: 

"""
  Nombre              Salario   
  Cristian Pachon     $ 3.200.000
  Daniela Pineda      $ 4.300.000
  Esteban Murcia      $ 4.600.000
  Jose Guzman         $ 3.900.000
  Camilo Rodriguez    $ 1.200.000
  Mariana Londoño     $ 1.100.000
  Estefania Muñoz     $ 1.700.000
  Cristian Rodriguez  $ 3.100.000
  Natalia Alzate      $ 2.200.000
  Juan Sanabria       $ 5.100.000
  Juanita Calderon    $ 1.300.000
  Laura Quintero      $ 2.500.000
  Viviana Quesada     $ 1.500.000"""


#Luego:
#Extraer el salario de Estefania Muñoz
#Extraer el salario de Mariana Londoño
#Extraer el salario mas alto 
#Extraer el salario más bajo
#Extraer los nombres de los trabajadores con salario mayor a 4 millones
#Extraer los nombres de los trabajadores con salario menor a 1.5 milones
#Determinar la media de los salarios
#Determinal la desviacion estandar de los salarios


index = ["Cristian Pachon","Daniela Pineda","Esteban Murcia","Jose Guzman","Camilo Rodriguez","Mariana Londoño","Estefania Muñoz","Cristian Rodriguez","Natalia Alzate","Juan Sanabria","Juanita Calderon","Laura Quintero","Viviana Quesada"]
data = [3200000,4300000,4600000,3900000,1200000,1100000,1700000,3100000,2200000,5100000,1300000,2500000,1500000]
salarios = pandas.Series(index=index, data=data)

print(salarios)
print("Salario de Estefania =>", salarios["Estefania Muñoz"])
print("Salario de Mariana =>", salarios["Mariana Londoño"])
print("Salario más alto =>", salarios.max())
print("Salario más bajo =>", salarios.min())
salariosAltos = salarios[salarios > 4000000]
print("Salarios superiores a 4 mill =>", list(salariosAltos.index))
salariosBajos = salarios[salarios < 1500000]
print("Salarios menores a 1.5 mill =>", list(salariosBajos.index))
print("media de salarios =>", salarios.mean())
print("Desviacion estandar de salarios =>", salarios.std())

# Dibujar y describir la serie salarios

print("descripcion => \n",salarios.describe())
#import matplotlib.pyplot as plt
#plt.figure()
#salarios.plot.hist()
#plt.show()















