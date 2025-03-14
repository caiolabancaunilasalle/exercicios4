
lista = input("Digite números inteiros separados por espaço: ")


numeros = [int(num) for num in lista.split()]


maior = max(numeros)
menor = min(numeros)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
