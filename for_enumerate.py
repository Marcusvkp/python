texto = """
O tempo é muito lento para os que esperam
Muito rápido para os que têm medo
Muito longo para os que lamentam
Muito curto para os que festejam
Mas, para os que amam, o tempo é eterno."""

for i, c in enumerate(texto):
    if c =='a' or c =='e':
    
        print(f"Vogal'{c}' encontrada, na posição {i}")
    
    else:
        continue