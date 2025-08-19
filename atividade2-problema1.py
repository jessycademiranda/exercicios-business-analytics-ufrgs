# Mostre todos os múltiplos de 23 entre 0 e 𝑚, sendo 𝑚 um valor inteiro qualquer informado pelo usuário.

m = int(input("Informe um número inteiro: "))

print(f"\nMúltiplos de 23 entre 0 e {m}:")

# Percorre os números de 0 até m (inclusive), com passo de 23
for i in range(0, m + 1, 23):
    print(i)