#Introducir presentación
print('Este es el juego de piedra, papel y tijera')
persona1 = input('Elija una opcion (piedra/papel/tijera)')
persona2 = input('Elija una opcion (piedra/papel/tijera)')

match persona1:
    case 'piedra':
        match persona2:
            case 'piedra':
                print ('Empatataste')
            case 'tijera':
                print ('Gana jugador 1 con ',persona1, ':Piedra rompe tijera')
            case 'papel':
                print ('Gana jugador 2 con ',persona2, ':Papel envuelve piedra')
    case 'tijera':
        match persona2:
            case 'piedra':
                print ('Gana jugador 2 con ',persona2, ':Piedra rompe tijera')
            case 'tijera':
                print ('Empatataste')
            case 'papel':
                print ('Gana jugador 1 con ',persona1, ':Tijera corta papel')
    case 'papel':
        match persona2:
            case 'piedra':
                print ('Gana jugador 1 con ',persona1, ':Papel envuelve piedra')
            case 'tijera':
                print ('Gana jugador 2 con ',persona2, ':Tijera corta papel')
            case 'papel':
                print ('Empatataste')
    case _: 
        print('Aprende a jugar')