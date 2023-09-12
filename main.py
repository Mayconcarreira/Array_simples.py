
#inicialização da lista

lista = [12, 10, 7, 5]
lista_animais = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

#inserir elemento macaco na lista na primeira posição
lista_animais[0]= 'macaco'
print(lista_animais)

tupla = (1, 10, 12, 14)
print(tupla[0])

"""Função para len para ler a quantidade de elementos na lista"""
print(len(lista_animais))

tupla_animal = tuple(lista_animais)

print(type(tupla_animal))
print(tupla_animal)

lista_numerica = list(tupla)
print(lista_numerica)

#print(lista_animais)

"""função para organizar a lista"""
lista.sort()
lista_animais.sort()

print(lista)
print(lista_animais)
lista_animais.reverse()
print(lista_animais)

"""Função para saber qual o elemento minimo da lista"""
print(min(lista_animais))

nova_lista = lista_animais * 3

 print(nova_lista)
 
 """Verifica se o lobo está na lista, se não tiver e diz que não está e adiciona lobo a lista"""
 if 'lobo' in lista_animais:
    print('Tem lobo')
else:
    print('Não tem lobo na lista. Será incluído')
    lista_animais.append('lobo')
    print(lista_animais)

lista_animais.pop()
print(lista_animais)
