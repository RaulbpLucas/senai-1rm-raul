salario = float(input("Qual o seu salario? "))
if salario > 8250:
    salariomaior = salario * 1.10
    print ("Seu reajuste de salarial de 12%: ",salariomaior)
else:
    salariomenor = salario * 1.15
    print("Seu reajuste salarial de 15%: ",salariomenor)