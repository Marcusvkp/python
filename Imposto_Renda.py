# Inicializa a variável salario com o valor 0
salario = 0

# Solicita ao usuário que digite o salário do colaborador e converte para float
salario = float(input("Digite o salário do colaborador: "))

# Verifica o valor do salário e determina o imposto devido
if salario <= 1903.98:
    # Se o salário for menor ou igual a 1903.98, o colaborador é isento de imposto
    print(f"O colaborador é isento de imposto.")
    
elif salario <= 2826.65:
    # Se o salário estiver entre 1903.99 e 2826.65, o imposto é de R$ 142,80
    print(f"O colaborador deve pagar R$ 142,80 de imposto.")
    
elif salario <= 3751.05:
    # Se o salário estiver entre 2826.66 e 3751.05, o imposto é de R$ 354,80
    print(f"O colaborador deve pagar R$ 354,80 de imposto.")
    
elif salario <= 4664.68:
    # Se o salário estiver entre 3751.06 e 4664.68, o imposto é de R$ 636,13
    print(f"O colaborador deve pagar R$ 636,13 de imposto.")
    
else:
    # Se o salário for maior que 4664.68, o imposto é de R$ 869,36
    print(f"O colaborador deve pagar R$ 869,36 de imposto.")
