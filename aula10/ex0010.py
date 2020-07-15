nome = str(input('Qual é seu nome? '))
if nome == 'Fulano':
    print('Que belo nome!')
else:
    print('Que nome feio!')

print('Bom dia!')


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)
print('A sua média foi {:.1f}'.format(m))
if m > 6.0:
    print('Sua média foi ótima! Parabéns!')
elif m <= 6.0:
    print('Sua média foi regular! Da para melhorar!')
else:
    print('Sua média foi ruim! Estude Mais!')
