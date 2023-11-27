import sys


def withdraw_money(balance: float, amount_withdrawn: float, limit: float, extract: list):
    if (balance >= amount_withdrawn) and (amount_withdrawn <= limit):
        extract.append(f'-R${amount_withdrawn:0.2f}')
        return [amount_withdrawn, extract]
    elif (balance < amount_withdrawn):
        print("Saldo insuficiente!")
        sys.exit()
    elif (amount_withdrawn > limit):
        print("Valor acima do limite de saque!")
        sys.exit()
