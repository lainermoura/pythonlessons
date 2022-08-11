from math import hypot
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
hip = hypot(co, ca)
print(f"O valor da hipotenusa equivale à {hip:.2f}")
