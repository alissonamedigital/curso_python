def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

titulo('Curso em vídeo')
titulo('Python')

def soma(a, b):
    s = a + b
    print(s)

soma(1, 2)


def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')

contador(1, 3, 4)
contador(1, 3, 4, 6, 7)
contador(9)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos+=1

valores = [7, 2, 5, 0, 4]
print(len(valores))
dobra(valores)
print(valores)
    