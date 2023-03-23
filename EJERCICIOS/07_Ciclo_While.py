#====================== EJERCICIOS CICLO WHILE ====================
#==> EJERCICIO 1 
"""Desarrolle un ciclo while infinito, con un mensaje que informe, cada vez que el ciclo es repetido."""

#cont = 1
#while True:
#    print("El ciclo ha sido repetido", cont, "veces")
#    cont += 1

#==> EJERCICIO 2 
"""Realice un ciclo while con un numero secreto. Cada vez que se ejecuta un ciclo, el programa pide
adivinar el numero, en caso de no ser acertado se debe mostrar un mensaje diciendo: "Estás atrapado". 
Y en caso contrario terminar el ciclo y avisar que el numero es correcto."""

#numero_secreto = 975
#numero_usuario = 9999999
#
#while (numero_usuario != numero_secreto):
#    numero_usuario = int(input("Ingrese la contraseña: "))
#    if numero_usuario == numero_secreto:
#        print("el numero es correcto")
#    else:
#        print("Estás atrapado")


#==> EJERCICIO 3 
"""Realice un programa, que determine el número mayor para una cantidad indeterminada de numeros positivos. (Utilice el ciclo while)"""

#mayor = 0
#respuesta = "si"
#
#while respuesta == "si":
#    respuesta = input("Desea ingresar un numero: ")
#    if respuesta == "si":
#        numero = int(input("Ingrese el numero: "))
#
#    if numero >= mayor:
#        mayor = numero
#
#print("mayor ==> ", mayor)


#==> EJERCICIO 4 
"""Realice un programa que lea una secuencia de números, y cuente cuántos números son pares y cuántos son impares. 
El programa termina cuando se ingresa el número cero."""

#cantidad_pares  = 0
#cantidad_impares  = 0
#
#numero_ingresado = 1
#while (numero_ingresado != 0):
#    numero_ingresado = int(input("Por favor ingrese un numero: "))
#    if (numero_ingresado % 2 == 0) and (numero_ingresado != 0):
#        cantidad_pares += 1
#    elif (numero_ingresado % 2 == 1):
#        cantidad_impares += 1
#
#print("cantidad_pares =>", cantidad_pares)
#print("cantidad_impares =>", cantidad_impares)


#==> Ejercicio 5 
"""Utilizando el ciclo while, imprima las siguientes secuencias de numeros:
=> 2,4,8,16,32,64,128, .. 1048576
=> 1,1,2,3,5,8, ... 2178309
=> 2,4,5,8,10,11,14,16,17,20 ...598, 599
"""

numero = 2
while (numero <= 1048576):
    print(numero, end="-")
    numero *= 2

print("\nserie fibonacci =>")
numero1 = 1
numero2 = 1
while (numero2 <= 2178309):
    print(numero2, end="-")
    numero1, numero2 = numero2, numero1 + numero2



print("\n\nSerie +2, +1, +3 ==> \n")
numero = 2
suma1, suma2, suma3 = 2,1,3
cont = 0

while numero <= 599:
    print(numero, end = "-")
    if cont%3 == 0:
        numero += suma1
    elif cont%3 ==1:
        numero += suma2
    elif cont%3 == 2:
        numero += suma3
    cont += 1 




