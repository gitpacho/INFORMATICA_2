###########
#Metodos de las cadenas
print("Métodos de las cadenas \n\n")

cadena = "hola mundo cruel"
#Esto lo pueden olvidar
print("mayusculas =>", cadena.upper())
print("capitalizar =>", cadena.capitalize())
print("capitalizar =>", cadena.title())
print("conteo =>", cadena.count("o"))
print("verificar =>", "12345".isdecimal())

#Pero esto no lo deben olvidar, ojo
#indexado (metodo especial que aplica para cualquier iterable)
print("indexado primero (h) y sexto (m)=>", cadena[0], cadena[5])
print("indexado ultimo (l, l) =>", cadena[15], cadena[-1])


########################################################
#Métodos de las listas
print("\n\nMétodos de las listas \n\n")

lista = [10,20,30,40,50, 50]
lista.append(1000)
print("agregar elementos =>", lista)
lista.pop(2)  #Elimino 3er elemento (30)
print("eliminar elemento =>", lista)
print("contar un elemento =>", lista.count(50))
lista.insert(0, 300)
print("Agregar un elemento al principio =>", lista)











#Metodos especiales indexado 
#lista = [10,20,30,40,50,60,70,80,90,100, 110]
#print("Primer elemento =>", lista[0])
#print("Ultimo elemento =>", lista[9], lista[-1])
#print("elemento del medio =>", lista[5], lista[-6])
#
##Metodos especiales slicing
#print("Elementos de la mitad hacia arriba", lista[6:-1:1])
#print("Elementos en indices pares", lista[0:-1:2])
#print("Elementos en indices impares", lista[1:-1:2])
#print("todos los elementos al reves", lista[-1:0:-1])






  

