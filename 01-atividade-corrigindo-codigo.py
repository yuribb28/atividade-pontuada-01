# Solicitando a entrada dos números e armazenando em uma lista
numeros = [int(input(f"Digite o {i}º número: ")) for i in range(1, 6)]

# Inicializando variáveis para estatísticas
quantidade_pares = quantidade_impares = quantidade_positivos = quantidade_negativos = 0
soma_pares = soma_impares = soma_geral = 0
maior_numero = menor_numero = numeros[0]

# Processando os números
for numero in numeros:
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1
        soma_impares += numero
    
    if numero > 0:
        quantidade_positivos += 1
    elif numero < 0:
        quantidade_negativos += 1
    
    soma_geral += numero
    maior_numero = max(maior_numero, numero)
    menor_numero = min(menor_numero, numero)

# Calculando as médias
media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0
media_impares = soma_impares / quantidade_impares if quantidade_impares > 0 else 0
media_geral = soma_geral / len(numeros)

# Exibindo os resultados
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos pares: {media_pares:.2f}")
print(f"Média dos ímpares: {media_impares:.2f}")
print(f"Média geral: {media_geral:.2f}")
print(f"Números na ordem inversa: {numeros[::-1]}")
