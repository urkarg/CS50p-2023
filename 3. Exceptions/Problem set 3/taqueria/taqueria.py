menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
cost = 0

while True:
    try:
        item = input("Item: ").casefold()
        for menu_item in menu:
            if item == menu_item.casefold():
                cost += menu[menu_item]
            if item == "no "+ menu_item.casefold():
                cost -= menu[menu_item]
        print(f"${cost:.2f}")
    except EOFError:
        print()
        break