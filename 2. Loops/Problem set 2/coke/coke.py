def main ():
    amount_due = 50
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = input("Insert Coin: ")
        coin = int(coin)
        change = get_coin(coin)
        amount_due = amount_due - change
    print(f"Change Owed: {-amount_due}")


def get_coin(coin):
    match coin:
        case 25:
            coin = 25
        case 10:
            coin = 10
        case 5:
            coin = 5
        case _:
            coin = 0
    return coin

main ()