

respuesta = 's'

while respuesta == 's':
    distancia_km = int(input('Dime la distancia que quieres recorrer: '))
    velocidad_km = int(input('Dime la velocidad que vas: '))
    tiempo_horas = distancia_km // velocidad_km
    tiempo_dias = tiempo_horas / 24
    print(f'Tardarías {tiempo_dias} dias en llegar.')
    respuesta = input('Quieres hacer otra simulación? (s/n): '). lower() #lower convierte en minúsculas el input