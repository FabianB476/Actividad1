# Solicitar al usuario ingresar el monto de la compra
monto_compra = float(input("Ingresa el monto de tu compra: $"))

# Verificar si el monto es mayor a 100 y aplicar el descuento si corresponde
if monto_compra > 100:
    descuento = monto_compra * 0.20  # 20% de descuento
    monto_final = monto_compra - descuento  # Aplicar el descuento al monto original
    print(f"Se ha aplicado un descuento del 20%. El monto final a pagar es: ${monto_final:.2f}")
else:
    print(f"El monto final a pagar es: ${monto_compra:.2f}")
