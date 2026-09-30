# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import floor

num = float(input('Digite um número real qualquer: '))
print(f'O número {num} tem a parte inteira {floor(num)}')