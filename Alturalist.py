alturas = [1.80, 1.76, 1.78, 1.87]
i = 0
maior = alturas[0]
while i <= len(alturas) - 1:
    if maior < alturas[i]:
        maior = alturas[i]
    i = i+1
print(maior)