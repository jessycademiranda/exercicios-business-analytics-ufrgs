# A população do país 𝑎 é 𝑝𝑎 no ano 𝑥, enquanto que a população do país 𝑏 é 𝑝𝑏 neste mesmo ano.
# A população do país a cresce a uma taxa 𝑡𝑎 , enquanto que a população do país 𝑏 cresce a uma taxa 𝑡𝑏 anualmente.
# Em qual ano a população do país 𝑏 será maior que a população do país 𝑎?
# Implemente um módulo chamado demografia que conterá o procedimento simular, o qual receberá como
# parâmetros os dados de entrada do problema descrito, exibindo na tela o resultado da simulação ano a ano, bem
# como o resultado final. Caso seja impossível a possível do país 𝑏 superar a do país 𝑎, mostre mensagem ao usuário

# Módulo: demografia

def simular(pa, pb, ta, tb, ano_inicial):
    ano = ano_inicial
    max_anos = 1000  # limite para evitar laço infinito

    print("\nSimulação da evolução populacional:")
    print(f"Ano {ano}: País A = {pa:.0f}, País B = {pb:.0f}")

    for _ in range(max_anos):
        if pb > pa:
            print(f"\n>> A população do país B superou a do país A no ano {ano}.")
            return

        # Atualiza populações com base nas taxas de crescimento
        pa *= (1 + ta / 100)
        pb *= (1 + tb / 100)
        ano += 1

        print(f"Ano {ano}: País A = {pa:.0f}, País B = {pb:.0f}")

    print("\n>> A população do país B não superará a do país A com as taxas atuais.")
