dg = float(input("Quanto foi gasto?:"))
dd = float(input("Quanto foi pago?"))
troco = dd - dg
sobra = troco
if troco < 0:
    print("Troco insuficiente")
    exit()
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
m1 = 0
c50 = 0
c25 = 0
c10 = 0
c5 = 0
c1 = 0
while troco >= 100:
    troco = troco - 100
    n100 = n100 + 1
while troco >= 50:
    troco = troco - 50
    n50 = n50 + 1
while troco >= 20:
    troco = troco - 20
    n20 = n20 + 1
while troco >= 10:
    troco = troco - 10
    n10 = n10 + 1
while troco >= 5:
    troco = troco - 5
    n5 = n5 + 1
while troco >= 2:
    troco = troco - 2
    n2 = n2 + 1
while troco >= 1:
    troco = troco - 1
    m1 = m1 + 1
while troco >= 0.5:
    troco = troco - 0.5
    c50 = c50 + 1
while troco >= 0.25:
    troco = troco - 0.25
    c25 = c25 + 1
while troco >= 0.1:
    troco = troco - 0.1
    c10 = c10 + 1
while troco >= 0.05:
    troco = troco - 0.5
    c5 = c5 + 1
while troco >= 0.01:
    troco = troco - 0.01
    c1 = c1 + 1
print("O seu troco é: ", sobra)
print("Notas totais: ", (n2 + n5 + n10 + n20 + n50 + n100))
print("Moedas totais: ", (c1+c5+c10+c25+c50+m1))
print("Notas de 100: ", n100)
print("Notas de 50: ", n50)
print("Notas de 20: ", n20)
print("Notas de 10: ", n10)
print("Notas de 5: ", n5)
print("Notas de 2: ", n2)
print("Moedas de 1 real: ", m1)
print("Moedas de 50 centavos: ", c50)
print("Moedas de 25 centavos: ", c25)
print("Moedas de 10 centavos: ", c10)
print("Moedas de 5 centavos: ", c5)
print("Moedas de 1 centavo: ", c1)