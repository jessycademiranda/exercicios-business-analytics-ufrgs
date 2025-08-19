# Uma população de microrganismos dobra a cada dia. Porém, após dobrar, no mesmo dia, 12% destes
# microrganismos morrem.
# Dado que a população no dia 𝑑0 = 1343, qual será a população no dia 𝑑32? Mostre a evolução diária desta
# população.

# População inicial
populacao = 1343
dias = 32

print("Evolução da população de microrganismos:")
print(f"Dia 0: {populacao:.2f}")

# Loop pelos dias
for dia in range(1, dias + 1):
    populacao *= 1.76  # Dobra e 12% morrem
    print(f"Dia {dia}: {populacao:.2f}")

# Resultado final
print(f"\nPopulação final no dia {dias}: {populacao:.2f}")
