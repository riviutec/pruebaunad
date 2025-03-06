""" crear una funcion de menu para mostrar opciones"""
def menu():
    print("1. Suma \n 2. Resta \n 3. Multiplicacion \n 4. Division \n 0. Salir")
    opcion = input("Ingrese una opcion: ")
    return opcion

# llamar a la funcion menu

op = True
while op:
    opcion = menu()
    if opcion == "1":
        print("Suma")
    elif opcion == "2":
        print("Resta")
    elif opcion == "3":
        print("Multiplicacion")
    elif opcion == "4":
        print("Division")
    elif opcion == "0":
        print("Salir")
        op = False
    else:
        print("Opcion invalida")
        op = False
print("Fin del programa")

""" fin del programa un comentario para la posteridad"""

