# Escreva uma função para ler do usuário os totais de cada um dos $n$ dias de vendas de uma loja. Retorne em qual
# dos dias se observou o maior total.

def dia_maior_venda(n):
    maior_total = -float('inf')
    dia_maior = -1

    for i in range(1, n + 1):
        total = float(input(f"Digite o total de vendas do dia {i}: "))
        if total > maior_total:
            maior_total = total
            dia_maior = i

    return dia_maior

# Programa principal
def main():
    n = int(input("Quantos dias de vendas você deseja informar? "))
    dia = dia_maior_venda(n)
    print(f"\nO maior total de vendas ocorreu no dia {dia}.")

# Chamada da função principal
main()
