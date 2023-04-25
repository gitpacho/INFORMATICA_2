import matplotlib.pyplot as plt
import numpy as np

#Dispersion de puntos
#x = [1,2,3,4,5,6]
#y = [10,20,30,40,50, 60]
#plt.figure()
#plt.plot(x, y, "o")
#plt.show()


#Dispersion senoidal más elaborada
#x = np.linspace(0,6.28)
#y = np.sin(x)
#plt.figure()
#plt.plot(x,y, "r+")
#plt.title("Funcion senoidal")
#plt.xlabel("Angulo")
#plt.ylabel("sin(x)")
#plt.grid()
##plt.show()

import numpy as np
#Graficar la funcion f(x) = x ** 0.5
#para valores de x => [0,90]

x0 = np.arange(0, 91, 1)
y0 = x0 ** 0.5
#Graficar la funcion f(x) = sen²(x) + 1
#para valores de x => [0, 10]

x1 = np.arange(0,10, 0.1)
y1 = np.sin(x1)**2 + 1

#Graficar la funcion f(x) = e ** (-1/x)
#para valores de x => [-5, 5]

x2 = np.arange(-5,5,0.03)
y2 = np.exp(-1/x2)

#Graficar la funcion f(x) = 1/x
#para valores de x => [-5, 5]

x3 = np.arange(-5,5, 0.03)  
y3 = 1/x3


def graficar(x, y, titulo, limitex, limitey, legenda):
    plt.figure(figsize=(10, 4))                 #crear figura
    plt.plot(x, y,".r", label = legenda) 
    plt.xlim(limitex[0],limitex[1])                             #limitar eje x
    plt.ylim(limitey[0],limitey[1])                             #limitar eje y
    plt.title(titulo)                          #mostrar titulo
    plt.xlabel("x [s]")                        #mostrar nombre ejex
    plt.ylabel("y [m]")                        #mostrar nombre ejey
    plt.grid()                                 #mostrar grilla
    plt.legend()                               #mostar labels
    plt.savefig("EJERCICIOS/11Grafica{}.png".format(titulo))
    #plt.show()                                 #mostrar figura
    plt.close()


graficar(x0, y0, "Funcion 1", (0,90), (0,12),  "y = x ^ (0.5)")
graficar(x1, y1, "Funcion 2", (0,10), (0,2),   "y = sin²(x) + 1")
graficar(x2, y2, "Funcion 3", (-5,5), (0, 3),  "y = e ^ (-1/x)")
graficar(x3, y3, "Funcion 4", (-5,5), (-1, 1), "y = 1/x")


#Obtener la grafica mostrada en la figura 5



