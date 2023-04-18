import matplotlib.pyplot as plt

x1 = [1,2,3,4,5,6]
y1 = [10,20,30,40,50, 60]

#Dispersion de puntos

plt.figure()
plt.plot(x1, y1, "o")
plt.show()

import numpy as np
x1 = np.linspace(0,6.28)
y1 = np.sin(x1) + 0.1 * np.random.random(len(x1))


plt.figure()
plt.plot(x1,y1, "r+")
plt.title("Funcion y = sin(x)")
plt.xlabel("Angulo")
plt.ylabel("sin(x)")
plt.grid()
plt.show()





