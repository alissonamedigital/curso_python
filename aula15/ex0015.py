idade = trials = 0
while idade < 18:
    idade = int(input('Qual a sua idade?  '))
    print('Você não pode acessar nosso o site!')
    trials += 1
    if trials == 3:
        print(f'Você atingiu o limite de {trials:-^20} tentativas, tente mais tarde!')
        break

numero = int(input('Digite o número que deseja saber a tabuada? '))
tabuada = 1

while tabuada <= 10:
    if numero < 0:
        break
    print(f'{tabuada} X {numero} é igual a {tabuada * numero}')
    tabuada += 1
print('FIM!')      