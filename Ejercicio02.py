#Escribir un programa que pregunte al usuario su nombre,
#  edad, dirección y teléfono y lo guarde en un diccionario.
#  Después debe mostrar por pantalla el mensaje “<nombre> tiene 
# <edad> años, vive en <dirección> y su número de teléfono es <teléfono>”.
datos = {"nombre": "", "edad": "", "direccion": "", "telefono": ""}
for i in datos.keys():
    datos[i] = input("Dime tu " + i + ": ")
print(datos["nombre"], "tiene", datos["edad"], "años, vive en", 
      datos["direccion"], "y su numero de telefono es", datos["telefono"])