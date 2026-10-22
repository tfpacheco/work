with open('aaaa.txt') as ficheiro:
    linhas = ficheiro.readlines()
    for linha in linhas:
        linha = linha.replace('python', 'JS')
        print(linha.rstrip())

print(len(linhas))
