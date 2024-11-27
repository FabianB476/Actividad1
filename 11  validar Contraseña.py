# Contraseña fija correcta
contraseña_correcta = "12345"

# Solicitar la contraseña al usuario
contraseña_ingresada = input("Ingresa la contraseña: ")

# Validar si la contraseña es correcta
if contraseña_ingresada == contraseña_correcta:
    print("Acceso concedido")
else:
    print("Contraseña incorrecta. Acceso denegado.")
