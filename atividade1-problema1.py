# Você e seus amigos foram a um restaurante e querem dividir a conta. Neste restaurante há a opção de pagar os 10%
# do garçom. Crie um programa no qual o usuário informa o total da conta e quantas pessoas irão dividir esta conta,
# mostrando como resultado o total a ser pago com os 10% inclusos. Mostre também quanto cada pessoa pagaria ao
# dividir esta conta com ou sem os 10%

# Informar o total da conta
total_conta = int(input("Informe o total da conta: "))
# Quantas pessoas irao dividir a conta
qnt_pessoas = int(input("Quantas pessoas irão dividir a conta: "))

adicional = 10

total_conta_adicional = total_conta+(total_conta/100)*adicional
print("Total da conta com adicional de 10%: " + str(total_conta_adicional))

total_pessoa = (total_conta/qnt_pessoas)
print("Total por pessoa sem adicional de 10%: " + str(total_pessoa))

total_pessoa_adicional = (total_conta_adicional/qnt_pessoas)
print("Total por pessoa com adicional de 10%: " + str(total_pessoa_adicional))
