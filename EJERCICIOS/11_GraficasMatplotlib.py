import matplotlib.pyplot as plt
import numpy as np

#Dispersion de puntos
x = [1,2,3,4,5,6]
y = [10,20,30,40,50, 60]
plt.figure()
plt.plot(x, y, "o")
plt.show()

#Dispersion senoidal más elaborada
x = np.linspace(0,6.28)
y = np.sin(x)
plt.figure()
plt.plot(x,y, "r+")
plt.title("Funcion senoidal")
plt.xlabel("Angulo")
plt.ylabel("sin(x)")
plt.grid()
plt.show()





