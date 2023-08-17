import calculadora




a = int(input("Digite um numero:"))
b = int(input("Digite outro numero:"))
operacao=int(input("Qual a operação (1- +, 2- -, 3- *,4- /): "))

if operacao == 1:
    soma=calculadora.soma(a, b)
    print(soma)
elif operacao ==2:
    menos= calculadora.subtracao(a, b)
    print(menos)
elif operacao == 3:
    mult = calculadora.multiplicacao(a, b)
    print(mult)
elif operacao ==4:
    div = calculadora.divisao(a, b)
    print(div)