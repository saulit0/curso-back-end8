def add_tarefa(tarefas):
    titulo = input("Digite o titulo da tarefa: ")
    tarefas.append({'titulo': titulo, 'concluida': False})

def lista_tarefas(tarefas):
    for i, tarefa in enumerate(tarefas, start=0):
        
    print(f"{i}, {tarefa}")

def marcar_concluida():
    
    lista_tarefas(tarefas)
    
    num = int(input("Qual tarefa você quer marcar? "))
    tarefas[num - 1]['concluida'] = True
    print(f"Tarefa {num} foi concluída")
    
def sair():
    
    return False

def main():

    tarefas = []
    
    opcoes = {
        '1': add_tarefa,
        '2': lista_tarefas,
        '3': marcar_concluida,
        '4': sair
    }
    
    continuar = True
    while continuar:
    
        print(opcoes)
        escolha = input("Escolha uma opção: ")
        
        funcao = opcoes.get(escolha)
        
        if funcao:
            if funcao(tarefas) == false:
                continuar = False