# Exercício Python 28 : Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime

maior_idade = []
menor_idade = []

hoje = datetime.datetime.now()
year = hoje.year

print("digite uma lista de anos de nascimento e saiba quais são maiores de idade")

for i in range(1,8):
    ano = int(input(f"digite o {i}° ano de nascimento:"))
    idade = year - ano
    if idade >= 18 :
        maior_idade.append(ano)
    else :
        menor_idade.append(ano)

print(f'''os maiores de idade são:{maior_idade}
os menores de idade são:{menor_idade}''')        