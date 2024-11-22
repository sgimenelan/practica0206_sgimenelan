#Escribir un programa que cree un diccionario vacío y lo vaya 
# llenado con información sobre una persona (por ejemplo nombre,
#  edad, sexo, teléfono, correo electrónico, etc.) que se le pida 
# al usuario. Cada vez que se añada un nuevo dato debe imprimirse 
# el contenido del diccionario.
datos = {}
informacion = ("nombre", "edad","sexo", "direccion", "telefono")
for i in informacion:
    datos[i] = input("Dime tu " + i + ": ")
    print(datos)