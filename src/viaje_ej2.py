distancia_km= int(input('introduce una distancia: '))
velocidad_kmh= int(input('introduce una velocidad: '))
tiempo_horas = distancia_km / velocidad_kmh
tiempo_dias = tiempo_horas / 24
print(f"Tardarías {tiempo_dias} días en llegar.")