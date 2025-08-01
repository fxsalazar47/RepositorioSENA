#------- convertir vocal a mayuscula ----
# V = input(f"Ingrese su vocal para convertirla a mayuscula: ")
# if V == "a" or V == "e" or V == "i" or V == "o" or V == "u":
#     print(f"Su vocal en mayuscula es: {V.upper()}")
# else:
#     print(f"La letra ingresada no es válida")

# ----- TALLER 28 JULIO ----

# 1 ---- Verifica si un numero es positivo, negativo o cero ----

# num = float(input(f"Ingrese un numero: "))

# if num > 0:
#     print(f"El numero {num} es POSITIVO")
# elif num < 0:
#     print(f"El numero {num} es NEGATIVO")
# else:
#     print(f"El numero {num} es CERO")

# 2 ---- Calcula el mayor de dos numeros ingresados ----

# nm = [float(input(f"Ingrese su primer numero: ")) , float(input(f"Ingrese su segundo numero: "))]

# if nm[0] > nm[1]:
#     print(f"El numero mayor es {nm[0]}")
# elif nm[1] > nm[0]:
#      print(f"El numero mayor es {nm[1]}")
# else:
#     print(f"Los numeros son iguales")

# 3 ---- Determina si un numero es par o impar ----

# num = float(input(f"Ingrese un numero: "))

# if num % 2 == 0:
#     print(f"El numero {num} es PAR")
# else:
#     print(f"El numero {num} es IMPAR")

# 4 ---- Dado un numero. verifica si esta entre 10 y 20

# num = float(input(f"Ingrese un numero: "))

# if num >= 10 and num <= 20:
#      print(f"El numero {num} SI esta entre 10 y 20")
# else:
#      print(f"El numero {num} NO esta entre 10 y 20")

# 5 ---- Dados tres numeros, encuentra el mayor usando condicionales ----

# num = [float(input(f"Ingrese el primer numero: ")) , float(input(f"Ingrese el segundo numero: ")) , float(input(f"Ingrese el tercer numero: "))]

# if num[0] > num[1] and num[0] > num[2]:
#     print(f"El mayor de {num} es {num[0]}")
# elif num[1] > num[0] and num[1] > num[2]:
#     print(f"El mayor de {num} es {num[1]}")
# elif num[2] > num[0] and num[2] > num[1]:
#     print(f"El mayor de {num} es {num[2]}")
# else:
#     print(f"Todos los numeros son iguales")

# 6 ---- Calcula el precio final con un 10% de descuento si el total es mayor a $100 ----

# prec = int(input(f"Ingrese el precio de su producto: $"))
# if prec > 100:
#    print(f"El precio total a pagar es de: ${prec - (prec * 0.1)}\nTu compra tiene un 10% de descuento por ser mayor a $100!")
# else:
#     print(f"El precio total de tu compra es de ${prec}")

# 7 ---- Verifica si una persona puede votar (mayor o igual a 18 años) ----

# edad = int(input(f"Ingresa tu edad: "))

# if edad >= 18:
#     print(f"Tu edad es {edad} años, y SI puedes votar")
# else:
#     print(f"Tu edad es {edad} años, y NO puedes votar")

# 8 ---- Dado el precio y tipo de cliente (VIP o normal), aplica un descuento del 20% solo a VIP. ----

# precio = float(input(f"Ingrese el precio del producto: $"))
# tipclient = input(f"Selecciona tu tipo de cliente:\nSi eres cliente VIP, ingrese: 1\nSi eres cliente NORMAL, ingrese: 0\n")

# if tipclient == "1":
#     print(f"Al ser cliente VIP, tienes un 20% de descuento.\nEl total a pagar es de ${precio - (precio * 0.2)}")
# else:
#     print(f"Al ser cliente normal, no tienes descuento.\nEl total a pagar es ${precio}")

# 9 ---- Determina si un número es múltiplo de 5 y de 3 al mismo tiempo. ----

# num = float(input(f"Ingrese un número: "))

# if num % 3 == 0 and num % 5 == 0:
#     print(f"El numero {num} es multiplo de 3 y 5 al mismo tiempo!")
# else:
#     print(f"El numero {num} no es multiplo de 3 y 5 al mismo tiempo :(")

# 10 ---- Dado un número, verifica si es divisible entre dos números dados. ----

# nums = [float(input(f"Ingrese un numero: ")) , float(input(f"Ingrese un numero para dividir el primero: ")) , float(input(f"Ingrese otro numero para dividir el primero: "))]

# if nums[0] % nums[1] == 0 and nums[0] % nums[2] == 0:
#     print(f"El numero {nums[0]} SI es divisible entre {nums[1]} y {nums[2]}")
# else:
#     print(f"El numero {nums[0]} NO es divisible entre {nums[1]} y {nums[2]}")

# 11 ---- Crea una lista con 5 números. Si el tercer número es mayor que 10, muestra “Mayor a 10”, si no, muestra “Menor o igual a 10”.

# list = [float(input(f"Ingrese un primer numero: ")) , float(input(f"Ingrese un segundo numero: ")) , float(input(f"Ingrese un tercer numero: ")) , float(input(f"Ingrese un cuarto numero: ")) , float(input(f"Ingrese un quinto numero: "))]

# if list[2] > 10:
#     print(f"Mayor a 10")
# else:
#     print(f"Menor a 10")

# 12 ---- Verifica si el número 7 está en la lista [3, 5, 7, 9]. Si está, muestra “Está en la lista”, si no, muestra “No está en la lista”.

# list = [float(input(f"Ingrese un primer numero: ")) , float(input(f"Ingrese un segundo numero: ")) , float(input(f"Ingrese un tercer numero: ")) , float(input(f"Ingrese un cuarto numero: "))]

# if list[0] == 7 or list[1] == 7 or list[2] == 7 or list[3] == 7:
#     print(f"El numero 7 SI se encuentra en la lista! {list}")
# else:
#     print(f"El numero 7 NO se encuentra en la lista! {list}")

# 13 ---- Suma los dos primeros elementos de la lista [4, 6, 2, 8]. Si la suma es mayor que 10, muestra “Suma alta”, de lo contrario, muestra “Suma baja”. ----

# list = [float(input(f"Ingrese un primer numero: ")) , float(input(f"Ingrese un segundo numero: ")) , float(input(f"Ingrese un tercer numero: ")) , float(input(f"Ingrese un cuarto numero: "))]

# if list[0] + list[1] > 10:
#     print(f"Suma alta")
# else:
#     print("Suma baja")

# 14 ---- Dada la lista ["Ana", "Luis", "Pedro", "Marta"], muestra el último nombre. Si ese nombre es “Marta”, muestra “Nombre correcto”, si no, “Nombre diferente”. ----

# nom = [input(f"Ingresa un primer nombre: ") , input(f"Ingresa un segundo nombre: ") , input(f"Ingresa un tercer nombre: ") , input(f"Ingresa un cuarto nombre: ")]

# if nom[3] == "Marta" or nom[3] == "marta":
#     print(f"Nombre correcto! {nom[3]}")
# else:
#     print(f"Nombre incorrecto! {nom[3]}")

# 15 ---- Crea una lista con tres colores. Cambia el segundo color solo si es igual a "azul", y muestra la lista actualizada. ----

# list = [input(f"Ingresa un color: ") , input(f"Ingresa otro color: ") , input(f"Ingresa un último color: ")]

# if list[1] == "Azul" or list[1] == "azul":
#     list[1]="Púrpura"
#     print(f"La lista actualizada es: {list}")
# else:
#     print(f"La lista permanece igual")

# 16 ---- Crea una tupla con los valores (5, 8, 12, 20). Si el primer valor es menor que el último, muestra “Orden ascendente”, si no, “Orden descendente”. ----

# tup = (float(input(f"Ingrese un numero (1/4): ")) , float(input(f"Ingrese un numero (2/4): ")) , float(input(f"Ingrese un numero (3/4): ")) , float(input(f"Ingrese un numero (4/4): ")))

# if tup[0] < tup[3]:
#     print(f"Orden ascendente")
# else:
#     print(f"Orden descendente")

# 17 ---- Dada la tupla (25, 32, 28), verifica si el segundo valor es mayor a 30. Si lo es, muestra “Edad mayor a 30”, si no, “Edad menor o igual a 30”. ----

# tup = (int(input(f"Ingrese un numero (1/3): ")) , int(input(f"Ingrese un numero (2/3): ")) , int(input(f"Ingrese un numero (3/3): ")))

# if tup[1] > 30:
#     print(f"Edad ({tup[1]}) mayor a 30")
# else:
#     print(f"Edad ({tup[1]}) menor o igual a 30")

# 18 ---- Convierte la tupla (1, 2, 3) a lista, y cambia el segundo valor a 10 solo si es igual a 2, luego a convertirla a convertirla a tupla y muestrala ----

# tup = (int(input(f"Ingrese un numero (1/3): ")) , int(input(f"Ingrese un numero (2/3): ")) , int(input(f"Ingrese un numero (3/3): ")))

# list = list(tup)

# if list[1] == 2:
#     list[1] = 10
#     tup = tuple(list)
#     print(f"Numeros ingresados: {tup}")
# else:
#     tup = tuple(list)
#     print(f"Numeros ingresados: {tup}")

# 19 ---- Dada la tupla (4, 9), accede al segundo valor. Si es mayor que 5, muestra "Coordenada alta". sino, "Coordenada baja"

# tup = (int(input(f"Ingrese una coordenada: ")) , int(input(f"Ingrese otra coordenada: ")))

# if tup[1] > 5:
#     print(f"Coordenada alta: {tup[1]}")
# else:
#     print(f"Coordenada baja: {tup[1]}")

# 20 ---- Compara las tuplas (3, 4) y (3, 5) son iguales, Si lo son, muestra "Tuplas iguales", sino, "Tuplas diferentes"

# tup1 = (int(input(f"Ingrese un numero (1/2): ")) , int(input(f"Ingrese un numero (2/2): ")))
# tup2 = (int(input(f"-------------------------------------------\nIngrese otros numero (1/2): ")) , int(input(f"Ingrese otros numero (2/2): ")))

# if tup1 == tup2:
#     print(f"Tuplas iguales")
# else:
#     print(f"Tuplas diferentes")

# 21 ---- Crea un diccionario con {"nombre" : "Juan" , "edad" : 17}. Si la edad es mayor o igual a 18, muestra "Adulto", si no, muestra "Menor de edad"

# dat = {"nombre" : input(f"Ingresa tu nombre: ") , "edad" : int(input(f"Ingresa tu edad: "))}

# if dat["edad"] >= 18:
#     print(f"Hola {dat['nombre']}! Tienes {dat['edad']} años y eres adulto!")
# else:
#     print(f"Hola {dat['nombre']}! Tienes {dat['edad']} años y eres menor de edad!")

# 22

# dat = {"nombre" : input(f"Ingresa tu nombre: ") , "edad" : int(input(f"Ingresa tu edad: "))}

# if dat["edad"] > 18:
#     dat["edad"] = 21
#     print(f"Datos ingresados: {dat}")
# else:
#     print(f"Datos ingresados: {dat}")

# 23

# dat = {"nombre" : input(f"Ingresa su nombre: ")}

# if dat.get("ciudad") == None :
#     dat["ciudad"] = "Bogotá"
#     print(f"{dat}")
# else:
#     print(f"{dat}")

# 24

# dat = {"producto" : input(f"Ingresa el nombre del producto: ") , "precio" : float(input(f"Ingrese el precio: $"))}

# if dat.get("precio") == dat["precio"]:
#     print(f"El precio es: ${dat['precio']}")
# else:
#     print(f"No hay precio")    

# 25

# dat = {"producto" : input(f"Ingresa el nombre del producto: ") , "precio" : float(input(f"Ingrese el precio: $"))}

# if dat.get("producto") == dat["producto"]:
#     print(f"El precio de {dat['producto']} es: ${dat['precio']}")
# else:
#     print(f"Producto No Disponible")    

