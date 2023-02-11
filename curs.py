data_type = 'dictionar'
if data_type == 'lista':
    print('lista')
    # Liste
    # declaram si initializam o lista
    lista_1 = [1, 2, 3, 4, 5, 6]
    lista_2 = ['apple', 'mac', 'iphone', 'ipad', 'apple']
    lista_3 = [1, True, '_', False, 5.2]
     # extrgem primul si ultimul ele din lista

    print(lista_1[0], lista_1[-1])
    lista_1.reverse()
    print(lista_1)

    lista_1.sort()
    print(lista_1)

    # oridine alfabetica
    lista_2.sort()
    print(lista_2)

    # TODO sortati lista 2 dupa penultima litera din fiecare  [mac, ipad, apple, iphone]

    # lista_3.sort()
    # print(lista_3) # doar daca nu ar fi strig in lista

    print(lista_2.count('apple'))

    # TODO count cate el sunt intr-o lista mai multe decat o data, app_le(elimina spatiile, litera mare, _, un caracter special - sa fie vazut tot ca apple
    # TODO lista - celelalte metodo build in din liste

    print(sum(lista_1))

    x = ['a', 'b', 'c', 'd']
    y = x
    y[0] = 'E'
    print(x)
    y = x.copy()
    u = x[:]
    print(x, y, u)
    print(id(x), id(y), id(u))
    # if id(x) == id(u):
    #     print('sunt egale')
    # if id (x) == id(y):
    #     print('nu sunt egale')

    lista_matrice = [lista_1, lista_2, lista_3]
    print(lista_matrice)

    lista_mare = [lista_matrice, [0, 1, lista_1, ['a', 'b', 'c'], [lista_matrice]], {}, True]
    print(lista_mare)
    print(lista_mare[0])
    print(lista_mare[0][0])
    print(lista_mare[0][0][-1])

    # TODO extragem '_', de extras ultimul 6 si sa extragem 2 din mijloc es poate folosi si if si count
elif data_type == 'set':
    # SET
    print('SETURI')
    my_set = {2, 3, 4, 5 , 6, 7, 2, 3, 4, 5 , 6, 7}
    print(my_set)
    my_list = [1, 1, 1, 1]
    print(list(set(my_list)))
# primt my_set 0 va fi eroare pt ca nu sunt indexate in seturi
    print(list(set(my_list)))
    second_set = {1, 2, 3, 8, 20, 5, 7}
    print(my_set.difference(second_set), my_set.intersection(second_set))

    # TODO ne jucam cu celelalte metode din seturi
elif data_type == 'tuple':
    print('TUPLE')
    tuple = (1, 2, 5, 7)
    print(tuple[0], tuple[-1])
    # TODO, de facut ce am facut si la liste

    print(tuple)
    print((type(tuple)))
    print((type([()])))

elif data_type == 'dictionar':
    print(dict)
    dictionar = {
        'user1': 'admin',
        'user2': 'Petre',
        'user3': {
            'name': 'John',
            'email': 'John@john.com',
            'is active': True
        }
    }
    print(dictionar['user2'], dictionar['user3']['email'])
    #TODO dispay John and his keys email only if his active status is true
    #TODO creaza un dictionar mai complex cu date primitive ptr key, ptr valori: lista de dictionare cu tuple, set, liste