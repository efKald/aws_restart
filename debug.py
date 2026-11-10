# debug.py
def calcular_precio_con_descuento(precio_base, porcentaje_descuento):
    # Aquí hay un error de lógica oculto:
    descuento = precio_base * porcentaje_descuento / 100
    precio_final = precio_base - descuento
    return precio_final

productos = [
    {"nombre": "Camiseta", "precio": 20, "descuento": 10},
    {"nombre": "Pantalón", "precio": 50, "descuento": "15"}, 
    {"nombre": "Zapatos", "precio": 80, "descuento": 20}
]

for prod in productos:
    print(f"Calculando para {prod['nombre']}...")
    resultado = calcular_precio_con_descuento(prod["precio"], prod["descuento"])
    print(f"Precio final: {resultado}")