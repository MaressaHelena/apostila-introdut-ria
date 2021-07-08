# Escreva um programa em Python que leia dois pares ordenados do plano cartesiano (x, y) e imprima:
# - a distância entre esses dois pontos;
# - o coeficiente angular da reta que passa por ambos os pontos;
# - o coeficiente linear da reta que passa por ambos os pontos.
# nesse exercício, os valores inseridos serão: 
# - x no primeiro ponto: 1; y no primeiro ponto: -4.5
# - x no segundo ponto: -2; y no segundo ponto: 10
#####################################################

x1 = 1
x2 = -2
y1 = -4.5
y2 = 10

# Sendo (x1,y1) e (x2,y2)
# irei isolar a varial cl; coeficiente linear
# partindo da ideia de que  y2=ca*x2+cl
d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
ca = (y2 - y1)/(x2 - x1)
cl = (y2 - (ca * x2))
print("Entre com x no primeiro ponto: ",x1)
print("Entre com x no segundo ponto: ",x2)
print("Entre com y no primeiro ponto: ",y1)
print("Entre com y no segundo ponto: ",y2)
print("Distância entre os pontos =",d)
print("Coeficiente angular =",ca)
print("Coeficiente linear =",cl)

