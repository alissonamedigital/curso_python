try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__} :(')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito obrigado')

a
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipo de dados que você digitou.')
except (ZeroDivisionError):
    print('Não é possível dividir um número por zero!')
except (KeyboardInterrupt):
    print('Usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito obrigado')


def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não informar os dados!\033[m')
            return 0
        else:
            return n

def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não informar os dados!\033[m')
            return 0
        else:
            return n

num1 = leia_int('Digite um Inteiro: ')
num2 = leia_float('Digite um Real: ')
print(f'O valor Inteiro digitado foi {num1} e o Real digitado foi {num2}')

import urllib
import urllib.request


try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessível no momento')
else:
    print('Consegui acessar o site')



lista = './aula23/nome.txt'
nome = str(input('Digite seu nome: '))

file = open(lista, 'at')
file.write(f'{nome}\n')
file.close()


file = open(lista, 'wt+')
file.close()

file = open(lista, 'rt')
print(file.read())


file = open(lista, 'rt')
print(file.read())
file.close()
