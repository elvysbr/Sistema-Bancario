menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

def voltar_ao_menu_principal():
    print('\nVoltando ao menu principal...')
    input('Pressione ENTER para voltar...')
    print()

print('Bem-vindo ao Banco do L!')


while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Digite o valor a depositar: '))
        if valor <= 0:
            print('Valor inválido.')
        else:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'
            print(f'Depositado com sucesso. Saldo: R$ {saldo:.2f}')
    
    elif opcao == 's':
        if numero_saques >= LIMITE_SAQUES:
            print('Você atingiu o limite de saques permitido.')
        elif saldo <= 0:
            print('Saldo insuficiente.')
        elif saldo:
            valor = float(input('Digite o valor a sacar: '))
            if valor <= 0:
                print('Valor inválido.')
            elif valor > saldo:
                print('Saldo insuficiente.')
                voltar_ao_menu_principal()
            else:

                saldo -= valor
                extrato += f'Saque: R$ {valor:.2f}\n'
                numero_saques += 1
                print(f'Saque efetuado com sucesso. Saldo: R$ {saldo:.2f}')
                if numero_saques >= LIMITE_SAQUES:
                    print(f'Você atingiu o limite de saques permitido. Saldo: R$ {saldo:.2f}')
                    voltar_ao_menu_principal()
            
    
    elif opcao == 'e':
        print('Extrato:')
        print(extrato)
        voltar_ao_menu_principal()
    
    elif opcao == 'q':
        break

    else:
        print('Opção inválida.')
        voltar_ao_menu_principal()