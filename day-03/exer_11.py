l = float(input('Digita a largura da parede: '))
a = float(input('Digita a altura da parede: '))
area = l * a
tinta = 2**2 
qtd_t = area / tinta
print('Quantidade de lata para pintar a parede {:.0f}'.format(qtd_t))