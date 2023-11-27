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
    option = input("Digite um número com a opção escolhida: ")

    if (option.upper() == 'S'):
        amount_withdraw = int(input("Quanto você deseja sacar? "))
        withdraw_money_operation = withdraw_money.withdraw_money(
            balance, amount_withdraw, 500, extract)
        balance -= withdraw_money_operation[0]
        extract.append(withdraw_money_operation[1])
        print(balance)

    elif (option.upper() == 'D'):
        amount_to_deposit = int(input("Quanto você deseja depositar? "))
        deposit_operation = (deposit.deposit(extract, amount_to_deposit))
        balance += deposit_operation[0]
        extract.append(deposit_operation)
        print(balance)

    elif (option.upper() == 'E'):
        print(extract)
    elif (option.upper() == 'Q'):
        print("Até mais...")
        sys.exit()
    else:
        print("Operação inválida!")
        continue
