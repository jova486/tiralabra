import random


"""File jonka sisältää metodeja markovin ketjujen toteuttamiseen
"""


def getNext(t, s):
    """Hakee markovin ketjuun seuraavan
    Args:
        t: Trie luokka jossa sekvenssit tallennettu
        s: taulukko jossa edeltävät
    """

    arr = t.query(s)
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


def doArray(trie, l, r):
    sq = []
    for j in range(0, l):
        sq.append(getNext(trie, sq))
    out = []
    for i in range(0, r):
        c = getNext(trie, sq)

        if c == []:
            for j in range(0, (len(sq)+1)):
                c = getNext(trie, sq[:-j])
                if c != []:
                    break
        out.append(c)
        sq.append(c)
        sq.pop(0)

    return out


def doArray_strict(trie, l, r):
    sq = []
    out = []
    for j in range(0, l):
        sq.append(getNext(trie, sq))

    for i in range(0, r):
        c = getNext(trie, sq)

        if c == []:
            return out
        out.append(c)
        sq.append(c)
        sq.pop(0)

    return out
