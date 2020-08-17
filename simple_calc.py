inp1 = float(input())
inp2 = float(input())
op = input()

if inp2 != 0:
    if op == "+":
        print(inp1 + (inp2))

    elif op == "-":
        print(inp1 - (inp2))

    elif op == "/":
        print(inp1 / (inp2))

    elif op == "*":
        print(inp1 * inp2)


    elif op == "mod":
        print((inp1) % (inp2))

    elif op == "pow":
        print((inp1) ** (inp2))

    elif op == "div":
        print((inp1) // (inp2))
elif inp2 == 0.0:
    if op in ('/', 'mod', 'div'):
        print("Division by 0!")
    elif op == "+":
        print(inp1 + (inp2))
    elif op == "-":
        print(inp1 - (inp2))

    elif op == "*":
        print(inp1 * inp2)

    elif op == "pow":
        print((inp1) ** (inp2))
