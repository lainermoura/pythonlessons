import math
ang = float(input('Digite um valor de ângulo: '))
rad = math.radians(ang)
seno = math.sin(rad)
coseno = math.cos(rad)
tang = math.tan(rad)
print(f'Se o ângulo for {round(ang, 2)}º \n o seno será {round(seno, 2)}° \n o coseno será {round(coseno, 2)}º \n e a tangente será {round(tang, 2)}º')
