def fatorial(numero):
    # Verifica se o número é 0 ou 1
    if numero == 0 or numero == 1:
        # Se for 0 ou 1, retorna 1 (pois 0! e 1! são 1)
        return 1
    else:
        # Se o número não for 0 ou 1, calcula o fatorial recursivamente
        # Multiplica o número pelo fatorial do número anterior
        return numero * fatorial(numero - 1)

# Solicita ao usuário um número para calcular o fatorial
x = int(input("Digite um número para o fatorial: "))

# Chama a função fatorial com o número fornecido e armazena o resultado
resultado = fatorial(x)

# Imprime o número fornecido e seu fatorial calculado
print("O fatorial de %d é %d" % (x, resultado))
