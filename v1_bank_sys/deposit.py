def deposit(extract: list, amount_deposited: float):
    extract.append(f'+R$ {amount_deposited:0.2f}')
    return [amount_deposited, extract]
