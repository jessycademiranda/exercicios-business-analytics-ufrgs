#Apresente uma função para calcular e retornar a amplitude térmica, dadas como argumentos a temperatura mínima
# e máxima. Apresente um pequeno programa no qual o usuário pode utilizar esta função.

# Função que calcula a amplitude térmica
def amplitude_termica(min_temp, max_temp):
    return max_temp - min_temp

# Programa principal
def main():
    # Solicita ao usuário as temperaturas
    min_temp = float(input("Digite a temperatura mínima (°C): "))
    max_temp = float(input("Digite a temperatura máxima (°C): "))

    # Calcula a amplitude térmica usando a função
    amplitude = amplitude_termica(min_temp, max_temp)

    # Exibe o resultado
    print(f"A amplitude térmica é: {amplitude:.2f}°C")

# Chama o programa principal
main()
