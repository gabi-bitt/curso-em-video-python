# Faça um programa que leia algo pelo tecado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele 

x = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(x))
print('Só tem espaços? ', x.isspace())
print('É um valor númerico? ', x.isnumeric())
print('É um valor alfabético? ', x.isalpha())
print('É um valor alfanúmerico? ', x.isalnum())
print('Está em maiúsculas? ', x.isupper())
print('Está em minúsculas? ', x.islower())