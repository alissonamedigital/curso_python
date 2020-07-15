frase = 'Curso em Vídeo Python'
print(frase[13:])
print(frase[1:15:2])
print(frase[::2])

print(frase.count('o'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(len(frase))

frase = '  Curso em Vídeo Python    '
print(len(frase.strip()))

frase = 'Curso em Vídeo Python'
print(frase.replace('Python','Android'))

print('Curso' in frase)
print(frase.find('Vídeo'))

dividido = frase.split()
print(dividido[0])