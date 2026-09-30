# faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input("Digite o ângulo: "))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"O seno de {angulo} é: {seno}")
print(f"O cosseno de {angulo} é: {cosseno}")
print(f"A tangente de {angulo} é: {tangente}")