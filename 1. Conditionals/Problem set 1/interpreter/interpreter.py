a, b, c = input("Expression: ").split(sep=" ")
a = float(a)
c = float(c)

match b:
    case "+":
        d = a + c
        print(d)
    case "-":
        d = a - c
        print(d)
    case "*":
        d = a * c
        print(d)
    case "/":
        d = a / c
        print(d)