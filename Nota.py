for n in range (0, 5, 1):
    Nome = input("Nome: ")
    RA = input("RA: ")
    nota = float(input("Nota: "))
    if nota < 5.0 and nota >= 0.0:
        print("Nome: ", Nome)
        print("RA: ", RA)
        print ("D")
    else:
        if nota < 7.0:
            print("Nome: ", Nome)
            print("RA: ", RA)
            print("C")
        else:
            if nota < 9.0:
                print("Nome: ", Nome)
                print("RA: ", RA)
                print("B")
            else:
                if nota <= 10.0:
                    print("Nome: ", Nome)
                    print("RA: ", RA)
                    print("A")
                else: print("Nota inválida!")