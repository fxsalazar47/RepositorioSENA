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

num1 = float(input(f"Ingresa un numero: "))
num2 = float(input(f"Ingresa un numero para dividirlo: "))
num3 = float(input(f"Ingresa otro numero para dividirlo: "))

if num1 % num2 == 0 and num1 %num3 == 0:
    print(f"{num1} es divisible entre {num2} y {num3}")
else:
    print(f"{num1} no es divisible entre {num2} y num{3}")