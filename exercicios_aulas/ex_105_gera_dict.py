# Analisando e gerando Dicionários
def notas(*n, sit=False):
    """
    ---> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas de alunos - aceita várias.
    :param sit: valor opcional, indicando que deve ser explicitamente chamado ao final com sit=True
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = (sum(n) / len(n))
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = "RAZOÁVEL (ESTUDE, CARAI)"
        else:
            r['situação'] = 'RUIM (SE LIIIGA, HEIN?!?'
    return r


# Programa principal
resp = notas(7.3, 8.4, 3.7, sit=True)
print(resp)
help(notas)
