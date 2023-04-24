# Escribe un programa en Python que simule una agenda de contactos. El programa debe permitir al usuario realizar las siguientes acciones:
#- Ver todos los contactos guardados en la agenda, mostrando nombre, dirección y número de teléfono.
#- Buscar un contacto por su nombre y mostrar su información (dirección y número de teléfono).
#- Agregar un nuevo contacto, solicitando el nombre, dirección y número de teléfono al usuario.
#- Borrar un contacto existente, solicitando el nombre del contacto al usuario.
#- El programa debe mostrar un menú con estas opciones y permitir al usuario seleccionar la opción deseada.
#- El programa debe almacenar los contactos en una lista, donde cada contacto es un diccionario con las claves "nombre", "direccion" y "telefono"."

agenda=[]

while True:
    print("Seleccione una opción:")
    print("1. Ver todos los contactos")
    print("2. Buscar un contacto")
    print("3. Agregar un nuevo contacto")
    print("4. Borrar un contacto existente")
    print("5. Salir del programa")
    opcion = input("Ingrese la opción deseada: ")
    
    if opcion=="1":
        if len(agenda) == 0:
            print("La agenda está vacía")
            print("")
        else:
            print("Lista de contactos:")
            for contacto in agenda:
                print("Nombre: ", contacto["nombre"])
                print("Dirección: ", contacto["direccion"])
                print("Teléfono:" , contacto["telefono"])
                print("")
    elif opcion=="2":
        if len(agenda) == 0:
            print("La agenda está vacía")
            print("")
        else:
            encontrado=False
            nombre = input("Ingrese el nombre del contacto: ")
            for contacto in agenda:
                if contacto["nombre"].lower() == nombre.lower():
                    print("Información de contacto:")
                    print("Nombre:", contacto["nombre"])
                    print("Dirección:", contacto["direccion"])
                    print("Teléfono:", contacto["telefono"])
                    print("")
                    encontrado=True
                    break
            if not encontrado:            
                print("No se encontró ningún contacto con ese nombre.")
                print("")
    elif opcion=="3":
        nombre = input("Ingrese el nombre del contacto: ")
        direccion = input("Ingrese la dirección del contacto: ")
        telefono = input("Ingrese el número de teléfono del contacto: ")
        nuevo_contacto = {"nombre": nombre, "direccion": direccion, "telefono": telefono}
        agenda.append(nuevo_contacto)
        print("El contacto ha sido agregado a la agenda.")
        print("")
    elif opcion=="4":
        if len(agenda) == 0:
            print("La agenda está vacía")
            print("")
        else:
            no_encontrado=True
            nombre = input("Ingrese el nombre del contacto que desea borrar: ")
            for contacto in agenda:
                if contacto["nombre"].lower() == nombre.lower():
                    agenda.remove(contacto)
                    print("El contacto ha sido borrado de la agenda.")
                    print("")
                    no_encontrado=False
                    break
            if no_encontrado:
                print("No se encontró ningún contacto con ese nombre.")
                print("")
    elif opcion=="5":
        print("Chao pescao!!!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
        print("")
    

