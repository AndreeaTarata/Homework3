lista_1 = [1, 2, 3, 4, 5, 6]
lista_2 = ['Ap p le%', 'maC#', 'iph one!', 'ipad', 'ap ple']
lista_3 = [1, True, '_', False, 5.2]

# TODO sortati lista 2 dupa penultima litera din fiecare  [mac, ipad, apple, iphone]
lista_2.sort(key = lambda x: x[-2])
print(lista_2)

# TODO count cate el sunt intr-o lista mai multe decat o data, app_le(elimina spatiile, litera m
import re
lista_fara_spatii = [
    re.sub(r'[^a-zA-Z0-9]+', '', item) for item in lista_2
]
print(lista_fara_spatii)
lista_lit_mici = [x.lower() for x in lista_fara_spatii]
print(lista_lit_mici)

a_count = 0
for word in lista_lit_mici:
    for char in word:
        if char == 'a':
            a_count = a_count + 1

print (a_count)

# TODO extragem '_', de extras ultimul 6 si sa extragem 2 din mijloc es poate folosi si if si count

lista_2 = ['apple', 'mac', 'iphone', 'ipad', 'apple']
lista_matrice = [lista_1, lista_2, lista_3]
print(lista_matrice)
lista_mare = [lista_matrice, [0, 1, lista_1, ['a', 'b', 'c'], [lista_matrice]], {}, True]
print(lista_mare)
print(lista_mare[1])
print(lista_mare[1][2])
print(lista_mare[1][2][5])
print(lista_mare)
print(lista_mare[0])
print(lista_mare[0][-1])
print(lista_mare[0][-1][-3])
