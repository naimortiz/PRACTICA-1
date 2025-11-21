distancia_km = int(input('Introduce la distancia total en km: '))
n = 0

for distancia in range (150000, distancia_km + 1, 150000):
    print(f'Parada en el km {distancia}')
    n = n + 1

print(f'Número total de paradas para repostar: {n}')

# range (1, 5)
# siedno 1 limite inferiory 5 el limite superior
# si solo pusieramos un numero se consideraria limite superior

# range (1, 5, 2)
#siendo 2 el rango de salto
 