#Ejemplos Metodos de las cadenas
print("Métodos de las cadenas \n\n")

cadena = "hola mundo cruel"
print("mayusculas =>", cadena.upper())
print("capitalizar =>", cadena.capitalize())
print("capitalizar =>", cadena.title())
print("conteo =>", cadena.count("o"))
print("verificar =>", "12345".isdecimal())
print("indexado primero (h) y sexto (m)=>", cadena[0], cadena[5])  #indexado (metodo especial que aplica para cualquier iterable)
print("indexado ultimo (l, l) =>", cadena[15], cadena[-1])         #indexado (metodo especial que aplica para cualquier iterable)



#Ejemplos métodos de las listas
print("\n\nMétodos de las listas \n\n")

lista = [10,20,30,40,50, 50]
lista.append(1000) #Agrego al final de la lista
print("agregar elementos =>", lista)
lista.pop(2)  #Elimino 3er elemento (30)
print("eliminar elemento =>", lista)
print("contar un elemento =>", lista.count(50)) #Cuento el numero de veces que está el 50
lista.insert(0, 300) #Inserto en el indice 0, el valor 300
print("Agregar un elemento al principio =>", lista)

lista = [10,20,30,40,50,60,70,80,90,100, 110]
print("Primer elemento =>", lista[0])                #Metodos especiales indexado 
print("Ultimo elemento =>", lista[9], lista[-1])     #Metodos especiales indexado 
print("elemento del medio =>", lista[5], lista[-6])  #Metodos especiales indexado 

print("Elementos de la mitad hacia arriba", lista[6:-1:1]) #Metodos especiales slicing
print("Elementos en indices pares", lista[0:-1:2])         #Metodos especiales slicing
print("Elementos en indices impares", lista[1:-1:2])       #Metodos especiales slicing
print("todos los elementos al reves", lista[-1:0:-1])      #Metodos especiales slicing