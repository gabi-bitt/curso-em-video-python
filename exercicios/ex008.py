# Escreva um programa que leia um valor em metros e o exiba convertido em centímetro e milímetros.

d = float(input('Digite uma distância em metros: '))
cm = d * 100
mm = d * 1000
print(f'Essa distância convertida para centímetros é: {cm}cm \nE em milímetros é: {mm}mm')
