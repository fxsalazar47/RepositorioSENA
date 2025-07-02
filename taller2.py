# TALLER DE APLICACION

# - 1 -

# lista = []
# print(lista)

# num1 = float(input(f"Ingrese el primer numero: "))
# num2 = float(input(f"Ingrese el segundo numero: "))
# num3 = float(input(f"Ingrese el tercer numero: "))

# lista.append(num1)
# lista.append(num2)
# lista.append(num3)

# promedio = (lista[0] + lista[1] + lista[2]) / 3

# print(f"El promedio de los tres numeros es {promedio}")

# - 2 -

# productos = {"Leche" : 4500 , "Pan" : 3000 , "Huevo" : 600}
# print(productos)

# aument = float(input(f"Ingrese un porcentaje de aumento (%): "))

# productos["Leche"] += productos["Leche"] * (aument/100)
# productos["Pan"] += productos["Pan"] * (aument/100)
# productos["Huevo"] += productos["Huevo"] * (aument/100)

# print(f"El precio de los productos con un aumento del {aument}% es {productos}")

# - 3 -

# tuplatemp = ()

# listatemp = list(tuplatemp)

# temp1 = float(input(f"Ingrese la temperatura del primer dia (°C): "))
# temp2 = float(input(f"Ingrese la temperatura del segundo dia (°C): "))
# temp3 = float(input(f"Ingrese la temperatura del tercer dia (°C): "))
# temp4 = float(input(f"Ingrese la temperatura del cuarto dia (°C): "))
# temp5 = float(input(f"Ingrese la temperatura del quinto dia (°C): "))

# listatemp.append(temp1)
# listatemp.append(temp2)
# listatemp.append(temp3)
# listatemp.append(temp4)
# listatemp.append(temp5)

# fahr1 = (listatemp[0] * 9/5) + 32
# fahr2 = (listatemp[1] * 9/5) + 32
# fahr3 = (listatemp[2] * 9/5) + 32
# fahr4 = (listatemp[3] * 9/5) + 32
# fahr5 = (listatemp[4] * 9/5) + 32

# listatemp[0] = fahr1
# listatemp[1] = fahr2
# listatemp[2] = fahr3
# listatemp[3] = fahr4
# listatemp[4] = fahr5

# tuplatemp = tuple(listatemp)
# print(f"Las temperaturas en °F: {tuplatemp}")

# - 4 -

# listaedades = [int(input(f"Edad 1: ")), int(input(f"Edad 2: ")), int(input(f"Edad 3: ")), int(input(f"Edad 4: ")), int(input(f"Edad 5: "))]

# print(listaedades)

# promedio = sum(listaedades) / 3

# print(f"La mayor edad es {max(listaedades)}, la menor es {min(listaedades)} y el promedio de todas las edades es {promedio}")

# - 5 -

# frutas = {"Manzana" : 2000 , "Pera" : 1750 , "Mango" : 3250}
# print(frutas)

# valortotal = [float(input(f"Cuantos kilos de manzana deseas?: ")), float(input(f"Cuantos kilos de pera deseas??: ")), float(input(f"Cuantos kilos de mango deseas?: "))]

# frutas["Manzana"] = (frutas["Manzana"]) * (valortotal[0])
# frutas["Pera"] = (frutas["Pera"]) * (valortotal[1])
# frutas["Mango"] = (frutas["Mango"]) * (valortotal[2])

# sm = frutas["Manzana"] + frutas["Pera"] + frutas["Mango"]

# print(f"El valor total de todos los kilos de fruta es: ${sm}")

# - 6 - 

# tupla = (int(input(f"Ingrese un numero (1/5): ")),int(input(f"Ingrese un numero (2/5): ")), int(input(f"Ingrese un numero (3/5): ")), int(input(f"Ingrese un numero (4/5): ")),int(input(f"Ingrese un numero (5/5): ")))

# suma = tupla[0] + tupla[1] + tupla[2] + tupla[3] + tupla[4]

# print(f"La suma total de los elementos de la tupla es: {suma}")

# - 7 -

# inv = [{"Nombre1" : (input(f"Ingrese el nombre para el primer producto: ")), "Cantidad1" : int(input(f"Ingrese la cantidad para el primer producto: ")), "Precio1" : float(input(f"Ingrese el precio para el primer producto: "))} 
#        , {"Nombre2" : (input(f"\nIngrese el nombre para el segundo producto: ")), "Cantidad2" : int(input(f"Ingrese la cantidad para el segundo producto: ")), "Precio2" : float(input(f"Ingrese el precio para el segundo producto: "))} 
#        , {"Nombre3" : (input(f"\nIngrese el nombre para el tercer producto: ")), "Cantidad3" : int(input(f"Ingrese la cantidad para el tercer producto: ")), "Precio3" : float(input(f"Ingrese el precio para el tercer producto: "))} ]

# print(inv) 

# - 8 -

# lista = [float(input(f"Ingresa un primer precio: ")) , float(input(f"Ingresa un segundo precio: ")) , float(input(f"Ingresa un tercer precio: ")) , float(input(f"Ingresa un cuarto precio: ")) , float(input(f"Ingresa un quinto precio: "))]

# desc = float(input(f"Ingresa un descuento(%): "))

# lista[0] = (lista[0] * desc) / 100
# lista[1] = (lista[1] * desc) / 100
# lista[2] = (lista[2] * desc) / 100
# lista[3] = (lista[3] * desc) / 100
# lista[4] = (lista[4] * desc) / 100

# print(f"los precios con descuento son: {lista}")

# - 9 - 

# tupla = (float(input(f"Ingresa tu primer nota: ")) , float(input(f"Ingresa tu segunda nota: ")) , float(input(f"Ingresa tu tercera nota: ")) , float(input(f"Ingresa tu cuarta nota: ")) )

# print(f"La nota mas alta fue {max(tupla)} y la menor fue {min(tupla)}")

# - 10 -

# conv = {"km" : float(input(f"Ingresa una medida en km: ")) , "m" : float(input(f"Ingresa una medida en m: ")) , "cm" : float(input(f"Ingresa una medida en cm: "))}

# conv["km"] = conv["km"] * 1000
# conv["cm"] = conv["cm"] / 100

# print(f"Las medidas en km y cm convertidas a m son: {conv['km']}km y {conv["cm"]}cm")

# - 11 - 

# listaprecios = [float(input(f"Ingresa del primer producto: ")) , float(input(f"Ingresa del segundo producto: ")) , float(input(f"Ingresa del tercer producto: "))]

# listaIVA = []

# listaIVA.append(listaprecios[0] + ((listaprecios[0] * 19) / 100))
# listaIVA.append(listaprecios[1] + ((listaprecios[1] * 19) / 100))
# listaIVA.append(listaprecios[2] + ((listaprecios[2] * 19) / 100))

# print(f"La lista de precios con IVA del 19% es: {listaIVA}")

# - 12 - 

# listnum = [float(input(f"Ingresa un primer numero: ")) , float(input(f"Ingresa un segundo numero: "))]

# tuplanum = (listnum[0] + listnum[1] , listnum[0] - listnum[1] , listnum[0] * listnum[1] , listnum[0] / listnum[1])

# print(f"Las operaciones matematicas basicas (suma, resta, multiplicación y division respectivamente) con estos dos numeros son: {tuplanum}")

# - 13 -

# est = {"Juan" : float(input(f"Ingresa la nota del primer estudiante: ")) , "Andrés" : float(input(f"Ingresa la nota del segundo estudiante: ")) , "Pedro" : float(input(f"Ingresa la nota del tercer estudiante: "))}

# prom = (est["Juan"] + est["Andrés"] + est["Pedro"]) / 3

# print(f"El promedio general de las notas es {prom}")

# - 14 - 

# sal1 = [float(input(f"Ingresa un primer salario: ")) , float(input(f"Ingresa un segundo salario: ")) , float(input(f"Ingresa un tercer salario: ")) , float(input(f"Ingresa un cuarto salario: ")) , float(input(f"Ingresa un quinto salario: "))]

# sal2 = []

# sal2.append(sal1[0] + ((sal1[0] * 10) / 100))
# sal2.append(sal1[1] + ((sal1[1] * 10) / 100))
# sal2.append(sal1[2] + ((sal1[2] * 10) / 100))
# sal2.append(sal1[3] + ((sal1[3] * 10) / 100))
# sal2.append(sal1[4] + ((sal1[4] * 10) / 100))

# print(f"Los salarios con el aumento del 10% son: {sal2}")

# - 15 - 

# prec = {"Producto_1" : float(input(f"Ingresa el precio del primer producto: ")) , "Producto_2" : float(input(f"Ingresa el precio del segundo producto: ")) , "Producto_3" : float(input(f"Ingresa el precio del tercer producto: ")) , "Producto_4" : float(input(f"Ingresa el precio del cuarto producto: ")) , "Producto_5" : float(input(f"Ingresa el precio del quinto producto: "))}

# perc = float(input(f"Ingresa el porcentaje de impuesto a agregar: "))

# prec["Producto_1"] = prec["Producto_1"] + (prec["Producto_1"] * perc) / 100
# prec["Producto_2"] = prec["Producto_2"] + (prec["Producto_2"] * perc) / 100
# prec["Producto_3"] = prec["Producto_3"] + (prec["Producto_3"] * perc) / 100
# prec["Producto_4"] = prec["Producto_4"] + (prec["Producto_4"] * perc) / 100
# prec["Producto_5"] = prec["Producto_5"] + (prec["Producto_5"] * perc) / 100

# print(f"Los precios con un impuesto del {perc}% es de {prec}")

# - 16 -

liste = [int(input(f"Ingresa una edad(1/4): ")) , int(input(f"Ingresa una edad(2/4): ")) , int(input(f"Ingresa una edad(3/4): ")) , int(input(f"Ingresa una edad(4/4): "))]
print(liste)

list1 = liste.copy()

list1[0] =list1[0]-18
list1[1] =list1[1]-18
list1[2] =list1[2]-18
list1[3] =list1[3]-18

print(f"Las personas menores de edad son aquellas que tengan un numero negativo: {list1}")

# - 17 - 

# dolares = float(input(f"Ingresa la cantidad en doalres: "))

# euros = dolares * 0.85
# pesos = dolares * 4000
# yenes = dolares * 110

# conversion = (euros , pesos , yenes)

# print(F"Conversion de ${dolares} dolares en euros, pesos y yenes: E{conversion}")

# - 18 - 

# dexvent = {"Producto_1" : int(input(f"Ingresa la cantidad de ventas del primer producto: ")) , "Producto_2" : int(input(f"Ingresa la cantidad de ventas del segundo producto: ")) , "Producto_3" : int(input(f"Ingresa la cantidad de ventas del tercer producto: "))}

# sum = dexvent["Producto_1"] + dexvent["Producto_2"] + dexvent["Producto_3"]

# print(f"La cantidad total de productos vendidos es de: {sum}")

# - 19 - 

# temp1 = 35
# temp2 = 8
# temp3 = 15
# temp4 = 31
# temp5 = 5
# temp6 = 22
# temp7 = 40
# temp8 = 9
# temp9 = 29
# temp10 = 10

# print(f"Temperaturas mayores a 30: {temp1}, {temp4}, {temp7}")
# print(f"Temperaturas menores a 10: {temp2}. {temp5}, {temp8}")

# - 20 - 

#prec = [float(input(f"Ingresa un primer precio: ")) , float(input(f"Ingresa un segundo precio: ")) , float(input(f"Ingresa un tercer precio: ")) , float(input(f"Ingresa un cuarto precio: ")) , float(input(f"Ingresa un quinto precio: "))]

# print(prec)

# delet = int(input(f"Elige que numero de la lista quieres eliminar (0,1,2,3,4): "))

# prec.pop(delet)

# prec.append(float(input(f"Agrega un nuevo precio: ")))

# prec.sort()

# print(f"Los precios de la lista ordenados son: {prec}")
