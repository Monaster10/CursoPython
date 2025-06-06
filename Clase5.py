# Lista donde se guardarán los gastos (cada gasto es un diccionario con monto y categoría)
gastos = []

# Función para ingresar un nuevo gasto
def ingresar_gasto():
    try:
        monto = float(input("Ingrese el monto del gasto: $"))
        if monto <= 0:
            print("Error: El monto debe ser un número positivo.\n")
            return
        categoria = input("Ingrese la categoría del gasto (ej: comida, transporte, etc.): ")
        gastos.append({"monto": monto, "categoria": categoria})
        print("Gasto agregado correctamente.\n")
    except ValueError:
        print("Error: Ingrese un número válido para el monto.\n")

# Función para mostrar todos los gastos
def ver_gastos():
    if not gastos:
        print("No hay gastos registrados.\n")
        return
    print("Listado de gastos:")
    for i, gasto in enumerate(gastos, 1):
        print(f"{i}. ${gasto['monto']} - Categoría: {gasto['categoria']}")
    print()

# Función para calcular y mostrar el total de gastos
def ver_total_gastos():
    total = sum(gasto["monto"] for gasto in gastos)
    print(f"Total de gastos realizados: ${total:.2f}\n")

# Función principal con menú
def menu_gastos():
    while True:
        print("=== CONTROL DE GASTOS ===")
        print("1. Ingresar un gasto")
        print("2. Ver listado de todos mis gastos")
        print("3. Ver total de gastos realizados")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_gasto()
        elif opcion == "2":
            ver_gastos()
        elif opcion == "3":
            ver_total_gastos()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")

# Ejecutar el programa
menu_gastos()