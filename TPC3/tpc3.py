import math
import re 

def proc_file():
    with open('processos.txt', 'r') as f:
        linhas = f.readlines()

        pattern = re.compile(r"^(?P<Pasta>\d+)::(?P<Data>\d{4}\-\d{2}\-\d{2})?::(?P<Nome>[a-zA-Z \,\.\(\)]+)?::(?P<Pai>[a-zA-Z \,\.\(\)]+)?::(?P<Mae>[a-zA-Z \,\.\(\)]+)?::(?P<Observacoes>(\s*.*\s*)*)?::$")
        linhasProcess = []

    for linha in linhas:
        linhasProcess.append(pattern.match(linha).groupdict())

    return linhasProcess


def proc_ano(linhasProcess):
    dic = {}
    pattern = re.compile(r"(\d{4})")

    for linha in linhasProcess:
        data = linha["Data"]
        ano = pattern.match(data).group(1)
        if ano in dic:
            dic[ano] +=1
        else:
            dic[ano] = 1
    return dic        

#print(proc_ano(proc_file()))
#print(proc_file())

def freq_nomes(linhasProcess):
    patternNome = re.compile(r"^(?P<nome>\w+)\b.*?\b((?P<sobrenome>\w+))?$")
    patternAno = re.compile(r"(\d{4})")
    dic = {}

    for linha in linhasProcess:
        data = linha["Data"]
        ano = patternAno.match(data).group(1)
        seculo = math.floor(int(ano) / 100) + 1
        nomes = patternNome.search(linha["Nome"])
        if seculo not in dic.keys():
            dic[seculo] = {}
        if nomes != None:
            for nome in [nomes['nome'],nomes['sobrenome']]:
                if nome not in dic[seculo].keys():
                    dic[seculo][nome] = 1
                else:
                    dic[seculo][nome] += 1
        

    # Ordernar dicionário
    for key,value in dic.items():
        dic[key] = dict(sorted(value.items(), key=lambda x: x[1], reverse=True))

    for key,value  in dic.items():
        print("** TOP 5 [SEC " + str(key) + "] **")

        for i, (key,value) in enumerate(dic[key].items()):
            if (i>4):
                break
            print(str(i+1) + ". " + key + " (" +str(value)+")")
        print("")
    

freq_nomes(proc_file())