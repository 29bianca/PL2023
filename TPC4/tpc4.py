import re
import json

def fic(ficheiro):
    lista = []
    regexp= re.compile(r"(?P<Numero>[^,]+),(?P<Nome>[^,]+),(?P<Curso>[^,]+),?(?P<Notas>[^{,]+)?(?P<Intervalo>\{\d(?:,\d)?\})?(?:::)?(?P<Agregação>[^,]+)?")
    with open(ficheiro,'r') as file:
        l_info = file.readline()[:-1] 
        arr_grup = (regexp.match(l_info).groupdict())
        linhas = file.readlines()
        for linha in linhas:
            aux = {}
            pos_split = linha.replace('\n', '').split(',')

            if(arr_grup['Numero']is not None):
                aux['Numero'] = pos_split[0]

            if(arr_grup['Nome']is not None):
                aux['Nome'] = pos_split[1]

            if(arr_grup['Curso']is not None):
                aux['Curso'] = pos_split[2] 

            if (arr_grup['Notas'] is not None):
                if (arr_grup['Intervalo'] is not None):
                    regexp_intervalos = re.compile(r"{(?P<Minimo>\d),?(?P<Maximo>\d)?}")
                    numeros = (regexp_intervalos.match(arr_grup['Intervalo']).groupdict())
                    numero_minimo_notas = int(numeros['Minimo'])
                    if(numeros['Maximo'] is not None):                                        
                        numero_maximo_notas = int(numeros['Maximo'])                                        
                        notas = [int(x) for x in pos_split[3:3+numero_maximo_notas] if x.isdigit()]
                    else: 
                        notas = [int(x) for x in pos_split[3:3+numero_minimo_notas] if x.isdigit()]
                    if (arr_grup['Agregação'] is not None):
                        if (arr_grup['Agregação'] == 'sum'):
                            soma = sum(notas)
                            aux['Nota'] = soma
                        else:
                            media = sum(notas) / len(notas)
                            aux['Nota'] = media
                    else:
                        aux['Nota'] = notas
                else:
                    aux['Nota'] = pos_split[3]
            lista.append(aux)   
        return lista
    

def escrever_json(list_dic, ficheiro):
    with open(ficheiro, 'w') as f:
        json.dump(list_dic, f, indent=2, separators=(',', ': '))

def main_menu():
    print("========== MENU ==========")
    print("1. alunos.csv")
    print("2. alunos2.csv")
    print("3. alunos3.csv")
    print("4. alunos4.csv")
    print("5. alunos5.csv")
    print("6. Sair")

    choice = input("Digita o número que pretende: ")
    if choice == '1':
        l = fic("alunos.csv")
        escrever_json(l,"alunos.json")
        print("json alunos criado...")
    elif choice == '2':
        l = fic("alunos2.csv")
        escrever_json(l,"alunos2.json")
        print("json alunos2 criado...")
    elif choice == '3':
        l = fic("alunos3.csv")
        escrever_json(l,"alunos3.json")
        print("json alunos3 criado...")
    elif choice == '4':
        l = fic("alunos4.csv")
        escrever_json(l,"alunos4.json")
        print("json alunos4 criado...")
    elif choice == '5':
        l = fic("alunos5.csv")
        escrever_json(l,"alunos5.json")
        print("json alunos5 criado...")
    elif choice == '6':
        print("A sair...")
        return
    else:
        print("Não é válido")
        main_menu()

def main():
    main_menu()
    
if __name__ == '__main__':
    main()