def calcular_valor(valor_prod, qtde, moeda="dolar", desconto=None, acrescimo=None):
    # Calcula o valor bruto multiplicando o valor do produto pela quantidade
    v_bruto = valor_prod * qtde
    
    # Verifica se há desconto
    if desconto:
        # Se houver desconto, calcula o valor líquido subtraindo o desconto do valor bruto
        v_liquido = v_bruto - (v_bruto * (desconto / 100))
    # Verifica se há acréscimo
    elif acrescimo:
        # Se houver acréscimo, calcula o valor líquido somando o acréscimo ao valor bruto
        v_liquido = v_bruto + (v_bruto * (acrescimo / 100))
    else:
        # Se não houver desconto nem acréscimo, o valor líquido é igual ao valor bruto
        v_liquido = v_bruto
    
    # Converte o valor líquido para a moeda especificada
    if moeda == 'real':
        # Se a moeda for 'real', retorna o valor líquido sem conversão
        return v_liquido
    elif moeda == 'dolar':
        # Se a moeda for 'dolar', converte o valor líquido para dólares usando uma taxa de câmbio de 5
        return v_liquido * 5
    elif moeda =='euro':
        # Se a moeda for 'euro', converte o valor líquido para euros usando uma taxa de câmbio de 5.7
        return v_liquido * 5.7
    else:
        # Se a moeda não estiver cadastrada, exibe uma mensagem de erro
        print("Moeda não cadastrada!")

# Exemplo de uso da função calcular_valor
valor_a_pagar = calcular_valor(valor_prod=50, qtde=5, desconto=5)

# Imprime o valor final da conta
print(f"O valor final da conta é {valor_a_pagar}")
