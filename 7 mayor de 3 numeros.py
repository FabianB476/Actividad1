# Solicitar tres números al usuario
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))

# Determinar cuál es el mayor
if numero1 >= numero2 and numero1 >= numero3:
    print(f"El número mayor es {numero1}")
elif numero2 >= numero1 and numero2 >= numero3:
    print(f"El número mayor es {numero2}")
else:
    print(f"El número mayor es {numero3}")
