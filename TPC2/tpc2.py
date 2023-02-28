c = 0
i = 0

while 1:
    texto = input(">>")
    aux = ""

    if texto == "=":
        print(c)

    if texto.lower() == "off":
        i = 0

    if texto.lower() == "on":
        i = 1

    if i == 1:
        for x in texto:
            if x.isdigit():
                aux += x

            else:
                if aux != "":
                    c += int(aux)
                    aux = ""
        if aux != "":
            c += int(aux)
            aux = ""