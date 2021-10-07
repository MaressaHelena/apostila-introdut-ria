# Escreva um programa em Python que leia dois pares ordenados do plano cartesiano (x, y) e imprima:
# - a distância entre esses dois pontos;
# - o coeficiente angular da reta que passa por ambos os pontos;
# - o coeficiente linear da reta que passa por ambos os pontos.


x1 = float(input("Entre com x no primeiro ponto: "))
y1 = float(input("Entre com y no primeiro ponto: "))
x2 = float(input("Entre com x no segundo ponto: "))
y2 = float(input("Ente com y no segundo ponto: "))

# Sendo (x1,y1) e (x2,y2)
# irei isolar a varial cl; coeficiente linear
# partindo da ideia de que  y2=ca*x2+cl

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
coeficiente_angular = (y2 - y1)/(x2 - x1)
coeficiente_linear = (y2 - (coeficiente_angular * x2))

print(f"Distância entre os pontos = {distancia:.2f}")
print(f"Coeficiente Angular = {coeficiente_angular:.2f}")
print(f"Coeficiente Linear = {coeficiente_linear:.2f}")

