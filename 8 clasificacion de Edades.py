# Solicitar la edad del usuario
edad = int(input("Por favor, ingresa tu edad: "))

# Clasificar al usuario según su edad
if 0 <= edad <= 12:
    print("Eres un niño.")
elif 13 <= edad <= 17:
    print("Eres un adolescente.")
elif edad >= 18:
    print("Eres un adulto.")
else:
    print("Edad no válida.")  # Para manejar entradas negativas
