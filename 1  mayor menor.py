# Función que compara dos números
def comparar_numeros(num1, num2):
    if num1 > num2:
        print(f"El número {num1} es mayor que {num2}.")
    elif num1 < num2:
        print(f"El número {num1} es menor que {num2}.")
    else:
        print(f"El número {num1} es igual a {num2}.")

# Solicitar números al usuario
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

# Llamar a la función para comparar
comparar_numeros(numero1, numero2)

