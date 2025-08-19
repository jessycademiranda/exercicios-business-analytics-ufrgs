# Calcule o IMC de um paciente e mostre na tela em qual faixa de classificação ele se encaixa:

# Solicita os dados do paciente
peso = int(input("Digite o peso (em kg): "))
altura = int(input("Digite a altura (em centrímetros): "))

# Calcula o IMC
imc = peso / ((altura/100) ** 2)

print(f"\nIMC calculado: {imc:.2f}")

# Tabela de classificação 
if imc < 18.5:
    classificacao = "Abaixo do peso (Magreza)"
elif imc <= 24.9:
    classificacao = "Peso Normal (Eutrófico)"
elif imc <= 29.9:
    classificacao = "Sobrepeso (Pré-obesidade)"
elif imc <= 34.9:
    classificacao = "Obesidade Grau I"
elif imc <= 39.9:
    classificacao = "Obesidade Grau II (Severa)"
else:
    classificacao = "Obesidade Grau III (Mórbida)"

print(f"Classificação: {classificacao}")
