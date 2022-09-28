import math


def troca_linhas(matrix, row1, row2):
    # row1 <-> row2
    new_row1 = []
    new_row2 = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == row1:
                new_row2 = new_row2 + [matrix[i][j]]
            if i == row2:
                new_row1 = new_row1 + [matrix[i][j]]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == row1:
                matrix[i][j] = new_row1[j]
            if i == row2:
                matrix[i][j] = new_row2[j]


def combinacao_linear(matrix, row1, row2, a):
    # r1 + a*r2 -> r1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == row1:
                matrix[i][j] = matrix[i][j] + a*matrix[row2][j]

    print_matrix(matrix)


def multiplica_linha(matrix, row, a):
    # a*row -> row
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == row:
                matrix[i][j] *= a


def escalonamento(matrix):
    linha_pivo = 0

    for j in range(len(matrix[0])-2):
        for i in range(len(matrix)):
            if i > j:
                if not matrix[linha_pivo][j] == 0.0:
                    combinacao_linear(matrix, i, linha_pivo, -
                                      matrix[i][j]/matrix[linha_pivo][j])
                else:
                    error = 1
                    for k in range(i, len(matrix)):
                        if not matrix[k][j] == 0.0:
                            troca_linhas(matrix, k, linha_pivo)
                            combinacao_linear(
                                matrix, i, linha_pivo, -matrix[i][j] / matrix[linha_pivo][j])
                            error = 0
                            break
                    if error == 1:
                        print("Error")
                        break

        linha_pivo += 1

    return matrix


def solucao(matrix):
    count = 1
    conjunto_solucao = []

    for i in range(len(matrix)-1, -1, -1):
        valor = matrix[i][len(matrix[0])-1]
        pos_solucao = 0
        for j in range(len(matrix[0])-2, len(matrix[0])-count-2, -1):
            if j == len(matrix[0])-count-1:
                valor /= matrix[i][j]
            else:
                valor -= matrix[i][j] * \
                    conjunto_solucao[len(conjunto_solucao)-1-pos_solucao]
                pos_solucao += 1

        conjunto_solucao = [round(valor, 16)] + conjunto_solucao
        count += 1

    return conjunto_solucao


def print_matrix(matrix):
    for i in range(len(matrix)):
        print('| ', end='')
        for j in range(len(matrix[0])):
            print('[' + str(matrix[i][j]) + '] ', end='')
        print('|')
    print()


if __name__ == '__main__':
    areia = 9.974
    cascalho_fino = 0.23033
    cascalho_grosso = 0.7891
    #9.974, 0.23033 e 0.7891 
    

    # [areia, cascalho_fino, cascalho_grosso, outro_valor]
    matrix = [
        #areia, areia, areia
        # cascalho fino, cascalho fino, cascalho fino
        # cascalho grosso, cascalho grosso, cascalho grosso
        [14.0/1000, 20.0 / 1000, 26.0 / 1000, areia],
        [0.4 / 1000, 0.45 / 1000, 0.56 / 1000, cascalho_fino],
        [1.3 / 1000, 1.6/ 1000, 1.9 / 1000, cascalho_grosso]
    ]

    print_matrix(matrix)

    matrix_escalonada = escalonamento(matrix)

    print(solucao(matrix_escalonada))