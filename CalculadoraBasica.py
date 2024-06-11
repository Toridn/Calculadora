while True:
    print ( "Selecciona la operación:" )
    print ( "1. Suma" )
    print ( "2. Resta" )
    print ( "3. Multiplicación" )
    print ( "4. División" )
    print ( "5. Salir" )

    opcion = input ( "Ingresa el número de la operación: " )

    if opcion != '5':
        num1 = float ( input ( "Ingresa el primer número: " ) )
        num2 = float ( input ( "Ingresa el segundo número: " ) )

    if opcion == '1':
        resultado = num1 + num2
        print ( num1 , "+" , num2 , "=" , resultado )
    elif opcion == '2':
        resultado = num1 - num2
        print ( num1 , "-" , num2 , "=" , resultado )
    elif opcion == '3':
        resultado = num1 * num2
        print ( num1 , "*" , num2 , "=" , resultado )
    elif opcion == '4':
        if num2 != 0:
            resultado = num1 / num2
            print ( num1 , "/" , num2 , "=" , resultado )
        else:
            print ( "Error: División por cero" )
    elif opcion == '5':
        break

    siguiente_calculo = int ( input ( "¿Quieres realizar otra operación? (1-si/2-no): " ) )
    if siguiente_calculo != 1:
        break
