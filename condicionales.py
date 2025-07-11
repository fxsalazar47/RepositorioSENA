#git if else

#ejemplo: verificar si un numero es positivo, negativo o cero

# N = float(input(f"Ingerse un numero: "))

# if N > 0:
#     print(f"Positivo porque es {N}")
# elif N < 0:
#     print(f"Negativo porque es {N}")
# else:
#     print(f"Es cero porque {N}")

# calcula el mayor de dos numeros ingresados

# n1 = float(input(f"Ingresa un primer numero: "))
# n2 = float(input(f"Ingresa un segundo numero: "))

# if n1 > n2:
#     print(f"El numero {n1} es mayor que {n2}")
# elif n2 >n1:
#     print(f"El numero {n2} es mayor que {n1}")

#  -------- Taller Condicionales --------

# 1 -----

# num = float(input(f"Ingresa un numero: "))

# if num > 0:
#     print(f"El numero {num} es positivo")

# elif num < 0:
#     print(f"El numero {num} es negativo")

# else:
#     print(f"El numero es 0")

# 2 ----

# N1 = float(input(f"Ingresa un primer numero: "))
# N2 = float(input(f"Ingresa un segundo numero: "))

# if N1 > N2:
#       print(f"El numero {N1} es mayor que {N2}")
# else:
#       print(f"El numero {N2} es mayor que {N1}")

# 3 ----

# num = int(input(f"Ingrese un numero entero: "))

# if num % 2 == 0:
#       print(f"El numero {num} es par")
# else:
#       print(f"El numero {num} es impar")

# 4 ----

# num = float(input(f"Ingrese un número: "))

# if 10 <= num <= 20:
#     print(f"El numero {num} esta entre 10 y 20")
# else: 
#     print(f"El numero {num} no está entre 10 y 20")

# 5 ----

# num = [float(input(f"Ingresa un primer numero: ")) , float(input(f"Ingresa un segundo numero: ")) , float(input(f"Ingresa un tercer numero: "))] 

# if num[0] > num[1] and num[0] > num[2]:
#     print(f"El número {num[0]} es mayor que {num[1]} y {num[2]}")
# elif num[1] > num[0] and num[1] > num[2]:
#     print(f"El numero {num[1]} es mayor que {num[0]} y {num[2]}")
# else:
#     print(f"El numero {num[2]} es mayor que {num[0]} y {num[1]}")

# 6 ----

# prec = float(input(f"Ingresa el precio de un producto: "))
# prec10 = prec - (prec * 0.1)
# if prec > 100: 
#     print(f"El precio final del producto con 10% de descuento es {prec10}")
# else:
#     print(f"El precio final sin el 10% de descuento es: {prec}")

# 7 ----

# edad = int(input(f"Ingresa tu edad: "))

# if edad >= 18:
#     print(f"El ciudadano puede votar")
# else:
#     print(f"El ciudadano no puede votar")

# 8 ----

# tp = (float(input(f"Ingrese el precio de producto: ")) , input(f"Eres cliente VIP? (Si/No): "))

# tp20 = tp[0] - (tp[0] * 0.2)

# if tp[1] == "Si":
#     print(f"El precio total con el descuento VIP del 20% es {tp20}")
# else:
#     print (f"El precio total sin el descuento VIP es de {tp[0]}")

# 9 ----

# num = float(input(f"Ingresa un numero: "))

# if num % 3 == 0 and num % 5 == 0:
#     print(f"El numero {num} es multiplo de 3 y 5")
# else:
#     print(f"El numero {num} no es múltiplo de 3 y 5")

# 10 ----

# num1 = float(input(f"Ingresa un numero: "))
# num2 = float(input(f"Ingresa un numero para dividirlo: "))
# num3 = float(input(f"Ingresa otro numero para dividirlo: "))

# if num1 % num2 == 0 and num1 %num3 == 0:
#     print(f"{num1} es divisible entre {num2} y {num3}")
# else:
#     print(f"{num1} no es divisible entre {num2} y num{3}")

# ------- TALER 2 ----------------

# 1 ---- Pide tu edad y muestra si eres menor de edad, mayor de edad o adulto mayor (65+).

# edad = int(input(f"Ingresa tu edad: "))

# if edad <= 17:
#     print(f"Eres menor de edad")
# elif edad >=18 and edad < 65:
#     print("Eres mayor de edad")
# else:
#     print("Eres un adulto mayor")

# 2 ---- Solicita tu estatura en metros. Si mide menos de 1.5 m, eres considerado bajo; entre 1.5 y 1.8 m, estatura media; más de 1.8 m, alto

# est = float(input(f"Ingresa tu estatura en metros (m): "))

# if est < 1.5:
#     print(f"Por tu estatura de {est}m eres considerado bajo (Menos de 1.5m)")
# elif est >= 1.5 and est < 1.8:
#     print(f"Por tu estatura de {est}m eres considerado de estatura media")
# else:
#     print(f"Por tu estatura de {est}m eres considerado alto")

# 3 ---- Ingresa un número y muestra si es múltiplo de 2, de 3, o de ninguno.

# num = float(input(f"Ingresa un numero: "))

# if num % 3 == 0 and num % 2 == 0:
#     print(f"El numero ingresado ({num}) es multiplo de 2 y 3")
# elif num % 3 == 0 or num % 2 == 0:
#     print(f"El numero ingresado ({num}) es multiplo de 2 o de 3")
# else:
#     print(f"El numero ingresado ({num} no es multiplo ni de 2 ni de 3)")

# 4 ---- Pide un número decimal y determina si tiene 1, 2 o más de 2 decimales (usa str() y split()).

# num = input("Ingresa un número decimal: ")
# partes = num.split(".")

# if len(partes) == 2:
#      decimales = partes[1]
#      if len(decimales) == 1:
#          print(f"El número {num} tiene 1 decimal.")
#      elif len(decimales) == 2:
#          print(f"El número {num} tiene 2 decimales.")
#      else:
#          print(f"El número {num} tiene más de 2 decimales.")

# else:
#     print(f"El numero no tiene decimales")

# 5 ---- Solicita un país y muestra si está en la siguiente tupla: ("Colombia", "Perú", "Argentina", "México").

# tppais = ("Colombia", "Peru", "Argentina", "Mexico")
# pais = input("Ingresa un país: ")

# if pais in tppais:
#     print(f"El país ingresado ({pais}) está en la tupla de países (Colombia, Peru, Argentina, Mexico).")
# else:
#     print(f"El país ingresado ({pais}) NO está en la tupla de países (Colombia, Peru, Argentina, Mexico).")

# 6 ---- Pide tu tipo de sangre (A, B, AB, O) y muestra tu compatibilidad según un diccionario predefinido.

# comp = {"A": "A, O",
#     "B": "B, O",
#     "AB": "A, B, AB, O",
#     "O": "O"}

# tipsangre = input("Ingresa tu tipo de sangre (A, B, AB, O): ")

# if tipsangre == "A":
#     print("Tu sangre es compatible con:", comp["A"])
# elif tipsangre == "B":
#     print("Tu sangre es compatible con:", comp["B"])
# elif tipsangre == "AB":
#     print("Tu sangre es compatible con:", comp["AB"])
# elif tipsangre == "O":
#     print("Tu sangre es compatible con:", comp["O"])
# else:
#     print("Tipo de sangre no reconocido")

# 7 ---- Ingresa una temperatura en °C. Si es menor de 10, hace frío. Si está entre 10 y 25, templado. Más de 25, hace calor.

# temp = float(input(f"Ingresa una temperatura (°C): "))

# if temp < 10:
#     print(f"Hace frio!")
# elif temp >= 10 and temp < 25:
#     print(f"La temperatura es templada")
# else:
#     print(f"Hace calor!")

# 8 ---- Crea un menú con opciones 1. Sumar, 2. Restar, 3. Multiplicar. Pide dos números y ejecuta la operación seleccionada.

# num1 = float(input(f"Ingresa un número: "))
# num2 = float(input(f"Ingresa otro numero: "))

# menuop = {"1": (num1 + num2) , "2" : (num1 - num2) , "3": (num1 * num2)}

# men = int(input(f"Qué operacion quieres realizar?:\n1- Suma\n2- Resta\n3- Multiplicacion\n"))

# if men == 1:
#     print(f"El resultado de la suma es: {menuop['1']}")
# elif men == 2:
#     print(f"El resultado de la resta es: {menuop['2']}")
# else:
#     print(f"El resultado de la multiplciacion es: {menuop['3']}")

# 9 ---- Pide un número entre 1 y 12 y muestra el mes correspondiente usando un diccionario.

# num = int(input(f"Ingresa un numero del 1 al 12: "))

# meses = {"1" : "Enero",
#          "2" : "Febrero",
#          "3" : "Marzo",
#          "4" : "Abril",
#          "5" : "Mayo",
#          "6" : "Junio",
#          "7" : "Julio",
#          "8" : "Agosto",
#          "9" : "Septiembre",
#          "10" : "Octubre",
#          "11" : "Noviembre",
#          "12" : "Diciembre"}

# if num == 1:
#     print(f"El mes es {meses["1"]}")
# elif num == 2:
#     print(f"El mes es {meses["2"]}")
# elif num == 3:
#     print(f"El mes es {meses["3"]}")
# elif num == 4:
#     print(f"El mes es {meses["4"]}")
# elif num == 5:
#     print(f"El mes es {meses["5"]}")
# elif num == 6:
#     print(f"El mes es {meses["6"]}")
# elif num == 7:
#     print(f"El mes es {meses["7"]}")
# elif num == 8:
#     print(f"El mes es {meses["8"]}")
# elif num == 9:
#     print(f"El mes es {meses["9"]}")
# elif num == 10:
#     print(f"El mes es {meses["10"]}")
# elif num == 11:
#     print(f"El mes es {meses["11"]}")
# elif num == 12:
#     print(f"El mes es {meses["12"]}")
# else:
#     print(f"Mes no reconocido")

# 10 ---- Solicita un número de 4 dígitos y determina si comienza con 1, 2 o cualquier otro.

# num = input(f"Ingresa un numero de 4 digitos: ")

# if num[0] == "1":
#     print(f"El primero de los 4 digitos comienza por 1")
# elif num[1] == "2":
#     print(f"El priemero de los 4 digitos comienza por 2")
# else:
#     print(f"El primero de los 4 digitos es diferente de 1 y 2")

# 11 ---- Ingresa una palabra. Muestra si su primera letra es vocal, consonante o un número. 

# pal = input("Ingresa una palabra: ")

# tipo = {
#     "vocales": ["a", "e", "i", "o", "u"],
#     "consonantes": ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"],
#     "numeros": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# }

# primeral = pal[0]

# if primeral in tipo["vocales"]:
#     print("La primera letra es una vocal.")
# elif primeral in tipo["consonantes"]:
#     print("La primera letra es una consonante.")
# elif primeral in tipo["numeros"]:
#     print("La primera letra es un número.")
# else:
#     print("La primera letra no es una vocal, consonante ni número.")

# 12 ---- Pide una fruta. Si está en la lista ["manzana", "pera", "piña"], muestra su precio. Si no, indica que no está disponible

# frutas = ["manzana", "pera", "piña"]
# precios = [1500, 1200, 2000]

# fruta = input("Ingresa una fruta: ")

# if fruta == frutas[0]:
#     print("Precio: $", precios[0])
# elif fruta == frutas[1]:
#     print("Precio: $", precios[1])
# elif fruta == frutas[2]:
#     print("Precio: $", precios[2])
# else:
#     print("Fruta no disponible.")

# 13 ---- Pide tu calificación (0 a 5). Si es menor que 3, reprobado. Entre 3 y 4, aprobado. Mayor a 4, excelente.

# cal = int(input(f"Ingresa tu calificación (0 a 5): "))

# if cal < 3:
#     print(f"Tu calificacion fue {cal} y reprobaste")
# elif cal >= 3 and cal < 4:
#     print(f"Tu calificacion fue {cal} y aprobaste!")
# else:
#     print(f"Tu calificacion fue {cal}, excelente!")

# 14 ---- Pide un número y muestra si es divisible entre 4, entre 6, o no lo es.

# nm = float(input(f"Ingresa un numero: "))

# if nm % 4 == 0 and nm % 6 == 0 :
#     print(f"El numero {nm} es divisible entre 4 y 6")
# else:
#     print(f"El numero no es divisible entre 4 ni 6")

# 15 ---- Crea un sistema de autenticación básico. Pide usuario y clave. Usa un diccionario para validar.

# datos = {
#     "usuario": input("Crea tu nombre de usuario: "),
#     "clave": int(input("Crea tu clave numérica: "))
# }

# print("Tus datos fueron guardados correctamente.\n")

# usuario_ingresado = input("Ingresa tu usuario: ")
# clave_ingresada = int(input("Ingresa tu clave: "))

# if usuario_ingresado == datos["usuario"] and clave_ingresada == datos["clave"]:
#     print("Acceso concedido.")
# else:
#     print("Acceso denegado.")

# 16 ---- Solicita una edad y muestra a qué grupo pertenece: niño (0-12), adolescente (13-17), adulto (18-64), mayor (65+).

# ed = int(input(f"Ingresa tu edad: "))

# if ed <= 12:
#     print(f"Tu edad es {ed} y eres un niño")
# elif ed >= 13 and ed <= 17:
#     print(f"Tu edad es {ed} y eres un adolescente")
# elif ed >= 18 and ed <= 64:
#     print(f"Tu edad es {ed} y eres un adulto")
# else:
#     print(f"Tu edad es {ed} y eres un adulto mayor")

# 17 ---- Pide el nombre de una ciudad. Si está en una tupla, muestra que es capital; si no, muestra “ciudad secundaria”.

# ciu = input(f"Ingresa el nombre de una ciudad de Colombia (Primera letra en mayúscula): ")

# cap = ("Leticia",  "Medellín","Arauca","Barranquilla","Cartagena","Tunja","Manizales","Florencia","Yopal","Popayán","Valledupar","Quibdó" "Montería","Bogotá","Inírida","San José del Guaviare","Neiva","Riohacha","Santa Marta","Villavicencio","Pasto","San Andrés","Cúcuta","Mocoa","Armenia","Pereira","Sincelejo","Ibagué","Cali","Mitú","Puerto Carreño")

# if ciu in cap:
#     print(f"{ciu} es una ciduad capital")
# else:
#     print(f"{ciu} es una ciudad secundaria")

# 18 ---- Ingresa el valor de una compra. Si es mayor de $200.000 aplica un 15% de descuento. Entre $100.000 y $200.000 aplica 10%. Si es menor, no hay descuento.

# compra = float(input("Ingresa el valor de la compra: "))

# desc15 = compra - (compra * 0.15)

# desc10 = compra - (compra * 0.10) 

# if compra > 200000:
#     print(f"El total a pagar con 15% de descuento es: ${desc15}")
# elif compra >= 100000 and compra <= 200000:
#     print(f"El total a pagar con 15% de descuento es: ${desc10}")

# else:
#     print(f"Tu compra fue de ${compra} y no tiene descuento") 

# 19 ---- Pide el nombre y el número de horas trabajadas. Calcula el salario con tarifa de $10.000/hora. Si trabajó más de 40 horas, aplica un bono del 20%.

# nombre = input("Ingresa tu nombre: ")
# horas = int(input("Ingresa el número de horas trabajadas: "))

# salario = horas * 10000
# bono = salario + (salario * 0.20)

# if horas > 40:
#     print(f"El salario de {nombre} es: ${bono}")
# else:
#     print(f"El salario de {nombre} es: ${salario}")

# 20 ---- 0. Ingresa tu puntaje en una prueba (0 a 100). Si es menor a 50, insuficiente. De 50 a 79, aceptable. 80 a 100, sobresaliente.

nota = int(input(f"Ingresa tu nota (0-100): "))

if nota < 50:
    print(f"Tu calificacion es {nota} y es insuficente")
elif nota >= 50 and nota <= 79:
    print(f"Tu calificacion es {nota} y es aceptable")
else:
    print(f"Tu calificación es {nota} y es sobresaliente")