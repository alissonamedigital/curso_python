lanche = ['Pizza', 'Hotdog', 'Picole', 'Biscoito']
lanche.append('Pudim')
print(lanche)
lanche.insert(0,'Chocolate')
print(lanche)
lanche.pop(3)
print(lanche)
lanche.remove('Hotdog')
print(lanche)

if 'Pizza' in lanche:
    lanche.remove('Pizza')

print(lanche)

valores = list(range(4,11))
print(valores)
valores.sort(reverse=True)
print(valores)
print(len(valores))

numeros = [2, 5, 9, 1]
numeros[2] = 3
print(numeros)
numeros.sort()
print(numeros)
numeros.insert(0, 33)
print(numeros)
if 40 in numeros:
    numeros.remove(40)
else:
    print('Número não encontrado na lista!')

novos_valores = []
novos_valores.append(5)
novos_valores.append(9)
novos_valores.append(1)
for n in novos_valores:
    print(f'{n}...', end='')

v = []
for cont in range(0, 5):
    v.append(int(input('Digite um valor: ')))

for c, a in enumerate(v):
    print(f'Na posição {c} encontrei o valor {a}!')
print('FIM!')

a = [2, 5, 7, 0]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

l = []
for n in range(0, 5):
    l.append(int(input(f'Digite um valor para a posição {n}: ')))

print('=-' * 30)
print(f'Você digitou os valores {l}')
print(f'O maior número dessa lista é {max(l)}')
print(f'O maior número dessa lista é {min(l)}')
print(f'O total de números ness lista é {len(l)}')

lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado a lista!')
    else:
        print('Valor Duplicado! Digite outro número!')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break

print('-=' * 30)
lista.sort()
print(f'Você digitou os valores {lista}')

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')