# Exercício 1) O indice de Massa Corporal (IMC) é calculado dividindo-se o peso 
# de um individuo pelo quadrado de sua altura. Faça um programa que leia o peso e a altura
# de um individuo e informe seu IMC
peso = float(input('Entre com o seu peso: '))
altura = float(input('Entre com a sua altura: '))
IMC = (peso/(altura**2))
print("Peso:", peso)
print("Altura:", altura)
print(f"================ IMC ================\n{IMC:.2f}")