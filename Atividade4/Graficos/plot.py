import matplotlib.pyplot as plt
import numpy as np

# Função para calcular TimeoutInterval
def calculate_timeout_interval(estimated_rtt, dev_rtt):
    return estimated_rtt + 4 * dev_rtt

def plot_result(arquivo, algoritmo):
  # Leitura do arquivo de entrada
  file_path = arquivo  
  #data = np.genfromtxt(file_path, delimiter=' ', usecols=(0, 1, 2))

  # Listas para armazenar os dados
  col1 = []
  col2 = []
  col3 = []

  with open(file_path, 'r') as file:
      for line in file:
          # Dividindo os valores da linha e convertendo para ponto flutuante
          values = [float(value.replace(',', '.')) for value in line.split()]
          
          # Armazenando nas respectivas colunas
          col1.append(values[0])
          col2.append(values[1])
          col3.append(values[2])

  # Convertendo as listas para arrays numpy
  col1 = np.array(col1)
  col2 = np.array(col2)
  col3 = np.array(col3)

  # Parâmetros para o cálculo do TimeoutInterval
  a = 0.125
  b = 0.25

  # Inicialização das variáveis para o primeiro valor
  estimated_rtt = col2[0]
  dev_rtt = 0
  timeout_interval = calculate_timeout_interval(estimated_rtt, dev_rtt)

  # Plotagem das curvas
  plt.plot(col1, label='Custo')
  plt.plot(col2, label='RTT')
  plt.plot(col3, label='Total')

  # Adição de rótulos e legenda
  plt.title('Resultados do algoritmo: ' + algoritmo)
  plt.xlabel('Rounds')
  plt.ylabel('Tempo(ms)')
  plt.legend(loc='upper left', fontsize='small')

  # Exibição do gráfico
  plt.show()

  def plot_timeout(arquivo, algoritmo):
  # Leitura do arquivo de entrada
    file_path = arquivo  
    #data = np.genfromtxt(file_path, delimiter=' ', usecols=(0, 1, 2))

    # Listas para armazenar os dados
    col1 = []
    #col2 = []
    #col3 = []

    with open(file_path, 'r') as file:
        for line in file:
            # Dividindo os valores da linha e convertendo para ponto flutuante
            values = [float(value.replace(',', '.')) for value in line.split()]
            
            # Armazenando nas respectivas colunas
            col1.append(values[1])
            #col2.append(values[1])
            #col3.append(values[2])

    # Convertendo as listas para arrays numpy
    col1 = np.array(col1)
    #col2 = np.array(col2)
    #print(col2)
    #col3 = np.array(col3)
    #print(col3)

    # Parâmetros para o cálculo do TimeoutInterval
    a = 0.125
    b = 0.25

    # Inicialização das variáveis para o primeiro valor
    estimated_rtt = col1[0]
    col2 = [estimated_rtt]
    dev_rtt = 0
    col3 = [dev_rtt]
    timeout_interval = calculate_timeout_interval(estimated_rtt, dev_rtt)
    col4 = [timeout_interval]

    # Loop para calcular os valores da coluna 4
    for x in col1[1:]:
        estimated_rtt = (1 - a) * estimated_rtt + a * x
        col2.append(estimated_rtt)
        dev_rtt = (1 - b) * dev_rtt + b * abs(x - estimated_rtt)
        col3.append(dev_rtt)
        timeout_interval = calculate_timeout_interval(estimated_rtt, dev_rtt)
        col4.append(timeout_interval)

    # Plotagem das curvas
    plt.plot(col1, label='SampleRTT')
    plt.plot(col2, label='EstimatedRTT')
    plt.plot(col3, label='DevRTT')
    plt.plot(col4, label='TimeoutInterval', linestyle='dashed')

    # Adição de rótulos e legenda
    plt.title('Cálculo de Performance do Algoritmo: ' + algoritmo)
    plt.xlabel('Rounds')
    plt.ylabel('Tempo(ms)')
    plt.legend(loc='upper left', fontsize='small')

    # Exibição do gráfico
    plt.show()

plot_result('1.1.txt', 'Plista')
plot_timeout('1.1.txt', 'Plista')

plot_result('1.2.txt', 'Annealing')
plot_timeout('1.2.txt', 'Annealing')

plot_result('1.3.txt', 'AnnealingGA')
plot_timeout('1.3.txt', 'AnnealingGA')

plot_result('2.1.txt', 'plista')
plot_timeout('2.1.txt', 'plista')

plot_result('2.2.txt', 'Annealing')
plot_timeout('2.2.txt', 'Annealing')

plot_result('2.3.txt', 'AnnealingGA')
plot_timeout('2.3.txt', 'AnnealingGA')












