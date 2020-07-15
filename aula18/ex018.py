from random import randint
# teste = ['José', 30]
# galera = []
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 50
# galera.append(teste[:])
# print(galera)

# galera = [['Maria', 20], ['Pedro', 13], ['Lucas', 24], ['Carla', 27]]
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')

# galera.clear()
# print(galera)

# for item in range:
    

# nome = []
# peso = []

# while True:
#     nome.append(str(input('Nome: ')))
#     peso.append(float(input('Peso: ')))
#     c = str(input('Quer continuar? [S/N]' ))
#     if c in 'nN':
#         break
#     print('=-' * 30)
#     print(f'Ao todo você cadastro {len(nome)} pessoas')

# print(f'{nome} e {peso}')

# numeros = []
# impares = []
# pares = []

# numeros.append(impares)
# numeros.append(pares)


# for c in range(1, 8):
#     v = int(input(f'Digite o {c}o. valor: '))
#     if v % 2 == 0:
#         numeros[1].append(v)
#     else:
#         numeros[0].append(v)
# print('=-' * 30)
# print(f'Os valores pares digitados foram: {numeros[1]}')
# print(f'Os valores impares digitados foram: {numeros[0]}')

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}: '))
# print('-=' * 30)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#     print()



# lista = []
# quantidade = int(input(f'Quantos jogos você quer que eu sorteie?:  '))
# for c in range(0, 6):
#     for x in range(1, 61):
#         lista.append(x)
        
# print(lista)


lista = []

quantidade = int(input(f'Quantos jogos você quer que eu sorteie?:  '))

for i in range(1, quantidade + 1):
    for num in range(0, 6):
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
        elif num+1 < 60 not in lista:
            lista.append(num+1)
            print(num)
        elif num-1 > 1 not in lista:
            lista.append(num-1)
            print(num)
        else:
            print('Erro ao gerar números. Tente novamente!')
        lista.sort()

    print(f'Jogo {i}: {lista}')
    lista.clear()