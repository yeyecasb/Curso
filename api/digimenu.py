from cliente_api import DigimonAPI

class DigiMenu:
    def __init__(self):
        self.api = DigimonAPI()

    def print_menu(self):
        print("-----------------------MENU-----------------------")
        print("  *  *  *  *  CONSULTA DE DIGIMON  *   *   *  *")
        print("-------------------------------------------------")
        print("1. Listar todos los Digimons")
        print("2. Buscar Digimon por nombre")
        print("3. Buscar Digimon por nivel")
        print("4. Salir")
        print("-------------------------------------------------")

    def run(self):
        while True:
            self.print_menu()
            choice = input("Ingrese una opción: ")

            if choice == "1":
                dict_digimon = self.api.get_all_digimon()
                print("------------------")
                for digimon in dict_digimon:
                    print(f"Nombre: {digimon['name']}")
                    print(f"Nivel: {digimon['level']}")
                    print("")
                print("------------------")
            
            elif choice == "2":
                name = input("Ingrese el nombre del Digimon: ")
                dict_digimon = self.api.get_digimon_by_name(name)
                if len(dict_digimon) == 0:
                    print("Digimon no encontrado")
                else:
                    for digimon in dict_digimon:
                        print(f"Nombre: {digimon['name']}")
                        print(f"Nivel: {digimon['level']}")
                        print("")
                    print("------------------")

            elif choice == "3":
                name = input("Ingrese el niveldel Digimon: ")
                dict_digimon = self.api.get_digimon_by_level(name)
                if len(dict_digimon) == 0:
                    print("Digimon no encontrado")
                else:
                    for digimon in dict_digimon:
                        print(f"Nombre: {digimon['name']}")
                        print(f"Nivel: {digimon['level']}")
                        print("")
                    print("------------------")
            
            elif choice == "4":
                break

            else:
                print("Opción inválida, ingrese una opción válida")

