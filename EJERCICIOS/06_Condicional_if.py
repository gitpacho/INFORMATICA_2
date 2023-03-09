#==> Ejercicio 1 
"""   a) Pedir al usuario que ingrese su edad, luego imprimir en pantalla si es mayor o menor de edad
      b) Pedir al usuario que ingrese su salario, luego imprimir si su salario es alto o bajo, 
        (salario alto > $ 5 000 000)
      c) Pedir al usuario que ingrese 3 notas, luego avisar si aprueba o reprueba la materia 
         (Aprueba con promedio mayor o igual a 3.0)"""   
edad=18
if (edad >=18):
       print("Es mayor de edad")
else:
       print("Es menor de edad")


salario=6000000
if (salario > 5000000):
       print("Salario alto")
else:
      print("salario bajo")

nota1 = 1
nota2 = 3
nota3 = 4
notaFinal = (nota1 + nota2 + nota3) / 3
if (notaFinal >= 3.0):
       print("APROBADO")
else:
       print("REPROBADO")


#==> Ejercicio 2
"""Dados 2 numeros, desarrolle un programa que determine, ¿qué número es menor?:
   Dados 3 numeros, desarrolle un programa que determine, ¿qué número es mayor?: """

num1 = 3 
num2 = 4
if (num1<num2):
       print("num1 es el menor: ", num1)
elif (num2<num1):
       print("num2 es el menor:", num2)
else:
       print("No hay un numero menor, son iguales")

num1 = 3 
num2 = 5
num3 = 5
if (num1>num2) and (num1>num3):
       print("num1 es el mayor", num1)
elif (num2>num1) and (num2>num3):
       print("num2 es el mayor", num2)
elif (num3>num1) and (num3>num2):
       print("num3 es el mayor", num3)
else:
       print("HAY IGUALDADES")

#==> Ejercicio 3
"""Desarrolle un programa que calcule el descuento salarial que hace una empresa a sus empleados, 
por motivos de pandemia. 
El programa debe solicitar el salario recibido por el trabajador (input)y luego debe imprimir 
el descuento realizado (print).
Si el empleado gana menos de $ 900.000 se le descuenta el 15%, luego
si devenga hasta $2.500.000 se le descuenta el 20%. Por último si 
gana por encima de este último valor se le descuenta el 25% de su 
salario."""

salario = 1_000_000 # debe ser un input el valor ingresado

if (salario < 900_000):
       descuento = salario * 0.15
elif (salario >= 900_000) and (salario <= 2_500_000):
       descuento = salario*0.20
else:
       descuento = salario*0.25
print("EL DESCUENTO ES DE ==> ", descuento)


#==> Ejercicio 4 
"""Los estudiantes del curso de matematicas obtuvieron las siguientes 
calificaciones definitivas (cada una de las notas equivale al 25%):

         Nota1  Nota2  Nota3  Nota4
Camila    1.0    2.3    5.0    5.0
Maria     5.0    3.5    2.5    3.2
José      2.2    4.0    3.2    4.1
Daniela   5.0    0.5    1.0    0.2
Esteban   4.0    5.0    0.0    0.0

El director del grupo preparará una salida académica, en caso de 
que se hayan cumplido las siguientes condiciones:
   * El 60% del grupo debe aprobar la materia
   * Por lo menos dos notas del grupo, deben tener un promedio mayor a 3.0
   * El promedio de los que perdieron la materia debe ser mayor a 2
¿habrá salida académica?"""


#------------ condicion1------------------------------
definitiva_Camila   = (1.0 + 2.3 + 5.0 + 5.0)/4
definitiva_Maria    = (5.0 + 3.5 + 2.5 + 3.2)/4
definitiva_José     = (2.2 + 4.0 + 3.2 + 4.1)/4
definitiva_Daniela  = (5.0 + 0.5 + 1.0 + 0.2)/4
definitiva_Esteban  = (4.0 + 5.0 + 0.0 + 0.0)/4 

reporte_Camila   = definitiva_Camila >= 3
reporte_Maria    = definitiva_Maria >= 3
reporte_José     = definitiva_José >= 3
reporte_Daniela  = definitiva_Daniela >= 3
reporte_Esteban  = definitiva_Esteban >= 3

porcentajeAprobados = ((reporte_Camila + reporte_Maria + reporte_José + reporte_Daniela + reporte_Esteban) / 5) * 100

condicion1 = porcentajeAprobados >= 60
print("condicion1 ==>", condicion1)



#------------ condicion2------------------------------

nota1Grupo = (1.0+5.0+2.2+5.0+4.0) / 5
nota2Grupo = (2.3+3.5+4.0+0.5+5.0) / 5
nota3Grupo = (5.0 +2.5 +3.2+ 1.0+ 0.0) / 5
nota4Grupo = (5.0+3.2+4.1+0.2+0.0) / 5

ReporteNota1Grupo = (nota1Grupo >= 3.0)
ReporteNota2Grupo = (nota2Grupo >= 3.0)
ReporteNota3Grupo = (nota3Grupo >= 3.0)
ReporteNota4Grupo = (nota4Grupo >= 3.0)

numeroNotasGrupoAprobadas = (ReporteNota1Grupo+ReporteNota2Grupo+ReporteNota3Grupo+ReporteNota4Grupo) 

condicion2 = (numeroNotasGrupoAprobadas >=2)
print("condicion2 =>", condicion2)


#------------ condicion3----------------------------

definitiva_Camila   = (1.0 + 2.3 + 5.0 + 5.0)/4
definitiva_Maria    = (5.0 + 3.5 + 2.5 + 3.2)/4
definitiva_José     = (2.2 + 4.0 + 3.2 + 4.1)/4
definitiva_Daniela  = (5.0 + 0.5 + 1.0 + 0.2)/4
definitiva_Esteban  = (4.0 + 5.0 + 0.0 + 0.0)/4 

EsCamilaMayorA2 =  round(definitiva_Camila)   >= 2
EsMariaMayorA2 =  round(definitiva_Maria)     >= 2
EsJoséMayorA2 =  round(definitiva_José)       >= 2
EsDanielaMayorA2 =  round(definitiva_Daniela) >= 2
EsEstebanMayorA2 =  round(definitiva_Esteban) >= 2

SonMayoresA2Todos = ((EsCamilaMayorA2+EsMariaMayorA2+EsJoséMayorA2+EsDanielaMayorA2+EsEstebanMayorA2)==5)
condicion3 = SonMayoresA2Todos

print("condicion3", condicion3)


if (condicion1 and condicion2 and condicion3):
   print("Habrá salida académica")
else:
   print(" No Habrá salida académica")






