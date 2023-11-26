from  Personal.vendedor import Login
from  Personal.consultor import Menu

def main():
    login_vendedor = Login()
    menu_consultor = Menu()
    while True: 
        try:
            print("Bienvenido")
            print("1. Administrador")
            print("2. Vendedor")
            print("3. Comprador")
            print("4. Consultor")
            print("5. Cliente")
            print("6. Salir")
        except:
            print("Opcion no valida, vuelva a intentar")
        else: 
                option = int(input("Ingrese la opcion: "))
                print()

                match option: 
                    case 1:
                        pass
                    case 2:
                        login_vendedor.login()
                    case 3: 
                        pass
                    case 4:
                        menu_consultor.menu()
                    case 5:
                        pass
                    case 6:
                        break
                    case default:
                        print("ERROR DE OPCION NO EXISTENTE")

if __name__ == "__main__":
    main()
