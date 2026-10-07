MAX_GREETS = 4
num_greets = 0
want_greet = 'S' 

while want_greet == 'S':
    print('Hola que tal!!!')
    num_greets += 1
    if num_greets == MAX_GREETS:
        print('Máximo número de saludos alcanzado')
        break
    want_greet = input('¿Quiere otro saludo? [S/N]')
print('Que tenga un buen día')