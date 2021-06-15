# José Emanuel Lopes Santos
# Matrícula: 201851368558
# ----------------- AV2 IA ----------------------

import random
from numpy import array

# Classe que defini os atributos de cada entrada
class Entrada():
    def __init__(self, valor, pesos):
        self.valor = int(valor)
        self.pesos = pesos

# Gera entradas aleatórias
def gerar_entradas(qtd_entradas, qtd_pesos):
    entradas = []
    for _ in range(qtd_entradas):
        entradaNova = Entrada(random.randint(0, 9), gerar_pesos(qtd_pesos))
        entradas.append(entradaNova)
    return entradas

# Gera pesos aleatórios para cada entrada
def gerar_pesos(qtd_pesos):
    pesos = []
    for _ in range(qtd_pesos):
        pesos.append(round(random.random(), 2))
    return pesos

# Lista todas as entradas
def listar_entradas(entradas):
    for entrada in entradas:
        print(f'{entrada.valor} Entrada pesos: {entrada.pesos}')
    print('\n')

# Define o valor de ativação através do somatório do produto entre o peso e o valor de entrada mais a constante
def defini_ativacao(entradas, peso_id):
    constante = 0
    somatorio_final = 0
    for entrada in entradas:
        somatorio_final += (entrada.valor * entrada.pesos[peso_id]) + constante
    return round(somatorio_final,2)

# Defini o valor de ativação para cada neurônio
# para nosso algoritmo a quantidade de neuronios é equivalente a quantidade de pesos
def definir_neuronios(qtd_neuronios, entradas):
    neuronioAtivacao = []
    i = 0
    for _ in range(qtd_neuronios):
        neuronioAtivacao.append(defini_ativacao(entradas, i))
        i += 1
    return neuronioAtivacao

# Define os custos
def definir_custos(neuronio_obtido, ideal):
    i = 0
    custos_finais = []
    for _ in neuronio_obtido:
        custo_final = round((neuronio_obtido[i]-ideal),2)
        i += 1
        custos_finais.append(custo_final)
    return custos_finais

# Lista os neuronios e os respectivos valores de ativação
def listar_neuronios(neuronios):
    i = 0
    for _ in neuronios:
        print(f'{i} ativação neuronio: {neuronios[i]}')
        i += 1
    print('\n')

# lista os custos
def listar_custos(custos):
    i = 0
    for _ in custos:
        print(f'{i} custo: {custos[i]}')
        i += 1
    print('\n')

# Ativa um neurônio caso o custo seja menor que 10
def ativar_neuronio(neuronios, custos):
    i = 0
    for _ in neuronios:
        if custos[i] < 10:
            print(f'{i} Neuronio Ativado Valor: {neuronios[i]} Custo:{custos[i]}')
        i += 1
    print('\n')

print('\n============== Início ==============\n')

# atributos fixos para entradas e pesos
qtd_pesos = 5
qtd_entradas = 5

entradaArr = gerar_entradas(qtd_entradas, qtd_pesos)

listar_entradas(entradaArr)

neuronios = definir_neuronios(qtd_pesos, entradaArr)

listar_neuronios(neuronios)

custos = definir_custos(neuronios, 0.5)

listar_custos(custos)

ativar_neuronio(neuronios,custos)

print('\n============== Final ==============\n')