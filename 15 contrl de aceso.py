# Definir las credenciales correctas
usuario_correcto = "admin"
contrasena_correcta = "1234"

# Número de intentos permitidos
intentos = 3

while intentos > 0:
    # Solicitar al usuario su nombre de usuario y contraseña
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    
    # Validar las credenciales
    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        print(f"Bienvenido, {usuario}.")
        break  # Salir del bucle si las credenciales son correctas
    else:
        intentos -= 1  # Decrementar el número de intentos
        if intentos > 0:
            print(f"Credenciales incorrectas. Le quedan {intentos} intentos.")
        else:
            print("Acceso bloqueado. Ha agotado todos los intentos.")
