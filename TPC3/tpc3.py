import re 

def proc_file():
    with open('processos.txt', 'r') as f:
        linhas = f.readlines()

        pattern = re.compiler(r"^(?P<Pasta>\d+)::(?P<Data>\d{4}\-\d{2}\-\d{2})?::(?P<Nome>[a-zA-Z \,\.\(\)]+)?::(?P<Pai>[a-zA-Z \,\.\(\)]+)?::(?P<Mae>[a-zA-Z \,\.\(\)]+)?::(?P<Observacoes>(\s*.*\s*)*)?::$")
        linhasProcess = []

    for linha in linhas:
        linhasProcess.append(pattern.match(linha).groupdict())

    return linhasProcess    

