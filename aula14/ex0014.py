n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números impares!'.format(par, impar))


n1 = int(input('Digite um número?'))
n2 = int(input('Digite outro número?'))


print(''' Escolha uma operação: 
[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir
''')
operacao = int(input())
if operacao == 1:
    print(n1 + n2)
elif operacao == 2:
    print(n1 - n2)
elif operacao == 3:
    print(n1 * n2)
elif operacao == 4:
    print(n1 / n2)
else:
    print('Número inválido')

 
timeout = 5
while timeout > 0:
    timeout -= 1
    print('Seu tempo está acabando restam {}'.format(timeout))