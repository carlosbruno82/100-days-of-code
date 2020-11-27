#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e 
#raiz quadrada

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = pow(n, 1/2) #r = n ** 0.5 or r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d)) 
print('O triplo de {} vale {}. \nA raiz quadrada de {} vale {:.2f}'.format(n, t, n, r))
# ou
# print('O dobro de {} vale {}.'.format(n, (n*2))) 
# print('O triplo de {} vale {}. \nA raiz quadrada de {} vale {:.2f}'.format(n, (n*3), n, (n**(1/2))))
