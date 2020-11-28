# ANÁLISE E MANIPULAÇÃO DE STRING

frase = 'Curso em Vídeo Python'
# count()
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))

# len()
print(len(frase))

# True ou False utilizando "in"
print('Curso' in frase)

# find()
print(frase.find('Python'))
print(frase.find('python'))

frase = ' Curso em Vídeo Python  '
print(len(frase))

# strip()
print(len(frase.strip()))

frase = 'Curso em Vídeo Python'

# replace()
# No string no seus micros elementos ela é imutáveis. A não ser que utilize
# uma função de transformação de string e faça a atribuição.
print(frase.replace('Python', 'Android'))