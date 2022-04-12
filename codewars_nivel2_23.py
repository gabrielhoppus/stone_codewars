"""Bootcamp Python - Código S
Code Wars I - 8 a 12/4

Grupo 23: Luiz Gabriel Macedo da Silva, Lucas Mattos de Lima Sobral, Igor de Abreu Medeiros,
Daniel Salomão Barreto, Lucas Simoes Alcantara Dantas, Larissa Henrique Evangelista Casotro

Implementar um sistema em Python que efetue o comportamento de um robô tentando encontrar
a saída de um labirinto.
As inspirações para esse projeto foram: aspiradores de pó automáticos (como o Roomba),
navegação no Google Maps e o problema clássico do Labirinto do Minotauro.
O objetivo do projeto é posicionar um robô em um labirinto e desenvolver a lógica para que ele
percorra esse labirinto em busca da saída, avançando pelas células em branco, respeitando as
paredes e retornando por um caminho caso esteja encurralado. O robô não pode avançar 2 vezes
por um mesmo caminho, assim, ao descobrir que está encurralado pode retornar pelas células
percorridas, mas não deve avançar novamente por este caminho."""


from time import sleep

PAREDE = '#'
CAMINHO_LIVRE = ' '
CAMINHO_PERCORRIDO = "."
ROBO = "X"
SAIDA = "S"

ESQUERDA = [0,-1]
DIREITA  = [0,1]
CIMA     = [-1,0]
BAIXO    = [1,0]

LABIRINTO = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
    ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'], 
    ['#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#'], 
    ['#', '#', '#', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'], 
    ['#', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#'], 
    ['#', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#'], 
    ['#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', '#'], 
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]
# função que formata e apresenta o labirinto para o usuário
def print_labirinto():
    print("")
    for linha in LABIRINTO:
        print(" ".join(linha))
    print("")    

# função que aciona o movimento e marca o caminho percorrido
def movimento(posicao: tuple, direcao: list) -> tuple:
    LABIRINTO[posicao[0]][posicao[1]] = CAMINHO_PERCORRIDO
    LABIRINTO[posicao[0]+direcao[0]][posicao[1]+direcao[1]] = ROBO
    return [posicao[0] + direcao[0], posicao[1]+direcao[1]] 

# função que verifica se um movimento é possível ou não
def verifica_movimento(posicao: tuple, direcao: list) -> bool:
    if LABIRINTO[posicao[0]+direcao[0]][posicao[1]+direcao[1]] == SAIDA:
        return True
    elif LABIRINTO[posicao[0]+direcao[0]][posicao[1]+direcao[1]] == CAMINHO_LIVRE:
        return True
    elif LABIRINTO[posicao[0]+direcao[0]][posicao[1]+direcao[1]] == PAREDE:
        return False
    elif LABIRINTO[posicao[0]+direcao[0]][posicao[1]+direcao[1]] == CAMINHO_PERCORRIDO:
        return False    

# função principal que roda o labirinto e o caminho percorrido pelo robô        
def main() -> tuple:
    print_labirinto()
    # pega o input do usuário das coordenadas iniciais do robô e valida o input 
    POSICAO_INICIAL = list(map(int,input("Digite a posição do Robô (linha, coluna): ").split(",")))
    while LABIRINTO[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]] != CAMINHO_LIVRE:
        POSICAO_INICIAL = list(map(int,input("Erro! Digite uma posição válida para o Robô (linha, coluna): ").split(",")))     
    POSICAO_SAIDA = [9,18]
    LABIRINTO[POSICAO_SAIDA[0]][POSICAO_SAIDA[1]] = SAIDA
    LABIRINTO[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]] = ROBO
    print_labirinto()
    
    # armazena os caminhos percorridos pelo robô sendo o primeiro sua primeira posição
    pilha = [POSICAO_INICIAL]
    POSICAO_ATUAL = POSICAO_INICIAL

    # checa as direções possíveis em busca da saída e do caminho livre
    while POSICAO_ATUAL != POSICAO_SAIDA:
        if verifica_movimento(POSICAO_ATUAL, CIMA):
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, CIMA)
            pilha.append(POSICAO_ATUAL)
            print_labirinto()
            sleep(1)
        elif verifica_movimento(POSICAO_ATUAL, DIREITA):
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
            pilha.append(POSICAO_ATUAL)
            print_labirinto()
            sleep(1)
        elif verifica_movimento(POSICAO_ATUAL, BAIXO):
           POSICAO_ATUAL = movimento(POSICAO_ATUAL, BAIXO)
           pilha.append(POSICAO_ATUAL)
           print_labirinto()
           sleep(1)
        elif verifica_movimento(POSICAO_ATUAL, ESQUERDA):
           POSICAO_ATUAL = movimento(POSICAO_ATUAL, ESQUERDA)
           pilha.append(POSICAO_ATUAL)
           print_labirinto()
           sleep(1)
        else:
            # refaz o caminho percorrido até achar outro caminho livre
            LABIRINTO[POSICAO_ATUAL[0]][POSICAO_ATUAL[1]] = CAMINHO_PERCORRIDO
            pilha.pop()
            POSICAO_ATUAL = pilha[-1]
            LABIRINTO[POSICAO_ATUAL[0]][POSICAO_ATUAL[1]] = ROBO
            print_labirinto()
            sleep(1)    
    print("Meus parabéns! \nVocê encontrou a saída!")                         
main()
