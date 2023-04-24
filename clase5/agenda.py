# agenda 0032

agenda = []

continuar = True

while continuar:
    print("Elija una opcion:")
    print("1. Ver todos los contactos")
    print("2. Buscar un contacto")
    print("3. Agregar un contacto")
    print("4. Borrar un contacto")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        if len(agenda) == 0:
            print("La agenda esta vacia. ")
        else:
            print("Contactos en la agenda:")
            for contacto in agenda:
                print("Nombre: ", contacto["nombre"])
                print("Direccion: ", contacto["direccion"])
                print("Telefono: ", contacto["telefono"])
                print("")
    elif opcion == "2":
        if len(agenda) == 0:
            print("La agenda esta vacia. ")
        else:
            no_encontrado = True
            nombre_buscado = input("Ingrese el nombre a buscar: ")
            for contacto in agenda:
                if contacto["nombre"] == nombre_buscado:
                    print("Nombre: ", contacto["nombre"])
                    print("Direccion: ", contacto["direccion"])
                    print("Telefono: ", contacto["telefono"])
                    no_encontrado = False
                    break
            if no_encontrado:
                print("No se encontro el contacto")
    elif opcion == "3":
        nombre = input("Ingrese el nombre a guardar: ")
        direccion = input("Ingrese la direccion a guardar: ")
        telefono = input("Ingrese el telefono a guardar: ")
        contacto = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono
        }
        agenda.append(contacto)
        print("El contacto ha sido guardado exitosamente")
    elif opcion == "4":
        if len(agenda) == 0:
            print("La agenda esta vacia. ")
        else:
            nombre_buscado = input("Ingrese el nombre a eliminar: ")
            no_encontrado = True
            for i in range(len(agenda)):
                if agenda[i]["nombre"] == nombre_buscado:
                    del agenda[i]
                    no_encontrado = False
                    print("El contacto fue eliminado")
                    break
            if no_encontrado:
                print("no se encontro un contacto con ese nombre")
    elif opcion == "5":
        print("chao")
        continuar = False
    else:
        print("Opcion invalida")
