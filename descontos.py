dias = float(input('quantos dias de aluguel? ' ))
km = float(input('quantos km foram rodados? '))
           carro = dias * 60
           quantidade = km * 0.15
           valor = carro * quantidade
             print(' valor do seu aluguel com base no numero de dias {} e de km {} rodados é de {}'.format(dias, km, valor ))