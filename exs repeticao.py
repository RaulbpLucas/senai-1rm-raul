while True:
    print("Selecione a questao")
    print("exercicio 1")
    print("exercicio 2")
    print("exercicio 3")
    print("exercicio 4")
    print("Saida 5")
    pergunta = int(input("Digite o numero do exercicio >"))
    if pergunta == 1:
        for count in range(1,61):
            print(count)
        print("Fim")
    if pergunta == 2:
        for count in range(0,62,2):
            print(count)
        print("Fim")
    if pergunta == 3:
        tabuada = int(input("Tabuada do numero: "))
        for count in range(10):
            print("{} x {} = {}".format(tabuada,count+1,tabuada*(count+1)))
    if pergunta == 4:
        num = int(input("Digite o numero desejado: "))
        final = 1
        for count in range (1,num+1):
            final = final*count
        print("{}! = {}".format(num,final))
    if pergunta == 5:
        break