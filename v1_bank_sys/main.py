import sys
import deposit
import withdraw_money

balance = 3000
extract: list = []

while True:
    print('''
      [S] - Sacar
      [D] - Depositar
      [E] - Extrato
      [Q] - Sair
    ''')
    opcao = input("Digite um número com a opção escolhida: ")

    if (opcao.upper() == 'S'):
        amount_withdraw = int(input("Quanto você deseja sacar? "))
        withdraw_money_operation = withdraw_money.withdraw_money(
            balance, amount_withdraw, 500, extract)
        balance -= withdraw_money_operation[0]
        extract.append(withdraw_money_operation[1])
        print(balance)

    elif (opcao.upper() == 'D'):
        amount_to_deposit = int(input("Quanto você deseja depositar? "))
        deposit_operation = (deposit.deposit(extract, amount_to_deposit))
        balance += deposit_operation[0]
        extract.append(deposit_operation)
        print(balance)

    elif (opcao.upper() == 'E'):
        print(extract)
    elif (opcao.upper() == 'Q'):
        print("Até mais...")
        sys.exit()
    else:
        print("Operação inválida!")
        continue
