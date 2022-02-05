import unittest
from trie import Trie
from markov_chain import getNext
from markov_chain import doArray
from markov_chain import doArray_strict


def isSub(a, b):
    if b == []:
        return True
    n = len(a)
    m = len(b)
    i = 0
    j = 0

    while (i < n and j < m):

        if (a[i] == b[j]):

            i += 1
            j += 1

            if (j == m):
                return True

        else:
            i = i - j + 1
            j = 0

    return False


class Test_markov_chain(unittest.TestCase):
    def setUp(self):
        self.arr_3 = [1, 2, 3, 4, 5]
        self.t = Trie()
        self.t.insert_array(self.arr_3, 3)

        self.arr = [1, 5, 3, 2, 6, 7, 8, 3, 2, 1, 5, 4,
                    6, 5, 3, 4, 2, 5, 4, 6, 7, 6, 1, 3, 2, 4]
        self.t2 = Trie()

    def test_getNext_returns_empty_list(self):
        out = getNext(self.t, [6])
        self.assertAlmostEqual([], out)

    def test_getNext_returns_right(self):

        out = getNext(self.t, [1, 2])
        self.assertAlmostEqual(3, out)

    def test_doArray_returns_all_asked(self):

        test_lenght = 2
        self.t2.insert_array(self.arr, test_lenght+1)
        self.assertAlmostEqual(len(doArray(self.t2, test_lenght, 100)), 100)

    def test_doArray_strict_all_can_be_found(self):

        arr = [1, 5, 3, 2, 6, 7, 8, 3, 2, 1, 5, 4,
               6, 5, 3, 4, 2, 5, 4, 6, 7, 6, 1, 3, 2, 4]
        t = Trie()
        test_lenght = 2
        t.insert_array(arr, test_lenght+1)
        for i in range(100):
            ret = doArray_strict(t, test_lenght, 10)
            for j in range(len(ret)-test_lenght):
                self.assertTrue(isSub(arr, ret[j:(j+test_lenght)]))
