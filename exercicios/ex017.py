# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math


co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))

hipotenusa = math.hypot(co, ca)

print(f"O comprimento da hipotenusa é: {hipotenusa}")