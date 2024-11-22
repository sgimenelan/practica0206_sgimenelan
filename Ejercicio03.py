#Escribir un programa que guarde en un diccionario los precios 
# de los artículos de la tabla, pregunte al usuario por un artículo,
#  un número de unidades y muestre por pantalla el precio de esa cantidad
#  de producto. Si el producto no está en el diccionario debe mostrar un
#  mensaje informando de ello.
productos = {"pan":1.40, "huevos":2.30, "cebolla":0.85, "aceite":4.35,}
producto = input("Dime el producto: ").lower()
cantidad = int(input("Dime la cantidad: "))
if producto in productos:
    precio = productos[producto] * cantidad
    print("El", producto, "te va a costar", precio, "€")
else:
    print("Tu producto no esta en la lista")
