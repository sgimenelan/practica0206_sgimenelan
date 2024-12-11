#Escribir un programa que permita gestionar la base de datos de alumnado de un
#  classroom. Los alumnos y alumnas se guardarán en una lista que almacena un
# diccionario para cada alumno/a en el que la clave de cada alumno/a será su NIF,
#  y el valor será otro diccionario con los datos del alumno/a (nombre, apellidos,
#  teléfono, correo, aprobado), donde aprobado tendrá el valor True si ha aprobado
#  el módulo. El programa debe preguntar al usuario por una opción del siguiente
#  menú: (1) Añadir alumno/a, (2) Eliminar alumno/a, (3) Mostrar alumno/a,
# (4) Listar todo el alumnado, (5) Listar alumnado aprobado, (6) Terminar.
# En función de la opción elegida el programa tendrá que hacer lo siguiente:
#1-Preguntar los datos del alumno/a, crear un diccionario con los datos y añadirlo a la base de datos.
#2-Preguntar por el NIF del alumno/a y eliminar sus datos de la base de datos.
#3-Preguntar por el NIF del alumno/a y mostrar sus datos.
#4-Mostrar lista de todo el alumnado de la base de datos con su NIF y nombre.
#5-Mostrar la lista del alumnado aprobado de la base de datos con su NIF y nombre.
#6-Terminar el programa.
menu = ""
alumnos = {}
while True:
    print("(1) Añadir alumno/a, (2) Eliminar alumno/a, (3) Mostrar alumno/a,")
    menu = int(input("(4) Listar todo el alumnado, (5) Listar alumnado aprobado, (6) Terminar: "))
    dato_alumno = {}
    if menu == 1:
        print("***Añadir alumno/a***")
        informacion = ("nombre", "apellidos", "telefono", "correo", "aprobado")
        nif = input("Dime tu NIF: ")
        if nif in alumnos:
            print("El alumno ya esta en la base de datos")
        else:
            for i in informacion:
                if i != "aprobado":
                    dato_alumno[i] = input("Dime tu " + i + ": ")
                else:
                    dato_alumno[i] = float(input("Dime cual es tu nota: "))
                    if dato_alumno[i] >= 5:
                        dato_alumno[i] = True
                    else:
                        dato_alumno[i] = False
            alumnos[nif] = dato_alumno
            print("***AÑADIDO***")
    if menu == 2:
        print("***Eliminar alumno/a***")
        nif = input("Dime el NIF que quieres borrar: ")
        if nif in alumnos:
            alumnos.pop(nif)
            print("***ELIMINADO***")
        else:
            print("El NIF no esta en la base de datos")
    if menu == 3:
        print("***Mostrar alumno/a***")
        nif = input("Dime el NIF que quieres mostrar: ")
        if nif in alumnos:
            print(nif + ":", alumnos[nif])
        else:
            print("El NIF no esta en la base de datos")
    if menu == 4:
        print("***Todo el alumnado***")
        for i in alumnos.keys():
            print("NIF: " + i + " Nombre:", alumnos[i]["nombre"])
    if menu == 5:
        print("***Alumnado aprobado***")
        for i in alumnos.keys():
            if alumnos[i]["aprobado"] == True:
                print("NIF: " + i + " Nombre:", alumnos[i]["nombre"])
    if menu == 6:
        print("***TERMINADO***")
        break