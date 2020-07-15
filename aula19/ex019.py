from random import randint
from operator import itemgetter
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'Jose'
pessoas['peso'] = '90.5'
print(f'Seu nome é {pessoas["nome"]} e sua idade é {pessoas["idade"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for i in pessoas.items():
    print(i)

for k, v in pessoas.items():
    print(f'{k} : {v}')

del pessoas['sexo']
print(pessoas)


brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[1]['sigla'])

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.items():
        print(v)
aluno = {}
aluno['nome'] = str(input('Digite seu nome: '))
aluno['media'] = float(input('Digite sua média: '))
if aluno['media'] > 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
print(aluno)
for k, v in aluno.items():
    print(f' -{k} é igual a {v}')


jogadores = {}
for j in range(1, 5):
    n = randint(1, 6)
    jogadores[f'Jogador{j}'] = n
    print(f'Jogador{j} tirou {n} no dado')
print('-=' * 30)
print('Ranking')
ranking = []
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for j, n in ranking: 
    print(f'{j} com {n}.')
print(jogadores)

time = []
jogador = {}
while True:
    jogador['nome'] = str(input('Diigite o nome de um jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou esse ano?: '))
    jogador['gols'] = []

    for g in range(1, jogador['partidas'] + 1):
        jogador['gols'].append(int(input(f'Quantos gols você na partida {g}: ')))
    jogador['total'] = sum(jogador['gols'])

    print('-=' * 30)
    print(jogador)
    print('-=' * 30)
    print(f'O campo nome tem o valor {jogador["nome"]}')
    print(f'O campo gols tem o valor {jogador["gols"]}')
    print(f'O campo total tem o valor {jogador["total"]}')
    print('-=' * 30)
    print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
    for p, g in enumerate(jogador['gols']):
        print(f'  => Na partida {p}, fez {g} gols.')