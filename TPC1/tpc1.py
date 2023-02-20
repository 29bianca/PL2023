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


def tabela_distSexo(dados):
    dados = dist_sexo(dados)
    print("\n\n|-------------------------------------------|")
    print("|           Distribuição por Sexo           |")
    print("|-------------------------------------------|")
    print("|   Sexo   |  Doentes |   Total  |    (%)   |")
    print("|-------------------------------------------|")
    print('|  {:<8}|  {:<8}|  {:<8}|  {:<8}|'.format("Homem",str(dados['M']),str(dados['M2']), str("{:.2f}%".format((dados['M'] / dados['M2']) * 100))))
    print("|-------------------------------------------|")
    print('|  {:<8}|  {:<8}|  {:<8}|  {:<8}|'.format("Mulher",str(dados['F']),str(dados['F2']), str("{:.2f}%".format((dados['F'] / dados['F2']) * 100))))
    print("|-------------------------------------------|\n\n")


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


def tabela_distEscalao(aidade, atotal, adoentes):
    print("\n\n|--------------------------------------------------|")
    print("|         Distribuição por Escalão Etário          |")
    print("|--------------------------------------------------|")
    print("| Escalão Etário  | Doentes  |   Total  |    (%)   |")
    print("|--------------------------------------------------|")
    for i, d, t in zip(aidade, atotal, adoentes):
        #print(i, t, d)
        print("|      {:<11}|  {:<8}|  {:8}|  {:<8}|".format(str(i), str(t), str(d), str("{:.2f}%".format((t / d) * 100))))
        print("|--------------------------------------------------|")


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

# Array com todos os escalões
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

def tabela_distColesterol(idade,nPessoas,nDoentes):
    print("\n\n|-------------------------------------------|")
    print("|    Distribuição por Nível de Colesterol   |")
    print("|-------------------------------------------|")
    print("|  Nível Colesterol   | Doentes  |   Total  |")
    print("|-------------------------------------------|")

    for i,n,d in zip(idade, nPessoas, nDoentes):
        print("|        {:<13}|  {:<8}|  {:<8}|".format(str(i), str(d), str(n), ))
        print("|-------------------------------------------|")   


def main():
    ficheiro = 'myheart.csv'
    dados=ler_infos(ficheiro)
    
    #print('Dados lidos: ')
    #for linha in dados:
    #    print(linha)

    distDoencaSexo = dist_sexo(dados)
    #print ('A distribuição da doença por sexo é: ', distDoencaSexo)

    idadeMin = idade_min(dados)
    #print(idadeMin)

    idadeMax = idade_max(dados)
    #print(idadeMax)

    escaloesIdade = escalao(idadeMin,idadeMax)
    #print(escaloesIdade)

    distEscalao = dist_escalao(dados,escaloesIdade)
    #print(distEscalao)

    distDoencaEsc = dist_doencaEsc(dados,escaloesIdade)
    #print(distDoencaEsc)

    colMin = colesterol_min(dados)
    #print(colMin)

    colMax = colesterol_max(dados)
    #print(colMax)

    escaloesColesterol = escalao_colesterol(colMin,colMax)
    #print(escaloesColesterol)

    distColesterol = dist_colesterol(dados,escaloesColesterol)
    #print(distColesterol)

    distColesterolEsc = dist_colesterolEsc(dados,escaloesColesterol)
    #print(distColesterolEsc)



# Loop principal do programa
    while True:
        print("Escolha uma opção:")
        print("1. Tabela Distribuição por sexo")
        print("2. Tabela Distribuição por escalão etário")
        print("3. Tabela Distribuição por nível de colesterol")
        print("4. Sair")
        escolha = input("Digite o número da opção desejada: ")
    
    # Verificar a escolha do usuário
        if escolha == "1":
            tabela_distSexo(dados)
        elif escolha == "2":
            tabela_distEscalao(escaloesIdade,distEscalao,distDoencaEsc)
        elif escolha == "3":
            tabela_distColesterol(escaloesColesterol,distColesterol, distColesterolEsc)
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Tente novamente.")


if __name__ == '__main__':
    main()

