def adicao(n1, n2):
    return n1 + n2
    
def subtracao(n1, n2):
    return n1 + n2
    
def divisao(n1, n2):
    return n1 + n2
    
def multiplicacao(n1, n2):
    return n1 + n2

while True:
    
    print("=== Calculadora ===\n")
    print("1. Adição")
    print("2. Subtração")
    print("3. Divisão")
    print("4. Multiplicação\n")
    
    try:
        
        opcao = int(input("Escolha o tipo da operação: "))
        
        if opcao == 1:
            numero1 = int(input("Digite o primeiro número: "))
            numero2 = int(input("Digite o segundo número: "))
            resultado = adicao(numero1, numero2)
            print("Resultado:", resultado)
            break
            
        elif opcao == 2:
            numero1 = int(input("Digite o primeiro número: "))
            numero2 = int(input("Digite o segundo número: "))
            resultado = subtracao(numero1, numero2)
            print("Resultado:", resultado)
            break
            
        elif opcao == 3:
            numero1 = int(input("Digite o primeiro número: "))
            numero2 = int(input("Digite o segundo número: "))
            resultado = divisao(numero1, numero2)
            print("Resultado:", resultado)
            break
            
        elif opcao == 4:
            numero1 = int(input("Digite o primeiro número: "))
            numero2 = int(input("Digite o segundo número: "))
            resultado = multiplicacao(numero1, numero2)
            print("Resultado:", resultado)
            break
        
        else:
            print("Opção inválida!")
        
    except ValueError:
        print("Erro: Por favor, digite apenas números.")
