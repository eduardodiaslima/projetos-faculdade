cpf = input("Digite seu CPF:")

tamCpf = len(cpf)

dc1 = int(cpf[9])
dc2 = int(cpf[10])
a1 = int(cpf[0]) * 10
a2 = int(cpf[1]) * 9
a3 = int(cpf[2]) * 8
a4 = int(cpf[3]) * 7
a5 = int(cpf[4]) * 6
a6 = int(cpf[5]) * 5
a7 = int(cpf[6]) * 4
a8 = int(cpf[7]) * 3
a9 = int(cpf[8]) * 2

b1 = int(cpf[0]) * 11
b2 = int(cpf[1]) * 10
b3 = int(cpf[2]) * 9
b4 = int(cpf[3]) * 8
b5 = int(cpf[4]) * 7
b6 = int(cpf[5]) * 6
b7 = int(cpf[6]) * 5
b8 = int(cpf[7]) * 4
b9 = int(cpf[8]) * 3
b10 = int(cpf[9]) * 2
cpf = int(cpf)

soma = (a1+a2+a3+a4+a5+a6+a7+a8+a9)
divisao = (soma * 10) % 11
soma2 = (b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10)
div2 = (soma2 * 10) % 11

if tamCpf != 11:
    print('CPF INVÁLIDO')
else:
    if dc1 == divisao and dc2 == div2:
        print("CPF VÁLIDO")
    else:
        print('CPF INVÁLIDO')