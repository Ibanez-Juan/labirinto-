labirinto = """
1111111111111111111111111111111111111111
1T00000000000000A00000000000100010000001
1010101010110101011111101010001010101101
101011111011010100000010101010000000000S
1010001010111101011110000000110101011101
1011111100000110100000011110110101010101
1011111111111101011111111110110101110101
101000000000000A0000000000100000A0000001
1011011010101010101010101010111010101101
1010001000100001000010000010101000101101
1010111111111111111111111110101110111101
100000000000001A000000100000100000000001
1111111111111111111111111111111111111111
"""
#Exemplo de labirinto
PASSAGEM, PAREDE, SAIDA, ARTEFATOS, TESEU, PASSEI, SOLUCAO = "01SAT.o"

# parte do código que faz com que o Teseu caminhe no
# labirinto e armazena os valores em uma lista


def saiu(x, y):
    if lab[x][y] == SAIDA:
        return True
    # quero salvar o valor de artefatos para contar apenas os que estiverem no caminho da solução
    if lab[x][y] in (TESEU, PASSAGEM, ARTEFATOS):
        lab[x][y] = PASSEI
        if saiu(x-1, y) or saiu(x+1, y) or saiu(x, y-1) or saiu(x, y+1):
            lab[x][y] = SOLUCAO
            print(x, y)  # quero salvar esse valor em uma var.
            return True
    else:
        return False


lab = []


# fatia o labirinto e se for maior que Zero
# os valores de x são armazenados na lista lab
for x in labirinto.splitlines():
    if len(x) > 0:
        x = list(x)
        lab.append(x)


for j in range(len(lab)):
    for k in range(len(lab[j])):
        if lab[j][k] == TESEU:
            x = j
            y = k
            break


if saiu(x, y):
    for linha in lab:
        print(''.join(linha))
else:
    print("Labirinto sem saída")

# contar e armazenar os dados
passosSaida, passosAndados = 0, 0
for i in range(len(lab)):
    for j in range(len(lab[i])):
        if lab[i][j] == SOLUCAO:
            passosSaida += 1
        if lab[i][j] == PASSEI:
            passosAndados += 1

passosTotais = passosAndados + passosSaida

print(passosSaida, passosTotais)
