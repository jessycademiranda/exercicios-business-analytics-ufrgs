# Um usuário de caixa eletrônico deseja sacar uma quantia inteira múltipla de 10, que pode ser distribuída em notas de
# R$ 100, R$ 50, R$ 20 e R$ 10. Pergunte ao usuário o valor a ser sacado e calcule quantas notas de cada valor deverão
# ser entregues de tal forma que o menor número de notas possível seja dispensado pela máquina.


# Valor a ser sacado
valor_saque = int(input("Informar o valor a ser sacado: "))

# Verificação do múltiplo de 10
if valor_saque % 10 != 0:
    print("Valor inválido. O valor deve ser múltiplo de 10.")
else:
    # Verifica as quantidades de notas
    notas_100 = valor_saque // 100
    valor_saque %= 100

    notas_50 = valor_saque // 50
    valor_saque %= 50

    notas_20 = valor_saque // 20
    valor_saque %= 20

    notas_10 = valor_saque // 10
    valor_saque %= 10

    print("Notas fornecidas:")
    if notas_100 > 0:
        print(f"{notas_100} nota(s) de R$ 100")
    if notas_50 > 0:
        print(f"{notas_50} nota(s) de R$ 50")
    if notas_20 > 0:
        print(f"{notas_20} nota(s) de R$ 20")
    if notas_10 > 0:
        print(f"{notas_10} nota(s) de R$ 10")


