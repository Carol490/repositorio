nombres = []

for i in range(3):
    while True:
        nombre = input(f'Ingrese un nombre {i+1}: ')
        if len(nombre) >= 3:
             nombres.append(nombre)
             break
        else:
            print(f'debe tener mas de 3 letras el nombre ')
nombre_mayor = max(nombres, key=len)

print(f'el nombre mayor es: {nombre_mayor} y tiene {len(nombre_mayor)} letras')
