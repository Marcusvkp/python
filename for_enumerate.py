texto = """
O tempo é muito lento para os que esperam
Muito rápido para os que têm medo
Muito longo para os que lamentam
Muito curto para os que festejam
Mas, para os que amam, o tempo é eterno."""

# Iterando sobre cada caractere do texto junto com seu índice
for i, c in enumerate(texto):
    # Verificando se o caractere é 'a' ou 'e'
    if c == 'a' or c == 'e':
        # Imprimindo a vogal encontrada e sua posição
        print(f"Vogal '{c}' encontrada, na posição {i}")
    
    else:
        # Continuando para a próxima iteração do loop
        continue
