i = 0 #contador
b = 0 #acumulador
c = "s" #variaveldecontrole
while c == "s":
    n = float(input("Qual o primeiro número? "))
    b = b + n
    i = i + 1
    c = input("Deseja continuar? Digite s: ")
print("A média é: ", (b/i))