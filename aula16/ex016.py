lanche = ('Suco', 'HotDog', 'Pizza', 'Pudim')
print(lanche[2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(lanche[cont])

print(len(lanche))

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche))

a = (2, 4, 6, 8)
print(a.count(4))
print(a.index(8))

pessoa = ('Jose', '39', 99.99, 1990)
del(pessoa)
