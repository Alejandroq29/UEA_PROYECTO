def calcular_descuento(monto):
    # Definimos los rangos de descuento
    if monto < 100:
        descuento = 0
    elif 100 <= monto < 500:
        descuento = 0.1  # 10% de descuento
    elif 500 <= monto < 1000:
        descuento = 0.15  # 15% de descuento
    else:
        descuento = 0.2  # 20% de descuento

    return descuento

def main():
    # Pedimos al usuario que ingrese el monto total de la compra
    monto_total = float(input("Ingrese el monto total de la compra: $"))

    # Calculamos el descuento
    descuento = calcular_descuento(monto_total)

    # Calculamos el monto final a pagar
    monto_descuento = monto_total * descuento
    monto_final = monto_total - monto_descuento

    # Mostramos los resultados
    print(f"\nMonto total de la compra: ${monto_total:.2f}")
    print(f"Descuento aplicado: ${monto_descuento:.2f} ({descuento * 100:.0f}%)")
    print(f"Monto final a pagar: ${monto_final:.2f}")

if __name__ == "__main__":
    main()