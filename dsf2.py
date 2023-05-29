radar = float (input("Qual a velocidade do automovel? "))
if radar > 80:
    print("vc é burro? Foi multado em 2 euros por km")
else:
    print("Nao fez mais que a obrigacao")
valormulta = radar * 2
print("Sua multa em euro: ",valormulta)