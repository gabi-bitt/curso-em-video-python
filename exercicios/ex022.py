# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1- o nome com todas as letras maiúsculas
# 2- o nome com todas minúsculas
# 3- quantas letras ao todo(sem conseiderar espeços)
# 4- quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome: ')).strip()
print(f'Nome em maiúsculas: {nome.upper()}')
print(f'Nome em minúsculas: {nome.lower()}')
print(f'O seu nome tem {len(nome) - nome.count(' ')} letras')
separa = nome.split()
print(f'O seu primeiro nome tem {len(separa[0])} letras')