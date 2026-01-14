def adicao(a, b):
    numero1 = a 
    numero2 = b
    total = numero1 + numero2
    return total
    
def subtracao(a, b):
    numero1 = a 
    numero2 = b
    total = numero1 - numero2
    return total
    
def divisao(a, b):
    numero1 = a 
    numero2 = b
    total = numero1 / numero2
    return total
    
def multiplicacao(a, b):
    numero1 = a 
    numero2 = b
    total = numero1 * numero2
    return total

while True:
    
    print("=== Calculadora ===\n")
    print("1. Adição")
    print("2. Subtração")
    print("3. Divisão")
    print("4. Multiplicação\n")
    
    try:
        
        opcao = int(input("opcaor o tipo da operação: "))
        
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
        
