import random


"""File jonka sisältää metodeja markovin ketjujen toteuttamiseen
"""


def getNext(t,s):
    """Hakee markovin ketjuun seuraavan
    Args:
        t: Trie luokka jossa sekvenssit tallennettu
        s: taulukko jossa edeltävät
    """

    arr = t.query(s)
    sum = 0
    for i in arr:
        sum +=i[1]

    prob = []
    temp = 0
    for i in arr:
        temp += i[1]/sum
        prob.append((i[0],temp))


    rand = random.random()

    out = []
    for i in prob:
        if i[1]>rand:
            out = i[0][-1]
            break
    return out

def doArray(self, s,out,t, r,sChoice):

        for i in range(0,r):
            a = [self.getNext(t,s)]

            if a == [[]]:

                a = [random.choice(sChoice)]
                print("eilöydy")
            out += a
            s = [s[1]]+a

        return out

def doArray2(self, s,out,t, r,sChoice, another):

        for i in range(0,r):
            a = [self.getNext(t,s)]

            if a == [[]]:

                a = [random.choice(sChoice)]
                out += a
                s = a+[another[i]]
                print("eilöydy 2")
            else:
                out += a
                s = a+[another[i]]

        return out
