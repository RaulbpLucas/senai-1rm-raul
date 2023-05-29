while True:
    print("selecione a questao:")
    print("exercicio 1")
    print("exercicio 2")
    print("exercicio 3")
    print("exercicio 4")
    pergunta = int(input("Digite o numero de exercicio: "))
    if pergunta == 1:
        base = int(input("valor da base: "))
        altura = int(input("valor altura: "))
        def area(base,altura):
            total = base*altura
            return total
        print("O valor em metros quadrados se da por: ",area(base,altura))
        print("Fim")
    if pergunta == 2:
        def contagem_regressiva(num1):
            while num1 > 0:
                num1 = num1 - 1
                print(num1)
        numero = int(input("Valor: "))
        contagem_regressiva(numero)
        print("Fim")
    if pergunta == 3:
        def maior(n1,n2,n3):
            if (n1 > n2 and n1 > n3):
                return n1
            elif (n2 > n1 and n2 > n3):
                return n2
            elif (n3 > n1 and n3 > n2):
                return n3
        a = int(input("Valor 1: "))
        b = int(input("Valor 2: "))
        c = int(input("Valor 3: "))
        print("O maior numero de da por: ",maior(a,b,c))
        print("Fim")
    if pergunta == 4:
        a = int(input("Digite o valor 1: "))
        b = int(input("Digite o valor 2: "))
        def valor(n1,n2):
            soma = n1 + n2
            print(soma)
            multiplicacao = n1 * n2
            print(multiplicacao)
            if (n1 > n2):
                print(n1)
            elif (n2 > n1):
                print(n2)
            if (n1 < n2):
                print(n1)
            elif (n2 < n1):
                print(n2)
        print(valor(a,b))
            

        