nome = str(input("Nome do funcionário: "))
cargo = str(input("Cargo do funcionário: "))
sal = float(input("E o salário:"))
salnovo = float
print("Cargo: ", cargo)
print("Salário antigo: ", sal)
if cargo == "GER":
    salnovo = (sal + (sal * 0.1))
    print("Novo salario: ", salnovo)
    print("Diferença: ", (salnovo - sal))
elif cargo == "ENG":
    salnovo = (sal + (sal * 0.2))
    print("Novo salario: ", salnovo)
    print("Diferença: ", (salnovo - sal))
elif cargo == "TEC":
    salnovo = (sal + (sal * 0.3))
    print("Novo salario: ", salnovo)
    print("Diferença: ", (salnovo - sal))
else:
    salnovo = (sal + (sal * 0.4))
    print("Novo salario: ", salnovo)
    print("Diferença: ", (salnovo - sal))