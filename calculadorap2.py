def somar(v1, v2):
    return v1 + v2

def subtrair(v1, v2):
    return v1 - v2

def multiplicar(v1, v2):
    return v1 * v2

def dividir(v1, v2):
    
    if v2 == 0:
        print("Não existe divisão por zero")
        return None
    return v1 / v2

def menu():
    print("O que deseja fazer?")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    
def obter_numeros():
    num1 = input(("Qual seu 1º número?: "))
    num2 = input(("Qual seu 2º número?: "))
    
    return num1, num2

def main():
    
    menu()
    op = input("Qual opção você deseja?: ")
    num1, num2 = obter_numeros()
    match op:
        case '1':
            r = somar(num1, num2)
            print(r)
        case '2':
            r = subtrair(num1, num2)
            print(r)
        case '3':
            r = multiplicar(num1, num2)
            print(r)
        case '4':
            r = dividir(num1, num2)
            print(r)

main()