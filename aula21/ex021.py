help()
help(print)
print(input.__doc__)

DocString

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem Retorno!
    Função criada por Alisson
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim!')

contador(2, 10, 10)


Parâmetro opcional

def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma é valor de {s}')

somar(1, 2)

somar(a=5, b=9)


def escopo_variavel(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
escopo_variavel(a)
print(f'A fora vale {a}')

Return

def somar_return(a=0, b=0, c=0):
    s = a + b + c
    return s

resp = somar_return(1, 2)
print(f'Rsultado {resp}')

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
        return f

fatorial(10)

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')

Exericício 101


def calcular_idade_para_voto(idade):
    from datetime import date
    res = date.today().year - idade
    if res < 16:
        return f'Você não vota com {res} anos de idade'
    elif res < 18 or res >= 65:
        return f'Voto compulsório com {res} anos de idade'
    else:
        return f'Voto obrigatório com {res} anos de idade'

idade =  int(input('Em que ano você naceu? '))
print(calcular_idade_para_voto(idade))


Exericício 102

def fatorial(n, show=False):
    """
    -> Calcula fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:  
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else: 
                print(' = ', end='')
        f *= c
        print(f'{c}')
    return f

print(fatorial(5, show=False))
help(fatorial)

Exericício 103


def ficha(nome='<Desconhecido>', gol=0):  
    print(f'O jogador {nome} fez {gol} gols no campeonato')

n = str(input(f'Nome do jogador: '))
g = str(input(f'Número de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)

Exericício 104

n = str(input(f'Digite um número: '))

def leia_int(v):
    if v.isnumeric():
        print(f'Você acabou  e digitar o número {n}')
    else:
        print('\033[0;31mERRO!: Isso não é um número\033[m')

leia_int(n)
