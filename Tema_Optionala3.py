# 1. Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.
# - Declara o lista cu 5 jucatori: lista_jucatori_teren
# - Declara o lista cu 5 jucatori de rezerva: lista_jucatori_rezerva
# - Declara o lista goala cu jucatori scosi din teren: lista_jucatori_scosi
# - Schimbari_efectuate = joaca-te cu valori diferite ca sa vezi cum trec datele prin cod
# - SCHIMBARI_MAX va fi o constanta cu valoarea 3
# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie atunci:
# - Efectuam schimbarea daca jucatorul e in lista de rezerve si nu exista in jucatorii de pe
# teren
# - Stergem jucatorul scos din lista de teren si il adaugam in lista de jucatori scosi
# - Adaugam jucatorul intrat in lista de jucatori de pe teren si il scoatem din lista de jucatori
# de rezerva
# - Afisam pe ecran: a intrat x, a iesit y. Mai aveti z schimbari (inlocuiti x, y si z cu numele
# variabilelor voastre)
# Daca jucatorul pe care vrem sa il schimbam nu e in teren:
# - Afisati ‘nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# Altfel, afisati ecran: ‘mai aveti z schimbari’
# Google search hint: “how to check if item is in list python”

lista_jucatori_teren = ['Ion', 'Hagi', 'Giga', 'Maradonna', 'Leu']
lista_jucatori_rezerva = ['Ana', 'Oana', 'Ilinca', 'Elena', 'Andreea']
lista_jucatori_scosi = []
schimbari_max = 3

schimbari_efectuate =

lista_jucatori_teren[0], lista_jucatori_rezerva[1] = lista_jucatori_rezerva[1], lista_jucatori_teren[0]
print(lista_jucatori_teren)
print(lista_jucatori_rezerva)

schimbari_efectuate = schimbari_efectuate + 1

lista_jucatori_scosi.append(lista_jucatori_rezerva[0])
del lista_jucatori_rezerva[0]

print(lista_jucatori_rezerva)
print(lista_jucatori_scosi)
jucator = input('Ce jucator alegi? ')
print(lista_jucatori_teren)

print(schimbari_efectuate)

if jucator not in lista_jucatori_scosi:
    print(f'{jucator} inca este pe teren - ORI IN REZERVE OR JOACA DEJA')
    if jucator in lista_jucatori_teren:
        print(f'{jucator} deja joaca')
    else:
        schimbari_efectuate = schimbari_efectuate + 1
        lista_jucatori_teren.append(jucator)
        print(f'A intrat {jucator}')
        print(lista_jucatori_teren)
        jucator_out = input('Ce jucator iese: ')
        lista_jucatori_teren.remove(jucator_out)
        print(f'A iesit {jucator_out}')
        print(lista_jucatori_teren)

else:
    print('Nu mai aveti schimbari')
