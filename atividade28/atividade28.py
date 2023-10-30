# Exercício Python 28 : Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.


maiores_idade = 0
menores_idade = 0
for i in range(1, 8):

    ano_nascimento = int(input(f"Digite o ano de nascimento da pessoa {i}: "))
    idade = 2023 - ano_nascimento
    
    if idade >= 18:
        maiores_idade += 1
    else:
        menores_idade += 1
print(f"Total de pessoas maiores de idade: {maiores_idade}")
print(f"Total de pessoas menores de idade: {menores_idade}")

