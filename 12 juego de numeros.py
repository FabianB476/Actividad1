import random

# Generar un número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)

# Solicitar al usuario que adivine el número
adivinanza = int(input("Adivina el número entre 1 y 10: "))

# Verificar si el número ingresado es correcto
if adivinanza == numero_aleatorio:
    print("¡Felicidades, acertaste!")
else:
    print("Intenta de nuevo.")
