# Escreva um programa que solicite ao usuário uma lista de números inteiros e
# calcule a soma de todos os elementos da lista.


numeros = input("Digite uma lista de números inteiros separados por espaço: ")


lista_numeros = list(map(int, numeros.split()))


soma = sum(lista_numeros)


print(f"A soma dos números da lista é: {soma}")
