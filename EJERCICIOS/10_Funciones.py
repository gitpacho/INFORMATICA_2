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

"""
cree y ejecute una funcion que calcule
la suma de dos vectores:

vector1    = [1,2,3,4,5]
vector2    = [6,7,8,9,0]
sumaVector = [7,9,11,13,5]

"""