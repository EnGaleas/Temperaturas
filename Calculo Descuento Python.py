def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento dado un porcentaje.
    :param monto_total: Total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 10%).
    :return: Monto del descuento.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Definir montos de compra y porcentaje de descuento personalizado
monto1 = 1000  # Primer monto total
monto2 = 1500  # Segundo monto total
porcentaje_personalizado = 15  # Porcentaje de descuento personalizado

# Calcular descuento utilizando la función
descuento1 = calcular_descuento(monto1)  # Se usa el valor por defecto (10%)
descuento2 = calcular_descuento(monto2, porcentaje_personalizado)  # Se usa el 15%

# Calcular el monto final a pagar después del descuento
total1 = monto1 - descuento1
total2 = monto2 - descuento2

# Mostrar resultados con detalles
print(f"Monto total: ${monto1}, Descuento: ${descuento1}, Total a pagar: ${total1}")  # Imprime los resultados de la primera compra
print(f"Monto total: ${monto2}, Descuento: ${descuento2}, Total a pagar: ${total2}")  # Imprime los resultados de la segunda compra
