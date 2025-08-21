num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))
op = input("digite a operacao (+, -, *, /): ")

print("----- RESULTADO -----")

match op:
    case '+':
        r = num1 + num2
        print(r)
        
    case '-':
        r = num1 - num2
        print(r)
        
    case '*':
        r = num1 * num2
        print(r)
        
    case '/':
        if num2 == 0:
            print("Não existe divisão por zero")
        else:
            r = num1 / num2
            print(r)
    case _:
        print("Operação inválida")