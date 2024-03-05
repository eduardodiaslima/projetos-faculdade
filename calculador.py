n1 = float(input("Digite um número:"))
op = str(input("Digite um operador:"))
n2 = float(input("Digite outro número:"))
print(n1,op,n2,"=")
if op == "/" or op == "%":
    if n1 != 0 and n2 !=0:
        if op == "/":
            print(n1 / n2)
        elif op == "%":
            print(n1%n2)
    else:
        if op == "/":
            print("Não se divide por 0")
        elif op == "%":
            print("Não se divide por 0")
else:
    if op == "+":
        print(n1+n2)
    elif op == "-":
        print(n1-n2)
    elif op == "*":
        print(n1*n2)
    elif op == "^":
        print(n1**n2)
    else:
        print("Operador inválido.")
