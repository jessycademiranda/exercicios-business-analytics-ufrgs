# Escreva uma expressão lógica/relacional que resulte em verdadeiro caso o usuário informe uma renda maior que R$
# 5.000,00 e que seu estado civil é “casado” ou então verdadeiro se sua renda for maior que R$ 3.500,00 e seu estado
# civil for “solteiro”

# Solicita a renda
renda = int(input("Digite sua renda: "))

# Solicita o estado civil
estado_civil = input("Digite seu estado civil (casado/solteiro): ").lower()

if (renda > 5000 and estado_civil == "casado") or (renda > 3500 and estado_civil == "solteiro"):
    print("verdadeiro")
else:
    print("falso")