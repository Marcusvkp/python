peso = float(input("Digite aqui seu peso (Kg): "))
altura = float(input("Digite aqui a sua altura (m):"))

imc = peso / (altura ** 2)
print("O seu IMC é de {:.1f}".format(imc))

if imc < 18.5:
    print("Você está ABAIXO DO PESO normal!")

elif 18.5 <= imc < 25:
    print("Você está na faixa de PESO Normal!")

elif 25 <= imc < 30:
    print("Você está em SOBREPESO!")

elif 30 <= imc < 40:
     print("Você está em OBESIDADE!")

else:
     print("Você está em OBESIDADE MÓRBIDA!")