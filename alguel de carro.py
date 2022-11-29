dias = int(input('quantos dias de aluguel? ' ))
km = float(input('quantos km foram rodados? '))
por = dias * 60
quantidade = km * 0.15
valor = quantidade + por
print(' valor do seu aluguel com base no numero de dias {} e de km {} rodados é de {}'.format(dias, km, valor ))

#dias = int(input('quantos dias de aluguel? ' ))
#km = float(input('quantos km foram rodados? '))
#valor = (dias * 60) + (km * 0.15)
#print ( 'O total a pagar é de R${:.2f}'.format(valor))