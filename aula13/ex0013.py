from time import sleep

for c in range(0,7):
    print(c)

for c in range(6, 0, -1):
    print(c)
print('Fim')

inpt = int(input('Digite um número: '))
for num in range(0, inpt):
    print(num)
print('Fim')

i = int(input('Início: '))
p = int(input('Passo: '))
f = int(input('Fim: '))
for item in range(i, f+1, p):
    print(item)
print('FIM')

lista =  [1, 10, 40, 77, 99]
for count in lista:
    print(count)
print('BUMMM')

for c in range(10, -1, -1):
    print(c)
    sleep(0.5)
print('BUMMM')

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
    