"""

Implemente uma função que formata um programa em C.
O código será fornecido numa única linha e deverá introduzir
um '\n' após cada ';', '{', ou '}' (com excepção da última linha).
No caso do '{' as instruções seguintes deverão também estar identadas
2 espaços para a direita.

"""

def formata(codigo):
    especiais = [';', '{', '}']
    string = ''
    counter = 0
    flag = 0               #1 se o último char é especial, 0 caso contrário
    
    for i in range(len(codigo)):
        if codigo[i] == '{':
            counter += 2
        elif codigo[i] == '}':
            counter -= 2
        
        if flag == 1 and codigo[i] in especiais:
            string = string + '\n' + (' ' * counter) + codigo[i]
        elif flag == 1 and codigo[i] == ' ':
            continue
        elif flag == 1 and codigo[i] not in especiais:
            string = string + '\n' + (' ' * counter) + codigo[i]
            flag = 0
        elif flag == 0 and codigo[i] in especiais:
            string = string + codigo[i]
            flag = 1
        else:
            string += codigo[i]
            
    return string
  
  
  
 """

Implemente uma função que calcula o horário de uma turma de alunos.
A função recebe dois dicionários, o primeiro associa a cada UC o
respectivo horário (um triplo com dia da semana, hora de início e
duração) e o segundo associa a cada aluno o conjunto das UCs em
que está inscrito. A função deve devolver uma lista com os alunos que
conseguem frequentar todas as UCs em que estão inscritos, indicando
para cada um desses alunos o respecto número e o número total de horas
semanais de aulas. Esta lista deve estar ordenada por ordem decrescente
de horas e, para horas idênticas, por ordem crescente de número.

"""

def horario(ucs,alunos):
    resultado = []
    
    for numero in alunos:
        total = 0
        frequencia = True
        indisponiveis = {}
        for cadeira in alunos[numero]:
            if cadeira not in ucs:
                frequencia = False
                break
            else:
                (dia, hora, duracao) = ucs[cadeira]
            if not disponibilidade(ucs[cadeira], indisponiveis):
                frequencia = False
                break
            else:
                if dia not in indisponiveis:
                    indisponiveis[dia] = []
                for i in range(duracao + 1):
                    indisponiveis[dia].append(hora + i)
                total += duracao
        if frequencia:
            resultado.append((numero, total))
    
    resultado.sort(key = lambda t: t[0])
    resultado.sort(key = lambda t: t[1], reverse=True)
    
    return resultado
    

def disponibilidade(t, indisponiveis):
    pode = True
    if t[0] in indisponiveis:
        for i in range(t[2] + 1):
            if (t[1] + i) in indisponiveis[t[0]]:
                pode = False
                break
    
    return pode
