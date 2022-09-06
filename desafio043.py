peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

imc = peso / (altura * altura)

if imc < 18.50:
    print("Abaixo do peso!")
    print(f"IMC {imc:.2f}")
elif imc >= 18.50 and imc < 25:
    print("Peso ideal!")
    print(f"IMC {imc:.2f}")
elif imc >= 25 and imc < 30:
    print("Sobrepeso!")
    print(f"IMC {imc:.2f}")
elif imc >= 30 and imc < 40:
    print("Obesidade")
    print(f"IMC {imc:.2f}")
elif imc >= 40:
    print("Obesidade mórbida")
    print(f"IMC {imc:.2f}")
else:
    print("Confira as informações digitadas!")