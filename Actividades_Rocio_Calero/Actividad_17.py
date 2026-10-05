persona1 = input('Elija una opcion (piedra/papel/tijera)')
persona2 = input('Elija una opcion (piedra/papel/tijera)')

match persona1:
    case 'piedra':
        match persona2:
            case 'piedra':
                print ('Empatataste')
            case 'tijera':
                print ('Gana ',persona1, ':Piedra rompe tijera')
            case 'papel':
                print ('Gana ',persona2, ':Papel emvuelve piedra')
            case _:
                print ('Perdeis los 2')
    case 'tijera':
        match persona2:
            case 'piedra':
                print ('Gana ',persona2, ':Piedra rompe tijera')
            case 'tijera':
                print ('Empatataste')
            case 'papel':
                print ('Gana ',persona1, ':Tijera corta papel')
            case _:
                print ('Perdeis los 2')
    case 'papel':
        match persona2:
            case 'piedra':
                print ('Gana ',persona1, ':Papel emvuelve piedra')
            case 'tijera':
                print ('Gana ',persona2, ':Tijera corta papel')
            case 'papel':
                print ('Empatataste')
            case _:
                print ('Perdeis los 2')
    case _: 
        print('Aprende a jugar')