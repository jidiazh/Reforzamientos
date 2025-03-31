# Diccionario inicial con facturas pendientes (Número de factura -> Monto)
facturas = {"00054": 1200.50,"00055": 850.75, "00056": 635.00}

# Función para mostrar las facturas actuales
def mostrar_facturas():
    print("Facturas pendientes:")
    if facturas:
        for num, monto in facturas.items():
            print(f"Factura {num}: S/. {monto:.2f}")
    else:
        print("No hay facturas pendientes.")

# Bucle principal del programa
while True:
    print("Opciones:")
    print("1. Agregar nueva factura")
    print("2. Pagar factura")
    print("3. Mostrar facturas pendientes")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        num_factura = input("Ingrese el número de la nueva factura: ")
        if num_factura in facturas:
            print("Esta factura ya existe en el sistema.")
        else:
            try:
                monto = float(input("Ingrese el costo de la factura: "))
                facturas[num_factura] = monto
                print("Factura agregada con éxito.")
            except ValueError:
                print("Error: Ingrese un monto válido.")

    elif opcion == "2":
        num_factura = input("Ingrese el número de factura que desea pagar: ")
        if num_factura in facturas:
            del facturas[num_factura]
            print("La factura {} ha sido cancelada.".format(num_factura))
        else:
            print("El número de factura no existe.")

    elif opcion == "3":
        mostrar_facturas()

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Intente de nuevo.")

    # Mostrar el diccionario actualizado después de cada operación
    mostrar_facturas()
