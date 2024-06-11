def suma(a , b):
    return a + b


def resta(a , b):
    return a - b


def multiplicacion(a , b):
    return a * b


def division(a , b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"


def calculadora():
    print ( "Selecciona la operación:" )
    print ( "1. Suma" )
    print ( "2. Resta" )
    print ( "3. Multiplicación" )
    print ( "4. División" )
    print ( "5. Salir" )

    while True:
        opcion = input ( "Ingresa el número de la operación: " )

        if opcion != '5':
            num1 = float ( input ( "Ingresa el primer número: " ) )
            num2 = float ( input ( "Ingresa el segundo número: " ) )

        if opcion == '1':
            resultado = suma ( num1 , num2 )
            print ( num1 , "+" , num2 , "=" , resultado )
        elif opcion == '2':
            resultado = resta ( num1 , num2 )
            print ( num1 , "-" , num2 , "=" , resultado )
        elif opcion == '3':
            resultado = multiplicacion ( num1 , num2 )
            print ( num1 , "*" , num2 , "=" , resultado )
        elif opcion == '4':
            resultado = division ( num1 , num2 )
            print ( num1 , "/" , num2 , "=" , resultado )
        elif opcion == '5':
            break

        siguiente_calculo = int ( input ( "¿Quieres realizar otra operación? (1-si/2-no): " ) )
        if siguiente_calculo != 1:
            break


calculadora ()
