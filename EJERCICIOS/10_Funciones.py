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

"""evaluar la funcion con los numeros =>
5, 101, 1_001, 10_003, 1000_001, 371_003"""
