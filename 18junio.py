# frutas = ["manzana","banana","naranja","banana"]
# frutas.remove("banana")
# print(frutas)

# numeros = [5,3,7,3,9]
# numeros.remove(3)
# print(numeros)

#--------------------ejercicios-append---------------

#1
# print("No.1")

# numeros = []
# print(numeros)

# numeros.append(7)
# print(numeros)

# print("-----------2---------")
# print("No. 2")

# nombres = []
# print(nombres)

# nombres.append("Ana")
# nombres.append("Luis")

# nombres.append("Carlos")

# print(nombres)

#------------------ejercicios-insert--------------------

# print("No. 1")

# num = [1, 2, 3]
# print(num)

# num.insert(0,99)

# print(num)

# print("----------------------------------------")
# print("No. 2")

# colores = ["azul", "verde"]
# print(colores)

# colores.insert(1,"rojo")

# print(colores)

#-----------------ejercicios-iterable------------------

# print("No. 1")

# lista = [1,2,3]
# lista2 = [4,5,6]

# print(lista)
# print(lista2)

# lista.extend(lista2)

# print(lista)

# print("---------------------------------------")
# print("No. 2 ")

# letras = ["a","b"]
# print(letras)

# letras.extend("ok")
# print(letras)
#--------------------remove-------------------------

# print("No. 1")

# frutas = ["manzana","uva","pera"]
# print(frutas)

# frutas.remove("uva")
# print(frutas)

# print("--------------------------------")
# print("No. 2")

# numeros = [1,2,3,2]
# print(numeros)

# numeros.remove(2)
# print(numeros)

#--------------pop-----------------------------------------

# numeros = [1,2,3,4]
# print(numeros)

# numeros.pop(3)
# print(numeros)

# print("----------------------------------------------")

# text = ["uno","dos","tres"]
# print(text)

# text.pop(0)
# print(text)

#----------------clear--------------------

# numeros = [1,2,3]
# print(numeros)

# numeros.clear()
# print(numeros)

# print("----------------------------------------")

# lista = []

# O1 = input(f"Dame un elemento (1/4): ")
# O2 = input(f"Dame un elemento (2/4): ")
# O3 = input(f"Dame un elemento (3/4): ")
# O4 = input(f"Dame un elemento (4/4): ")

# lista.append(O1)
# lista.append(O2)
# lista.append(O3)
# lista.append(O4)

# print(lista)

# lista.clear()
# print(lista)

#---------------------index------------------------

# lista = ["manzana","pera","uva"]
# print(lista)

# print(lista.index("pera"))

# print("------------------------")

# numeros = [4,5,6,7]
# print(numeros)

# print(numeros.index(6))

#-----------------------count------------------------

# listanum = [3,1,3,5,3]
# print(listanum)

# print(listanum.count(3))

# print("------------------------------------------")

# letras = ["a","b","a","c","a"]
# print(letras)

# print(letras.count("a"))

#-----------------------sort------------------------------

# numeros = [5,1,4,2,3]
# print(numeros)

# numeros.sort()
# print(numeros)

# print("------------------------------------")

# letras = ["z","a,","m","b"]
# print(letras)

# letras.sort()
# print(letras)

#--------------------------reverse-------------------------------

# lista = [1,2,3,4]
# print(lista)

# lista.reverse()
# print(lista)

# print("-------------------------")

# lista2 = ["inicio","medio","final"]
# print(lista2)

# lista2.reverse()
# print(lista2)

#----------------------------copy-------------------------------

# lista = [1,2,3]
# print(lista)

# nuevalista = lista.copy()
# print(f"copia: {nuevalista}")

# print("---------------------------------------------")

# letras = ["a","b","c"]
# print(letras)

# letras2 = letras.copy()
# letras2.insert(3,"d")

# print(f"Copia {letras2}")

#---------------- ACTIVIDAD LISTAS -------------------- #

LISTA1 = []
LISTA2 = []
print(f"Lista 1: {LISTA1}\nLista 2: {LISTA2}")

# añadir lista1 el int100 y el string "Hola Mundo"

LISTA1.append(100)
LISTA1.append("Hola Mundo")
print(f"Punto No. 1: {LISTA1}")

# añadir a lista2 el string "Hola y Adios" y el int 300

LISTA2.append("Hola y Adios")
LISTA2.append(300)
print(f"Punto No. 2: {LISTA2}")

#generar lista 3 con los elementos de lista1 sin considerar el ultimo

LISTA3 = LISTA1.copy()
LISTA3.remove("Hola Mundo")
print(f"Punto No. 3: {LISTA3}")

#generar lista4 con todo de lista 2 menos el primero y el ultimo

LISTA4 = LISTA2.copy()
LISTA4.clear()
print(f"Punto No. 4: {LISTA4}")

#generar lista5 con elementos de lista4 y lista3
LISTA5 = []
LISTA5.extend([LISTA4])
LISTA5.extend([LISTA3])

print(f"Punto No. 5: {LISTA5}")

#------------------------------------------------------------

