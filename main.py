# nome = input('Digite seu nome: ')
# idade = int(input('Digite sua idade: '))

# int('20') -> 20

# print('Seu nome é', nome)
# print('O dobro da sua idade é:', idade / 2)

# primeiro elemento: 0
# ultimo elemento: -1
# acessar um elemento: lista[indice]
# lista = [20, 18, 80]
# print(lista)
# indice = int(input('Digite o indice da lista: '))
# print(lista[indice])

#tamanho da lista len(lista)
# print(len(lista))
# lista.sort()
# print(lista)


# metodo append() adiciona um novo elemento à lista
# lista.append(elemento)

#lista.append(200)
# print(lista)


# pedir a idade do usuário e adicionar à lista
# no fim, imprimir a lista ordenada

# idade = int(input('Digite sua idade: '))
# lista.append(idade)
# lista.sort()
# print(lista)
# lista.reverse()
# print(lista)
# lista.pop(0)
# print(lista)

# dicionario é um conjunto {chave: valor, chave1: valor1}
# para criar um dicionario: dicionario = {'nome': 'bruno'}
#dicionario = {'nome': 'bruno'}
# para adicionar novos pares chave valor:
#dicionario['idade'] = 22
# print(dicionario)
#para acessar elementos de um dicionário:
# print(dicionario['nome'] + str(dicionario['idade']))
# nome = dicionario['nome']
# idade = dicionario["idade"]
# print(f'Seu nome eh {nome} e sua idade eh {idade}')

#idades = [10, 30, 20]
#quantidade = int(input('Digite a quantidade de idades: '))

#for i in range(quantidade):
#    idade = int(input(f'Digite a {i+1}a idade: '))
#    idades.append(idade)

#print(idades)

## peçam a altura e o nome de x usuários (x vai ser informado pelo usuário) e adicione em duas listas distintas
# uma lista altura que contém números decimais
# uma lista de nome que só contém strings
# no fim, imprima as duas listas

# alturas = []
# nomes = []

# quantidade = int(input('Digite a quantidade de alturas e nomes: '))

# for i in range(quantidade):
#     nome = (input(f'Digite o {i+1}o nome: '))
#     nomes.append(nome)
# for i in range(quantidade):
#     altura = float(input(f'Digite a {i+1}a altura: '))
#     alturas.append(altura)

# print(alturas)
# print(nomes)

# condicional

# if (1 <= 0): # falso
#     print('verdadeiro') 
# elif (2 != 2): # falso
#     print('2 é igual a 2')
# elif (3 > 3): # falso
#     print('3 maior q 2')
# else:
#     print('falso')


## peça a idade do usuário e se o usuário for maior de idade imprima 'liberado'
# caso contrário, imprima 'não autorizado'
    
# idade = int(input('Digite sua idade: '))

# if (idade >= 18):
#     print('liberado')
# else:
#     print('não autorizado')

# def funcao(idade):
#     if (idade >= 18):
#         print('liberado')
#     else:
#         print('não autorizado')


# def dobro_idade(idade):
#     idade = idade * 2
#     return idade

# idade = int(input('digite sua idade: ')) # 20
# dobro_da_idade = dobro_idade(idade) # -> 40

# print(dobro_da_idade)

# idade = 20

# def imprimir_idade():
#     print(idade)

# imprimir_idade()


# def verifica_liberacao(nome, idade):
#     return nome == 'joao' and idade >= 18
    
# usuario_liberado = verifica_liberacao('joao', 19)

# if (usuario_liberado): 
#     print('pode passar')
# else:
#     print('n pode passar')

# crie uma funcao que peca o nome e o sobrenome de uma pessoa e imprima seu nome junto com o sobrenome

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

def nomeCompleto(nome, sobrenome):
    print(nome + ' ' + sobrenome)
    return nome, sobrenome

nomeCompleto(nome, sobrenome)



    