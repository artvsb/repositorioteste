estoque_atual = int(input('Qual a quantidade atual em estoque do produto? \n'))
estoque_max = int(input('Qual a quantidade máxima em estoque do produto? \n'))
estoque_min = int(input('Qual a quantidade mínima em estoque do produto?'))
qtd_media = (estoque_max + estoque_min)/2
if estoque_atual < qtd_media: 
    print('Efetuar compra.')
else:
    print('Não efetuar compra.')