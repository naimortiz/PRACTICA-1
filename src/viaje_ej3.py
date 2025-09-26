distancia_km = int(input('introduce una distancia: '))
velocidad_kmh = int(input('introduce una velocidad: '))
tiempo_horas = distancia_km / velocidad_kmh
tiempo_dias = tiempo_horas / 24
print(f"Tardarías {tiempo_dias} días en llegar.")

edad = int(input('Dime que edad tienes: '))
estado_fisico = int(input('Dime el nivel físico que tienes(del 1 al 10): '))

if edad >= 18:
    if estado_fisico < 5:
        print('Debes estar en mejor forma física')
    else:
        print('¡Listo para despegar!')

else:
    print('Debes ser mayor de edad para poder embarcar ')