"""
Programa para calcular pagos y propinas en una barberia.
Permite atender avrios clientes y maneja errores de entrada.
"""
def servicio_barberia():
    try:
        nombre = input("Nombre del cliente: ")
        precio = float(input("Precio del servicio: "))
        pago = float(input("Dinero pagado: "))
           
        if pago < precio:
            print("Falta dinero para completar el pago")
        elif pago == precio:
            print(f"Gracias por su visita, {nombre}")
        else:
            propina = pago - precio
            print(f"Gracias por la propina, {nombre}")
            print(f"Propina: {propina}")
    except ValueError:
        print("Error: ingrese solo numeros")
while True:
    servicio_barberia()
    continuar = input("¿Atender otro cliente? (s/n):")
    if continuar.lower() !="s":
        break

    
    
