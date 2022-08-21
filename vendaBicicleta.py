def armazenaValores():
    global valorVenda, rateTotalValor, lucroEsperado

    while True:
        try:
            valorVenda = int(input('Insira o valor da Venda: '))
        except ValueError as e:
            print("Valor inválido:", e)
        else:
            break
    while True:
        try:
            rateTotalValor = int(input('Insira a porcentagem do total que a bicicleta foi vendida: '))
            if not 0 <= rateTotalValor <= 100:
                raise ValueError('valor fora do esperado. insira um valor entre 0 e 100')
        except ValueError as e:
            print("Valor inválido:", e)
        else:
            break
    while True:
        try:
            lucroEsperado = int(input('Insira a porcentagem do lucro esperado: '))
            if not 0 <= lucroEsperado <= 100:
                raise ValueError('valor fora do esperado. insira um valor entre 0 e 100')
        except ValueError as e:
            print("Valor inválido:", e)
        else:
            break

def calcula():
    armazenaValores()
    try:
        x = (((valorVenda*100)/rateTotalValor) * (100 + lucroEsperado))/100
        print(f'\nResposta: {x}\n')
    except:
        print('erro!')

if __name__=='__main__':
    while True:
        calcula()
        print(f'--------------------------------------------------------------\n\n')
        finish = input(f'precione qualquer tecla para sair ou "s" para continuar: ')
        if finish != 's' or finish != 'S':
            quit()