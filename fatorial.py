fatorial = int(input("Digite o numero que deseja: "))
for count in range(10):
    print("{}! = {}".format(fatorial,fatorial-1*(fatorial*count-1)))
print("Fim")