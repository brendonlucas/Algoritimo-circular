def main():
    processos = [10, 4, 3]
    quantun = 2
    troca_contexto = 0
    matriz = cria_matriz(processos)
    completa_matriz(matriz, processos, quantun, troca_contexto)
    faz_o_calculo_tme(matriz)
    faz_o_calculo_turnaround(matriz)


def faz_o_calculo_turnaround(matriz):
    for i in range(len(matriz)):
        soma = matriz[i][0] + matriz[i][1]
        print("O tempo de Turnaround do processo", i, "é", soma, "u.t")


def faz_o_calculo_tme(matriz):
    qtd_processos = len(matriz)
    soma = 0
    for i in range(len(matriz)):
        tempo_de_espera_atual = matriz[i][1]
        soma += tempo_de_espera_atual
    media = soma / qtd_processos
    print("O Tempo medio de espera =", media, "u.t")


def completa_matriz(matriz, processos, quantun, troca_contexto):
    while True:
        for i in range(len(processos)):
            tempo_processo_atual = processos[i]
            sub = tempo_processo_atual - quantun
            if sub >= 0:
                matriz[i][0] = matriz[i][0] + quantun
                for j in range(len(matriz)):
                    if j != i and processos[j] > 0:
                        matriz[j][1] = matriz[j][1] + quantun + troca_contexto
                processos[i] = sub

            if sub < 0:
                matriz[i][0] = matriz[i][0] + processos[i]
                for k in range(len(matriz)):
                    if k != i and processos[k] > 0:
                        matriz[k][1] = matriz[k][1] + processos[i] + troca_contexto
                processos[i] = 0

        for t in range(len(processos)):
            temp = processos[t]
            if sum(processos) == temp:
                matriz[t][0] = matriz[t][0] + temp
                processos[t] = 0
                break

        if sum(processos) == 0:
            break


def cria_matriz(processos):
    lista = []
    for i in range(len(processos)):
        lista.append([0, 0])
    return lista


if __name__ == '__main__':
    main()
