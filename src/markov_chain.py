import random


"""File jonka sisältää metodeja markovin ketjujen toteuttamiseen
"""


def getNext(trie, array):
    """Hakee markovin ketjuun seuraavan
    Args:
        trie: Trie luokka jossa sekvenssit tallennettu
        arr: taulukko jossa edeltävät
    """

    arr = trie.query(array)
    sum = 0
    for i in arr:
        sum += i[1]

    prob = []
    temp = 0
    for i in arr:
        temp += i[1]/sum
        prob.append((i[0], temp))

    rand = random.random()

    out = []
    for i in prob:
        if i[1] > rand:
            out = i[0][-1]
            break
    return out


def doArray(trie, deg, lenght):
    """Tekee r pitoisen sekvenssin markovin l asteisen markovin ketjun avulla
    Args:
        trie: Trie luokka jossa sekvenssit tallennettu
        deg: markovin ketjun aste
        lenght: sekvenssin pituus
    """

    sq = []
    out = []
    while lenght > 0:
        next = getNext(trie, sq)
        if next != []:
            if len(sq)<deg:
                sq.append(next)
            else:
                out.append(next)
                sq.append(next)
                sq.pop(0)
                lenght -=1
        else:
            sq = []
    return out



def doArray_strict(trie, deg, lenght):
    """ testejä varten tehty metodi. Eroaa edellisestä siten että pysähtyy mikäli ei pääse
        eteenpäin halutulla syvyydellä.
        Tekee r pitoisen sekvenssin markovin l syvyisen markovin ketjun avulla
    Args:
        trie: Trie luokka jossa sekvenssit tallennettu
        deg: markovin ketjun aste
        lenght: sekvenssin pituus
    """
    sq = []
    out = []
    for j in range(0, deg):
        sq.append(getNext(trie, sq))

    for _ in range(0, lenght):
        next = getNext(trie, sq)

        if next == []:
            return out
        out.append(next)
        sq.append(next)
        sq.pop(0)

    return out
