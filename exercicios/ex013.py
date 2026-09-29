# Faça um algotimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário do funcionário: R$ '))
novo = salario + (salario * 15 / 100)
print(f'O funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${novo:.2f}')