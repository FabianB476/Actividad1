# Solicitar al usuario un número entero
numero = input("Ingresa un número entero: ")

# Calcular la suma de los dígitos
suma_digitos = sum(int(digit) for digit in numero if digit.isdigit())

# Mostrar el resultado
print(f"La suma de los dígitos de {numero} es: {suma_digitos}")
