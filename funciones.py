def operar_numeros(num1, num2):
    """
    Función que recibe dos números enteros y pregunta al usuario qué operación desea realizar.
    Retorna el resultado de la operación seleccionada.
    """
    print(f"Números ingresados: {num1} y {num2}")
    print("Seleccione la operación que desea realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    opcion = input("Ingrese el número de la operación (1-4): ")
    
    if opcion == "1":
        resultado = num1 + num2
        print(f"Suma: {num1} + {num2} = {resultado}")
        return resultado
    elif opcion == "2":
        resultado = num1 - num2
        print(f"Resta: {num1} - {num2} = {resultado}")
        return resultado
    elif opcion == "3":
        resultado = num1 * num2
        print(f"Multiplicación: {num1} * {num2} = {resultado}")
        return resultado
    elif opcion == "4":
        if num2 != 0:
            resultado = num1 / num2
            print(f"División: {num1} / {num2} = {resultado}")
            return resultado
        else:
            print("Error: No se puede dividir por cero")
            return None
    else:
        print("Opción no válida")
        return None