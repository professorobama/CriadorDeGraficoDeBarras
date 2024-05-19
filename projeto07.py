#Criador de Gráfico de Barras:
#Implemente um programa que crie um gráfico de barras a partir de uma lista de valores fornecidos pelo usuário. Use um laço de repetição for para desenhar as barras.

import matplotlib.pyplot as plt

# Função para criar o gráfico de barras
def criar_grafico_barras(valores):
    # Obtém a quantidade de valores na lista
    quantidade_valores = len(valores)
    
    # Define a largura das barras
    largura_barra = 0.5
    
    # Define a posição de cada barra no eixo x
    posicoes_barras = range(1, quantidade_valores + 1)
    
    # Cria o gráfico de barras
    plt.bar(posicoes_barras, valores, width=largura_barra, color='blue')
    
    # Adiciona rótulos aos eixos
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    
    # Adiciona título ao gráfico
    plt.title('Gráfico de Barras')
    
    # Exibe o gráfico
    plt.show()

# Solicita ao usuário os valores para criar o gráfico de barras
valores = []
quantidade = int(input("Quantos valores deseja inserir? "))
for i in range(1, quantidade + 1):
    valor = float(input(f"Digite o valor {i}: "))
    valores.append(valor)

# Chama a função para criar o gráfico de barras com os valores fornecidos pelo usuário
criar_grafico_barras(valores)

#Este código utiliza a biblioteca matplotlib para criar um gráfico de barras a partir de uma lista de valores fornecidos pelo usuário. A função criar_grafico_barras(valores) recebe a lista de valores como entrada e cria o gráfico correspondente. O usuário pode especificar a quantidade de valores e inserir cada valor individualmente. Após inserir todos os valores desejados, o gráfico de barras será exibido na saída padrão.


'''Explicando o código:

1) Importação de Bibliotecas:
- O código começa importando a biblioteca matplotlib.pyplot com o alias plt. Essa biblioteca é utilizada para criar gráficos em Python.

2) Definição da Função criar_grafico_barras:
- A função criar_grafico_barras(valores) é definida para criar o gráfico de barras a partir dos valores fornecidos como entrada.
- A quantidade de valores é obtida utilizando len(valores).
- A largura das barras é definida como 0.5.
- As posições das barras no eixo x são definidas como uma sequência de números de 1 até a quantidade de valores na lista.
- O gráfico de barras é criado utilizando plt.bar() com as posições das barras e os valores fornecidos como entrada.
- Rótulos são adicionados aos eixos x e y com plt.xlabel() e plt.ylabel().
- Um título é adicionado ao gráfico com plt.title().
- O gráfico é exibido utilizando plt.show().

3) Solicitação dos Valores ao Usuário:
- O programa solicita ao usuário a quantidade de valores que deseja inserir.
- Utilizando um loop for, cada valor é solicitado individualmente ao usuário e adicionado à lista valores.

4) Chamada da Função criar_grafico_barras:
- Após inserir todos os valores desejados, a função criar_grafico_barras() é chamada com a lista de valores fornecida pelo usuário como entrada.
- Isso resulta na criação e exibição do gráfico de barras com base nos valores inseridos.

Em resumo, o código solicita ao usuário uma quantidade de valores e, em seguida, solicita cada valor individualmente. Depois de receber todos os valores, cria um gráfico de barras utilizando a biblioteca matplotlib e exibe-o na saída padrão.'''


