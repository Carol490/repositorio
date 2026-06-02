print(f'''
      proga:
      ''')
Comandante_galactico = 0
Cadete_estelar = 0 
cant_pilotos = 0
cant_pilotos = int(input('Ingrese la cantidad de pilotos espaciales: '))
if cant_pilotos == 0:
    print('¡Número inválido! Ingresa un entero positivo para continuar el entrenamiento')
else:
    for i in range(cant_pilotos):
        nombre = input(f'Ingrese el nombre del piloto espacial {i + 1}: ')
        if (len(nombre)) < 6 or ( ' ' in nombre):
            print(f'¡Error de calibración! El nombre del piloto espacial {i + 1} debe tener un máximo de 6 caracteres y no contener espacios. Por favor, ingresa un nombre válido.')   
            continue 
        print(f'¡Bienvenido al entrenamiento, {nombre}!')
        #parte 2 y 3 
        nivel_vuelo = int(input(f'Ingrese el nivel de vuelo de {nombre}: '))
        if nivel_vuelo < 40:
            Comandante_galactico += 1
        elif nivel_vuelo >= 40:
            Cadete_estelar += 1
        else:
            print(f'¡Error de calibración! Ingresa un número entero positivo para el nivel de vuelo de {nombre}.')
        #parte 5 
print(f'''
     ¡La flota estelar cuenta con {Comandante_galactico} Comandantes Galácticos y {Cadete_estelar} Cadetes Estelares! ¡Prepáren
se para despegar
      ''')
