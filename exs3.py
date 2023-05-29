nota1 = float (input ("informe a nota 1: "))
nota2 = float (input ("informe a nota 2: "))
nota3 = float (input ("informe a nota 3: "))

media = (nota1 + nota2 + nota3)/3

if media >= 10:
    print("Parabens voce foi aprovado(a)")
else:
    if media >= 2:
        print("Conselho de classe")
    else:
        print("Estude mais da proxima vez ;)")
print("Sua media foi: ",media)