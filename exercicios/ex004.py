# Faça um programa que elaia algo pelo tecado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele 

x = input('Digite algo: ')
print(type(x))
print(x.isnumeric())
print(x.isalpha())
print(x.isalnum())
print(x.isdecimal())