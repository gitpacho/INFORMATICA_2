import numpy 
import pandas
import matplotlib.pyplot as plt

def grafica(y, encendido):
    plt.figure()
    x = range(len(y))
    plt.plot(x, y)
    if encendido == True:
        plt.show()
    else:
        plt.close()


#=================arreglos numpy ==================

arreglo1D = numpy.array([3,5,7,2])

arreglo2D = numpy.array([[1,2,3],
                         [4,5,6],
                         [7,8,9]])

#=> Arreglos Predefinidos
array1D = numpy.arange(10,20, 0.5)
array2D = array1D.reshape((4,5))  #filas,columnas

print("array1", array1D)
print("array2", array2D)

aleatorios1D = numpy.random.random(50)  #50 valores aleatorios [0,1]
aleatorios2D = aleatorios1D.reshape((5,10))

print("aleatorios1D", aleatorios1D)
print("aleatorios2D", aleatorios2D)





