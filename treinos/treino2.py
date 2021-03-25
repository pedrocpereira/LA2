'''

Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 

'''
# 13%

def area(p,mapa):

    if mapa[p[1]][p[0]] != '*':
        queue = [p]
    visitados = set()
    
    while queue:
        x, y = queue.pop(0)
        visitados.add((x, y))
        
        for i in [-1, 1]:
            if 0 <= x + i < len(mapa) and (x + i, y) not in visitados and mapa[y][x + i] == '.':
                queue.append((x + i, y))
            if 0 <= y + i < len(mapa) and (x, y + i) not in visitados and mapa[y + i][x] == '.':
                queue.append((x, y + i))
                
    return len(visitados)
  
 

'''

O objectivo deste problema é determinar quantos movimentos são necessários para 
movimentar um cavalo num tabuleiro de xadrez entre duas posições.
A função recebe dois pares de coordenadas, que identificam a origem e destino pretendido,
devendo devolver o número mínimo de saltos necessários para atingir o destino a partir da origem.
Assuma que o tabuleiro tem tamanho ilimitado.

'''
# 13%

def saltos(o,d):
    if o == d:
        return 0
    
    orla = [(o[0],o[1], 0)]
    visitados = set()
    
    while orla:
        x, y, total = orla.pop(0)
        visitados.add((x,y))
        
        for sinal_hor in [-1, 1]:
            for sinal_ver in [-1, 1]:
                if (x + sinal_hor, y + sinal_ver * 2) == d or (x + sinal_hor * 2, y + sinal_ver) == d:
                    return total + 1
                if (x + sinal_hor, y + sinal_ver * 2) not in visitados:
                    orla.append((x + sinal_hor, y + sinal_ver * 2, total + 1))
                if (x + sinal_hor * 2, y + sinal_ver) not in visitados:
                    orla.append((x + sinal_hor * 2, y + sinal_ver, total + 1))
            
 
            
'''

Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.
Pretende-se que implemente uma função que calcula o tamanho de uma cidade, 
sendo esse tamanho a distância entre os seus cruzamentos mais afastados.
A entrada consistirá numa lista de nomes de ruas (podendo assumir que os 
nomes de ruas são únicos). Os identificadores dos cruzamentos correspondem a 
letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

'''
# 10%

def build(ruas):
    adj = {}
    for rua in ruas:
        x, y = rua[0], rua[-1]
        if x not in adj:
            adj[x] = {}
        if y not in adj:
            adj[y] = {}
        if x != y:
            if x not in adj[y]:
                adj[x][y] = len(rua)
                adj[y][x] = len(rua)
            else:
                adj[x][y] = min(len(rua), adj[x][y])
                adj[y][x] = min(len(rua), adj[y][x])
    return adj
 
def tamanho(ruas):
    adj = build(ruas)
    dist = {}
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")
                
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d]
                    
    maximos = [max(dist[v].items())[1] for v in dist]
    
    return max(maximos)

            
'''

O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.

'''
# 13%

def build(vizinhos):
    adj = {}
    
    for fronteira in vizinhos:
        for pais in fronteira:
            if pais not in adj:
                adj[pais] = []
            for vizinho in fronteira:
                if vizinho != pais and vizinho not in adj[pais]:
                    adj[pais].append(vizinho)
                    
    return adj
    
def dfs(adj, o, vis, pai):
    vis.add(o) 
    for d in adj[o]: 
        if d not in vis: 
            pai[d] = o 
            dfs(adj,d,vis,pai) 
    return pai
            

def maior(vizinhos):
    adj = build(vizinhos)
    travessias = [dfs(adj, x, set(), {}) for x in adj]
    maiores = []
    for pai in travessias:
        tamanho = 1
        for key in pai:
            visitados = set()
            counter = 0
            while key:
                visitados.add(key)
                key = pai.get(key, False)
                counter += 1
            if counter > tamanho:
                tamanho = counter
        maiores.append(tamanho)

    return max(maiores) if maiores else 0

            
'''

O número de Erdos é uma homenagem ao matemático húngaro Paul Erdos,
que durante a sua vida escreveu cerca de 1500 artigos, grande parte deles em 
pareceria com outros autores. O número de Erdos de Paul Erdos é 0. 
Para qualquer outro autor, o seu número de Erdos é igual ao menor 
número de Erdos de todos os seus co-autores mais 1. Dado um dicionário que
associa artigos aos respectivos autores, implemente uma função que
calcula uma lista com os autores com número de Erdos menores que um determinado 
valor. A lista de resultado deve ser ordenada pelo número de Erdos, e, para
autores com o mesmo número, lexicograficamente.

'''
# 13%

def erdos(artigos,n):
    numero = {"Paul Erdos": 0}
    queue = ["Paul Erdos"]
    
    while queue:
        autor = queue.pop(0)
        for artigo in artigos:
            if autor in artigos[artigo]:
                for coautor in artigos[artigo]:
                    if coautor not in numero:
                        numero[coautor] = numero[autor] + 1
                        queue.append(coautor)
                        
    lista = [x for x in numero if numero[x] <= n]
    lista.sort(key = str.lower)
    lista.sort(key = lambda y: numero[y])
                    
    return lista


'''

Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista 
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruções podem ser 'N','S','E','O'.

'''
# 13%

def caminho(mapa):
    pai = {}
    queue = [(0,0)]
    fim = (len(mapa) - 1, len(mapa) - 1)
    anterior = (0,0)
    result = ''
    
    #travessia em largura
    while queue:
        x, y = queue.pop(0)
        if (x, y) == fim:
            break
        for i in [-1, 1]:
            if 0 <= x + i < len(mapa) and mapa[y][x + i] == ' ' and (x + i, y) not in pai:
                pai[(x + i, y)] = (x, y)
                queue.append((x + i, y))
            if 0 <= y + i < len(mapa) and mapa[y + i][x] == ' ' and (x, y + i) not in pai:
                pai[(x, y + i)] = (x, y)
                queue.append((x, y + i))
                
    #caminho mais curto
    caminho = [fim]
    ponto = fim
    while ponto != (0,0):
        ponto = pai[ponto]
        caminho.insert(0, ponto)
        
    while caminho:
        atual = caminho.pop(0)
        if atual[0] > anterior[0]:
            result += 'E'
        elif atual[0] < anterior[0]:
            result += 'O'
        elif atual[1] > anterior[1]:
            result += 'S'
        elif atual[1] < anterior[1]:
            result += 'N'
        anterior = atual
    
    return result


'''

Implemente uma função que calcula o menor custo de atravessar uma região de
Norte para Sul. O mapa da região é rectangular, dado por uma lista de strings,
onde cada digito representa a altura de cada ponto. Só é possível efectuar 
movimentos na horizontal ou na vertical, e só é possível passar de um ponto
para outro se a diferença de alturas for inferior ou igual a 2, sendo o custo 
desse movimento 1 mais a diferença de alturas. O ponto de partida (na linha
mais a Norte) e o ponto de chegada (na linha mais a Sul) não estão fixados à
partida, devendo a função devolver a coordenada horizontal do melhor
ponto para iniciar a travessia e o respectivo custo. No caso de haver dois pontos
com igual custo, deve devolver a coordenada mais a Oeste.

'''
# 13%

def dijkstra(mapa, o):
    dist = {o: 0}
    orla = {o}
    while orla:
        x, y = min(orla, key = lambda x: dist[x])
        orla.remove((x, y))
        for i in [-1, 1]:
            dx = x + i
            dy = y + i
            if 0 <= dx < len(mapa[0]) and abs(int(mapa[y][dx]) - int(mapa[y][x])) <= 2 and (dx, y) not in dist:
                orla.add((dx, y))
                dist[(dx, y)] = 1 + abs(int(mapa[y][dx]) - int(mapa[y][x])) + dist[(x, y)]
            if 1 <= dy < len(mapa) and abs(int(mapa[dy][x]) - int(mapa[y][x])) <= 2 and (x, dy) not in dist:
                orla.add((x, dy))
                dist[(x, dy)] = 1 + abs(int(mapa[dy][x]) - int(mapa[y][x])) + dist[(x, y)]
    
    result = [dist[x] for x in dist if x[1] == (len(mapa) - 1)]
    return min(result) if result else float("inf")
    
def travessia(mapa):
    dist = [(x, dijkstra(mapa, (x, 0))) for x in range(len(mapa[0]))]
    dist.sort(key = lambda t: t[1])
    return dist[0]


'''

Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.

'''
# 13%

def build(rotas):
    adj = {}
    
    for rota in rotas:
        i = 0
        while i + 2 < len(rota):
            o = rota[i]
            c = rota[i + 1]
            d = rota[i + 2]
            if o not in adj:
                adj[o] = {}
            if d not in adj:
                adj[d] = {}
            adj[o][d] = c
            adj[d][o] = c
            i += 2
    
    return adj
    
def fw(adj): 
    dist = {} 
    
    for o in adj: 
        dist[o] = {} 
        for d in adj: 
            if o == d: 
                dist[o][d] = 0 
            elif d in adj[o]: 
                dist[o][d] = adj[o][d] 
            else: 
                dist[o][d] = float("inf")
                
    for k in adj: 
        for o in adj: 
            for d in adj: 
                if dist[o][k] + dist[k][d] < dist[o][d]: 
                    dist[o][d] = dist[o][k] + dist[k][d] 
 
    return dist

def viagem(rotas,o,d):
    if o == d:
        return 0
    
    dist = fw(build(rotas))
    
    return dist[o][d]
