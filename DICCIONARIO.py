
# persona = {
#     "nombre" : "carlos",
#     "edad" : 30,
#     "ciudad" : "palmira"
# }

#--------------------------

# auto = {
#     "marca" : "Ford",
#     "modelo" : "Mustang",
#     "año" : 2022 ,
#     "placa" : "KGA201" 
# }

# # acceder a valores

# print(auto["modelo"])

# # modificar valores

# auto["año"] = 2023
# print(auto["año"])

# # añadir elementos

# auto["color"] = "Rojo"

# print(auto)

# # eliminar elementos (se puede usar del y .pop)

# del auto["modelo"]
# auto.pop("marca")

# print(auto)

# "del" elimina el par clave-valor directamente - no devuelve nada - si la clave no existe manda eror

#ejemplo

carro = {"marca" : "Toyota", "modelo" : "Corolla"}
valor = carro.pop("marca")
print(valor)
print(carro)

#-----------------------------------------------------

