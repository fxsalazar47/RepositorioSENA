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

list = [float(input(f"Ingrese un primer numero: ")) , float(input(f"Ingrese un segundo numero: ")) , float(input(f"Ingrese un tercer numero: ")) , float(input(f"Ingrese un cuarto numero: "))]

if list[0] + list[1] > 10:
    print(f"Suma alta")
else:
    print("Suma baja")

