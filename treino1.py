"""

Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.

"""

def aloca(prefs):
    prefs_ordenado = list(prefs.items())
    prefs_ordenado.sort(key = lambda t: t[0])
    alocados = []
    alunos = []
    
    for (aluno, lista) in prefs_ordenado:
        colocado = False
        for projecto in lista:
            if projecto not in alocados:
                alocados.append(projecto)
                colocado = True
                break
        if not colocado:
            alunos.append(aluno)
    
    return alunos
    
'''
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada 
por ordem crescente do número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos,
devem ser listadas por ordem lexicográfica do nome completo.
'''

def apelidos(nomes):
    nomes.sort(key = str.lower)
    nomes.sort(key = lambda completo: len(completo.split()))
    return nomes
    
'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.

Pretende-se que implemente uma função que lista os cruzamentos de uma cidade 
por ordem crescente de criticidade: um cruzamento é tão mais crítico quanto 
maior o número de ruas que interliga.

A entrada consistirá numa lista de nomes de ruas (podendo assumir que os nomes de ruas são únicos). 
Os identificadores dos cruzamentos correspondem a letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

A função deverá retornar uma lista com os nomes dos cruzamentos por ordem crescente de criticidade, 
listando para cada cruzamento um tuplo com o respectivo identificador e o número de ruas que interliga.
Apenas deverão ser listados os cruzamentos que interliguem alguma rua, e os cruzamentos com o mesmo 
nível de criticidade deverão ser listados por ordem alfabética.
'''

def cruzamentos(ruas):
    criticidade = {}
    
    for rua in ruas:
        if rua[0] not in criticidade:
            criticidade[rua[0]] = 1
        else:
            criticidade[rua[0]] += 1
        
        if rua[-1] not in criticidade:
            criticidade[rua[-1]] = 1
        elif rua[0] != rua[-1]:
            criticidade[rua[-1]] += 1
            
    tuplo = list(criticidade.items())
    tuplo.sort(key = lambda t: t[0])
    tuplo.sort(key = lambda t: t[1])
    
    return tuplo
    
'''
Defina uma função que recebe um número positivo
e produz a soma dos seus factores primos distintos.
'''

def factoriza(n):
    factores = []
    f = 3
    
    while n % 2 == 0:
        n //= 2
        if 2 not in factores:
            factores.append(2)
            
    while f*f <= n:
        while n % f == 0:
            n //= f
            if f not in factores:
                factores.append(f)
        f += 2
    
    if n > 1:
        factores.append(n)
        
    return sum(factores)
    
'''
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''

def frequencia(texto):
    d = {}
    
    for palavra in texto.split():
        if palavra not in d:
            d[palavra] = 1
        else:
            d[palavra] += 1
            
    tuplo = list(d.items())
    tuplo.sort(key = lambda x: x[0])
    tuplo.sort(key = lambda x: x[1], reverse = True)
    
    return [t[0] for t in tuplo]

'''

Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com 
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.

'''

def tabela(jogos):
    pontos = {}
    
    for timeA, golosA, timeB, golosB in jogos:
        if timeA not in pontos:
            pontos[timeA] = [0,0]
        if timeB not in pontos:
            pontos[timeB] = [0,0]
            
        score = golosA - golosB
        if score > 0:
            pontos[timeA][0] += 3
        elif score < 0:
            pontos[timeB][0] += 3
        else:
            pontos[timeA][0] += 1
            pontos[timeB][0] += 1
        pontos[timeA][1] += score
        pontos[timeB][1] += -score
        
    tabela_com_saldo = list(pontos.items())
    tabela_com_saldo.sort(key = lambda t: t[0])                            #ordena pelos nomes das equipas
    tabela_com_saldo.sort(key = lambda t: t[1][1], reverse = True)         #ordena pelo saldo de golos
    tabela_com_saldo.sort(key = lambda t: t[1][0], reverse = True)         #ordena pela pontuação
    
    return [(x, y[0]) for x, y in tabela_com_saldo]
    
"""
Um hacker teve acesso a um log de transações com cartões de
crédito. O log é uma lista de tuplos, cada um com os dados de uma transação,
nomedamente o cartão que foi usado, podendo alguns dos números estar
ocultados com um *, e o email do dono do cartão.

Pretende-se que implemente uma função que ajude o hacker a 
reconstruir os cartões de crédito, combinando os números que estão
visíveis em diferentes transações. Caso haja uma contradição nos números 
visíveis deve ser dada prioridade à transção mais recente, i.é, a que
aparece mais tarde no log.

A função deve devolver uma lista de tuplos, cada um com um cartão e um email,
dando prioridade aos cartões com mais digitos descobertos e, em caso de igualdade
neste critério, aos emails menores (em ordem lexicográfica).
"""

def hacker(log):
    dados = {}
    descobertos = {}
    
    for cartao, email in log:
        if email not in dados:
            dados[email] = list(cartao)
        else:
            for i in range(16):
                if cartao[i] != '*' and (dados[email][i] == '*' or (dados[email][i] != '*' and dados[email][i] != cartao[i])):
                    dados[email][i] = cartao[i]
    
    for email in dados:
        descobertos[email] = 0
        for i in range(16):
            if dados[email][i] != '*':
                descobertos[email] += 1
    
    lista = [(''.join(y), x) for x, y in list(dados.items())]
    lista.sort(key = lambda t: t[1])                                #ordena a lista de tuplos em ordem crescente referente ao e-mail (critério de desempate)
    lista.sort(key = lambda t: descobertos[t[1]], reverse = True)   #ordena a lista de tuplos em ordem decrescente referente ao valor de cada chave no dicionário descobertos
    
    return lista
    
'''
Pretende-se que implemente uma função que detecte códigos ISBN inválidos. 
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos, 
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
'''

def isbn(livros):
    validos = []
    
    for livro in livros:
        soma = 0
        for i in range(13):
            if i % 2 == 0:
                soma += int(livros[livro][i])
            else:
                soma += 3*(int(livros[livro][i]))
        if soma % 10 == 0:
            validos.append(livro)
            
    invalidos = [x for x in livros if x not in validos]
    invalidos.sort(key = str.lower)
    
    return invalidos
    
'''
Implemente uma função que determine qual a menor sequência de caracters que
contém n repetições de uma determinada palavra
'''

def repete(palavra,n):
    if(n == 0):
        return ''
        
    iguais = 0
    
    for i in range(len(palavra)):
        if palavra[0:i+1] == palavra[-1-i:]:
            iguais += 1
        else:
            break
            
    lista = list(palavra)
    if iguais != 0 and iguais != len(lista):
        del lista[:iguais]
    elif iguais == len(lista):
        del lista [:iguais - 1]
        
    sem_iguais = ''.join(lista)
    return palavra + (sem_iguais * (n - 1))

'''
Neste problema prentede-se que implemente uma função que calcula o rectângulo onde se movimenta um robot.

Inicialmente o robot encontra-se na posição (0,0) virado para cima e irá receber uma sequência de comandos numa string.
Existem quatro tipos de comandos que o robot reconhece:
  'A' - avançar na direcção para o qual está virado
  'E' - virar-se 90º para a esquerda
  'D' - virar-se 90º para a direita 
  'H' - parar e regressar à posição inicial virado para cima
  
Quando o robot recebe o comando 'H' devem ser guardadas as 4 coordenadas (minímo no eixo dos X, mínimo no eixo dos Y, máximo no eixo dos X, máximo no eixo dos Y) que definem o rectângulo 
onde se movimentou desde o início da sequência de comandos ou desde o último comando 'H'.

A função deve retornar a lista de todas os rectangulos (tuplos com 4 inteiros)
'''

def robot(comandos):
    lista = []
    flag = x = y = 0
    max_mins = [0,0,0,0]
    
    for comando in comandos:
        if comando == 'E':
            flag -= 1
        elif comando == 'D':
            flag += 1
        elif comando == 'A':
            if flag % 4 == 0:
                y += 1
                max_mins[3] = max(y, max_mins[3])
            elif flag % 4 == 1:
                x += 1
                max_mins[2] = max(x, max_mins[2])
            elif flag % 4 == 2:
                y -= 1
                max_mins[1] = min(y, max_mins[1])
            elif flag % 4 == 3:
                x -= 1
                max_mins[0] = min(x, max_mins[0])
        elif comando == 'H':
            lista.append(tuple(max_mins))
            flag = x = y = 0
            max_mins = [0,0,0,0]
    
    return lista
