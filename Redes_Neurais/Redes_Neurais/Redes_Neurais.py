import numpy as np

entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
#saidas = np.array([[0],[1],[1],[1]]) Para OR
saidas = np.array([[0],[0],[0],[1]]) #Para AND
pesos = np.array([[0.0],[0.0]])
#pesos = 2 * np.random.random((1,2)) - 1 #Gerando os pesos de modo aleatório

taxaAprendizagem = 0.1
epocaMaxima = 20

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

def calculaSaida(entradas):
    s = entradas.dot(pesos)
    return stepFunction(s)


def treinar():
    epoca = 0
    erroTotal = 1
    while (erroTotal != 0):
        epoca +=1
        if(epoca == epocaMaxima):
            print("A rede não foi capaz de aprender!")
            return

        print('Epoca: ' + str(epoca))
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = saidas[i] - saidaCalculada
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('Peso atualizado: ' + str(pesos[j]))
            print('Total de erros: ' + str(erroTotal))

treinar()
