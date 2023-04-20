import matplotlib.pyplot as plt
import numpy as np

#Dispersion de puntos
x = [1,2,3,4,5,6]
y = [10,20,30,40,50, 60]
plt.figure()
plt.plot(x, y, "o")
#plt.show()
plt.close()

#Dispersion senoidal más elaborada
x = np.linspace(0,6.28)
y = np.sin(x)
plt.figure()
plt.plot(x,y, "r+")
plt.title("Funcion senoidal")
plt.xlabel("Angulo")
plt.ylabel("sin(x)")
plt.grid()
plt.close()
#plt.show()

#Graficar la funcion f(x) = x ** 0.5
#para valores de x => [0,90]

x_rango = range(0,91,2)
y_list  = []
for x in x_rango:
    y_list.append(x**0.5)

plt.figure(figsize=(5, 2))                               #crear figura
plt.plot(x_rango, y_list,"og", label="f(x) = x^(0.5)") 
plt.plot(x_rango, [i + 1 for i in y_list],"ob", label="f(x) = 1 + x**0.5")
plt.xlim(0,90)                             #limitar eje x
plt.ylim(0,12)                             #limitar eje y
plt.title("Dispersion de puntos")          #mostrar titulo
plt.xlabel("x [s]")                        #mostrar nombre ejex
plt.ylabel("y [m]")                        #mostrar nombre ejey
plt.grid()                                 #mostrar grilla
plt.legend()                               #mostar labels
plt.show()                                 #mostrar figura


#Graficar la funcion f(x) = sen²(x) + 1
#para valores de x => [0, 10]

#Graficar la funcion f(x) = e ** (-1/x)
#para valores de x => [-5, 5]

#Graficar la funcion f(x) = 1/x
#para valores de x => [-5, 5]






