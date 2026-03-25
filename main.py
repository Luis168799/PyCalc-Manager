
# Autor: Luis
# Proyecto: PyBudget & Calc Tool
# Derechos Reservados © 2026

def calculadora(num1, num2, op):
    print("Bienvenido a la calculadora de Luis".center(50,'-'))
    if op == 1:
        print(f"El resultado de la suma de {num1} y {num2} es: {num1 + num2}")
    elif op == 2:
        print(f"El resultado de la resta de {num1} y {num2} es: {num1 - num2}")
    elif op == 3:
        print(f"El resultado de la multiplicación de {num1} y {num2} es: {num1 * num2}")
    elif op == 4:
        if num2 != 0:
            print(f"El resultado de la división de {num1} y {num2} es: {num1 / num2}")
        else:
            print("No se puede dividir entre cero.")
    else:
        print("Te equivocaste de opción.")

PIN_CONSTRASEÑA = "1234"

def gestor_de_gastos():
    saldo = 0.0
    nombre_archivo = "historial.txt"

    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if "+" in linea:
                    monto = float(linea.split("$")[1])
                    saldo += monto
                elif "-" in linea:
                    monto = float(linea.split("$")[1])
                    saldo -= monto
        print("¡Historial previo cargado con éxito!")
    except FileNotFoundError:
        print("No se encontró historial previo. Iniciando desde cero.")

    while True:
        print(f"\n--- SALDO ACTUAL: ${saldo:.2f} ---")
        print("1. Agregar Ingreso (+)")
        print("2. Registrar Gasto (-)")
        print("3. Ver Historial Completo")
        print("4. Salir")
        print("5. Borrar todo el historial (Reset)")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            monto = float(input("Monto a ingresar: "))
            saldo += monto
            with open(nombre_archivo, "a") as archivo:
                archivo.write(f"Ingreso: +${monto:.2f}\n")
            print("¡Dinero guardado en el archivo!")

        elif opcion == "2":
            monto = float(input("Monto del gasto: "))
            if monto > saldo:
                print("Saldo insuficiente.")
            else:
                saldo -= monto
                with open(nombre_archivo, "a") as archivo:
                    archivo.write(f"Gasto: -${monto:.2f}\n")
                print("¡Gasto registrado en el archivo!")

        elif opcion == "3":
            print("\n--- HISTORIAL GUARDADO EN DISCO ---")
            try:
                with open(nombre_archivo, "r") as archivo:
                    print(archivo.read())
            except FileNotFoundError:
                print("El historial está vacío.")

        elif opcion == "4":
            break
        
        elif opcion == "5":
            intento = input("Introduce la contraseña para BORRAR TODO: ")
            
            if intento == PIN_CONSTRASEÑA:
                confirmar = input("¿Estás seguro? Esta acción no se puede deshacer (s/n): ")
                if confirmar.lower() == "s":
                    with open(nombre_archivo, "w") as archivo:
                        archivo.write("") 
                    saldo = 0.0
                    print("Historial y saldo reiniciados con éxito.")
                else:
                    print("Operación cancelada.")
            else:
                print("PIN incorrecto. Volviendo al menú...")

def menu_principal():
    while True:
        print("\n=== MULTI-PROGRAMA EN PYTHON ===")
        print("1. Usar calculadora")
        print("2. Usar gestor de gastos")
        print("3. Salir")
        
        eleccion = input("¿Qué quieres hacer hoy?: ")
        
        if eleccion == "1":
            n1 = float(input("Ingresa el primer número: "))
            n2 = float(input("Ingresa el segundo número:"))
            print("(1)Suma (2)Resta (3)Multi (4)Div")
            op = int(input("Operación: "))
            calculadora(n1, n2, op)
            
            input("\nPresiona ENTER para volver al menú...")
            
        elif eleccion == "2":
            gestor_de_gastos()
            
        elif eleccion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Esa función no existe, intenta de nuevo.")
            
if __name__ == "__main__":
    menu_principal()