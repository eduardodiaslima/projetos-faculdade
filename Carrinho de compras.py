i = 1
qtd = 0
somador = 0
while i == 1:
    produto = input('Escreva o nome do produto: ')
    preço = float(input('Escreva o preço: '))
    qtd = qtd + 1
    somador = somador + preço
    i = int(input("Para continuar digite 1 e para parar digite 2: "))
print("Quantidade: ", qtd)
print("Preço total: ", somador)