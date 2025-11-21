distancia_km = int(input('Dime la distancia que quieres recorrer: '))
velocidad_kmh = int(input('Dime la velocidad que vas: '))    
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24

semanas = 0

while tiempo_dias > 7:
    semanas = semanas + 1
    tiempo_dias = tiempo_dias - 7

print(f'Tardarías {semanas} semanas y {tiempo_dias} días en llegar.')
