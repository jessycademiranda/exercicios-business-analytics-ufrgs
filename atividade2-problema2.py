# Calcule o produto de 𝑛 números informados pelo usuário.

n = int(input("Quantos números você deseja multiplicar? "))

produto = 1  # Inicializa o produto como 1

# Loop para ler os n números e multiplicá-los
for i in range(n):
    num = float(input(f"Digite o {i+1}º número: "))
    produto *= num  # Multiplica o número atual ao produto acumulado

print(f"\nO produto dos {n} números é: {produto}")
