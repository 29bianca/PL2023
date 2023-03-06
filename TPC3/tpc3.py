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

print(proc_ano(proc_file()))