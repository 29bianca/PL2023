def ler_infos(ficheiro):
    with open(ficheiro) as f:
        next(f)     #a primeira linha do ficheiro do csv não interessa

        dados=[]    #matriz com os dados

        for linha in f:
            campos = linha.strip().split(",")
            idade = int(campos[0])
            sexo = campos[1]
            tensao = int(campos[2])
            colesterol = int(campos[3])
            batimento = int(campos[4])
            temDoenca = bool(int(campos[5]))

            dic_dados = {'idade':idade,
                         'sexo':sexo,
                         'tensão':tensao,
                         'colesterol':colesterol,
                         'batimento':batimento,
                         'temDoença':temDoenca
                         }
            dados.append(dic_dados)
    return dados            

#--------------------Distribuição por Sexo----------------------#
def dist_sexo(dados):
    dist = {'M': 0, 'F': 0, 'M2':0, 'F2':0}
    for linha in dados:
        sexo = linha['sexo']
        temDoenca = linha['temDoença']

        if temDoenca:
            dist[sexo]+=1

        if sexo == 'M':
            dist['M2']+=1
        else:
             dist['F2']+=1

    return dist   

#--------------------Distribuição por Escalão Etário----------------------#

def idade_min(dados):
    min = 1000
    for linha in dados:
        if linha['idade'] < min:
            min = linha['idade']
    return min

def idade_max(dados):
    max = 0
    for linha in dados:
        if linha['idade'] > max:
            max = linha['idade']
    return max    

def escalao(idademin, idademax):
    escaloes = []
    for i in range(idademin, idademax + 1, 5):
        escaloes.append((i, i + 4))
    return escaloes

def dist_escalao(dados,escaloes): #nr pessoas num dado escalao
    array = []
    for e in escaloes:
        min = e[0] 
        max = e[1]
        c = 0
        for i in dados:
            if i['idade'] >= min and i['idade']<= max:
                c+=1
        array.append(c)  
    return array          

def dist_doencaEsc(dados,escaloes): #nr pessoas que tem a doença e que esta num dado escalao
    array = []
    for e in escaloes:
        min = e[0] 
        max = e[1]
        c = 0
        for i in dados:
            if i['idade'] >= min and i['idade']<= max and i['temDoença'] == True:
                c+=1
        array.append(c)  
    return array   

#--------------------Distribuição por Níveis de Colesterol----------------------#
def colesterol_min(dados):
    min = 1000
    for linha in dados:
        if linha['colesterol'] < min and linha['colesterol'] != 0:
            min = linha['colesterol']
    return min

def colesterol_max(dados):
    max = 0
    for linha in dados:
        if linha['colesterol'] > max:
            max = linha['colesterol']
    return max    

def escalao_colesterol(colmin, colmax):
    escColes = []
    for i in range(colmin, colmax + 1, 10):
        escColes.append((i, i + 9))
    return escColes

def dist_colesterol(dados,escaloes): 
    array = []
    for e in escaloes:
        min = e[0] 
        max = e[1]
        c = 0
        for i in dados:
            if i['colesterol'] >= min and i['colesterol']<= max:
                c+=1
        array.append(c)  
    return array          


def dist_colesterolEsc(dados,escaloes): 
    array = []
    for e in escaloes:
        min = e[0] 
        max = e[1]
        c = 0
        for i in dados:
            if i['colesterol'] >= min and i['colesterol']<= max and i['temDoença']==1:
                c+=1
        array.append(c)  
    return array   



def main():
    ficheiro = 'myheart.csv'
    dados=ler_infos(ficheiro)
    print('Dados lidos: ')
    for linha in dados:
        print(linha)

    distDoencaSexo = dist_sexo(dados)
    print ('A distribuição da doença por sexo é: ', distDoencaSexo)

    idadeMin = idade_min(dados)
    print(idadeMin)

    idadeMax = idade_max(dados)
    print(idadeMax)

    escaloesIdade = escalao(idadeMin,idadeMax)
    print(escaloesIdade)

    distEscalao = dist_escalao(dados,escaloesIdade)
    print(distEscalao)

    distDoencaEsc = dist_doencaEsc(dados,escaloesIdade)
    print(distDoencaEsc)

    colMin = colesterol_min(dados)
    print(colMin)

    colMax = colesterol_max(dados)
    print(colMax)

    escaloesColesterol = escalao_colesterol(colMin,colMax)
    print(escaloesColesterol)

    distColesterol = dist_colesterol(dados,escaloesColesterol)
    print(distColesterol)

    distColesterolEsc = dist_colesterolEsc(dados,escaloesColesterol)
    print(distColesterolEsc)


if __name__ == '__main__':
    main()

