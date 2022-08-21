def armazenaValores():
    global media1, media2

    while True:
        try:
            media1 = int(input('Insira a idade3 media de [A] e [B]: '))
        except ValueError as e:
            print("Valor inválido:", e)
        else:
            break
    while True:
        try:
            media2 = int(input('Insira a idade3 media de [A], [B] e [C]: '))
        except ValueError as e:
            print("Valor inválido:", e)
        else:
            break

def calcula():
    armazenaValores()
    try:
        x = (media2 * 3) - (media1 * 2)
        print(f'\nResposta: {x}\n')
    except:
        print('erro!')
    
if __name__=='__main__':
    while True:
        calcula()
        print(f'--------------------------------------------------------------\n\n')
        finish = input(f'precione qualquer tecla para sair ou "s" para continuar: ')
        if finish != 's':
            quit()