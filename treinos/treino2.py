'''

Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 

'''

def area(p,mapa):
    if mapa[p[0]][p[1]] == '*':
        return 0
        
    queue = [p]
    visitados = set()
    
    while queue:
        x, y = queue.pop(0)
        visitados.add((x, y))
        
        for i in [-1, 1]:
            if 0 <= x + i < len(mapa) and (x + i, y) not in visitados and mapa[x + i][y] == '.':
                queue.append((x + i, y))
            if 0 <= y + i < len(mapa) and (x, y + i) not in visitados and mapa[x][y + i] == '.':
                queue.append((x, y + i))
                
    return len(visitados)
  
  
  '''

O objectivo deste problema é determinar quantos movimentos são necessários para 
movimentar um cavalo num tabuleiro de xadrez entre duas posições.
A função recebe dois pares de coordenadas, que identificam a origem e destino pretendido,
devendo devolver o número mínimo de saltos necessários para atingir o destino a partir da origem.
Assuma que o tabuleiro tem tamanho ilimitado.

'''

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
