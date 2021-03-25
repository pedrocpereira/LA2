"""

Neste problema pretende-se que desenvolva uma função para detectar código
morto num programa. Código morto são instruções que nunca poderão ser
executadas num programa e que, como tal, poderiam ser eliminadas.
A linguagem de programação a analisar é muito simples. Um programa é uma
sequência de comandos, e apenas existem dois tipos de comandos: "print" que
dado um número imprime esse número e "jump" que dada uma sequência de 
localizações do programa separadas por vírgulas salta para uma dessas 
localizações à sorte. Uma localização é simplesmente o indíce de um comando
na sequência. A execução de um programa termina quando se executa a última
instrução (se for um "print") ou se salta para uma localização inexistente.
A função deve devolver um tuplo com o número de instruções que podem ser
executadas e o número de instruções que nunca poder~ão ser executadas.

"""


def deadcode(prog):
    vivos = 0
    mortos = 0
    comandos = set()
    
    for i in range(len(prog)):
        instrucao = prog[i].split()[0]
        n = prog[i].split()[1]
        indices = []
        if instrucao == 'jump':
            if i == 0 or i in comandos:
                for indice in n.split(','):
                    indices.append(int(indice))
                    comandos.add(int(indice))
                if min(indices) >= len(prog):
                    mortos += 1
                else:
                    vivos += 1
            else:
                mortos += 1
                
        if instrucao == 'print':
            if i == 0 or i in comandos:
                comandos.add(i + 1)
                vivos += 1
            else:
                mortos += 1
            
    return (vivos, mortos)
  
  
  
  """

Neste problema pretende-se que implemente uma função que ajude o Pac-Man a 
fugir dos fantasmas. Ir´á receber um mapa onde um '*' representa uma parede e 
um ' ' uma posição livre, onde 'P' marca a posição onde se encontra o Pac-Man e
'G' uma posição onde se encontra um fantasma. A função deve devolver a posição
para onde o Pac-Man se deve deslocar (uma das posições adjancentes, sendo que
apenas se pode movimentar na horizontal ou vertical, ou a posição onde se
encontra, se a melhor opção for ficar quieto), por forma a que fique o mais
distante possível de um fantasma. Caso haja mais do que uma posição ideal a 
prioridade deverá ser: ficar quieto, desloar-se para cima, deslocar-se para
baixo, deslocar-se para a direita, e deslocar-se para esquerda.
A posição consiste na coordenada horizontal (medida da esquerda para a direita)
e na coordenada vertical (medida de cima para baixo).

"""
def bfs(mapa, origem, fantasmas):
    distancias = []
    pai = {}
    queue = [origem]
    for fantasma in fantasmas:
        while queue:
            x, y = queue.pop(0)
            if (x, y) == fantasma:
                break
            for i in [-1, 1]:
                dx = (x + i) % len(mapa[0])
                dy = (y + i) % len(mapa)
                if mapa[y][dx] in [' ', 'P', 'G'] and (dx, y) not in pai:
                    pai[(dx, y)] = (x, y)
                    queue.append((dx, y))
                if mapa[(dy) % len(mapa)][x] in [' ', 'P', 'G'] and (x, dy) not in pai:
                    pai[(x, dy)] = (x, y)
                    queue.append((x, dy))
                
        caminho = [fantasma]
        ponto = fantasma
        while ponto != origem:
            ponto = pai[ponto]
            caminho.insert(0, ponto)
            
        distancias.append(len(caminho))
        
    return distancias

def pacman(mapa):
    inicio = None
    fantasmas = []
    posicoes = []
    
    #posicóes do pac-man e dos fantasmas
    for i in range(len(mapa)):
        if 'P' in mapa[i]:
            inicio = (mapa[i].index('P'), i)
        if 'G' in mapa[i]:
            for j in range(len(mapa[i])):
                if mapa[i][j] == 'G':
                    fantasmas.append((j, i))
                    
    #se não houver fantasmas, fica quieto
    if not fantasmas:
        return inicio
    
    if inicio is not None:
        posicoes.append(inicio)
        x, y = inicio
    for p in [(x, (y - 1) % len(mapa)), (x, (y + 1) % len(mapa)), ((x + 1) % len(mapa[0]), y), ((x - 1) % len(mapa[0]), y)]:
        if mapa[p[1]][p[0]] == ' ':
            posicoes.append(p)
            
    #dicionário que liga cada ponto à lista dos tamanhos mais curtos até cada fantasma
    distancias = {}
    for ponto in posicoes:
        distancias[ponto] = bfs(mapa, ponto, fantasmas)
        
    lista_distancias = list(distancias.items())
    lista_distancias.sort(key = lambda t: min(t[1]), reverse = True)
    
    return lista_distancias[0][0] 
