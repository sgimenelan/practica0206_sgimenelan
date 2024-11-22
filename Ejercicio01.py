#Escribir un programa que guarde en una variable el diccionario
#  {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por 
# una divisa y muestre su símbolo o un mensaje de aviso si la divisa
#  no está en el diccionario.
divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("Dime la divisa: ")
if divisa in divisas:
    print(divisas[divisa])
else:
    print("Tu divisa no esta en el diccionario")