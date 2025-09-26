distancia_km = int(225000000)
#velocidad_kmh = [10000, 20000, 30000, 40000, 50000]

for velocidad_kmh in range(10000, 50001, 10000):
    tiempo_horas = distancia_km / velocidad_kmh
    tiempo_dias = tiempo_horas / 24
    print('Velocidad: ',velocidad_kmh,'-> Tiempo: ',tiempo_dias)
