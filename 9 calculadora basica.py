# Solicitar dos números al usuario
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Solicitar la operación matemática
operacion = input("Ingresa la operación (+, -, *, /): ")

# Realizar la operación correspondiente
if operacion == "+":
    resultado = numero1 + numero2
    print(f"El resultado de la suma es: {resultado}")
elif operacion == "-":
    resultado = numero1 - numero2
    print(f"El resultado de la resta es: {resultado}")
elif operacion == "*":
    resultado = numero1 * numero2
    print(f"El resultado de la multiplicación es: {resultado}")
elif operacion == "/":
    if numero2 != 0:  # Verificar si el divisor no es cero
        resultado = numero1 / numero2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operación no válida.")
