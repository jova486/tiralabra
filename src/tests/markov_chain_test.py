"""
Created on Fri Jan 14 18:26:35 2022

@author: jovajova
"""
import unittest
from trie import Trie
from markov_chain import getNext
from markov_chain import doArray
from markov_chain import doArray_strict


def isSub(arr, sub):
    """Apumetodi joka testaa onko b a:n osajono
    """
    if sub == []:
        return True
    length_arr = len(arr)
    length_sub = len(sub)
    i = 0
    j = 0

    while (i < length_arr and j < length_sub):

        if (arr[i] == sub[j]):

            i += 1
            j += 1

            if (j == length_sub):
                return True

        else:
            i = i - j + 1
            j = 0

    return False


class Test_markov_chain(unittest.TestCase):
    """Markovin ketjujen tuottamiseen liittyviä testejä
    """

    def setUp(self):
        """Testien alustus
        """
        self.arr_3 = [1, 2, 3, 4, 5]
        self.trie = Trie()
        self.trie.insert_array(self.arr_3, 3)

        self.arr = [1, 5, 3, 2, 6, 7, 8, 3, 2, 1, 5, 4,
                    6, 5, 3, 4, 2, 5, 4, 6, 7, 6, 1, 3, 2, 4]
        self.trie2 = Trie()

    def test_get_next_returns_empty_list_when_wrong_input(self):
        """Väärällä syötteellä palautetaan tyhjä lista
        """
        out = getNext(self.trie, [2, 1])
        self.assertAlmostEqual([], out)
        out = getNext(self.trie, [6])
        self.assertAlmostEqual([], out)
        out = getNext(self.trie, [4, 5])
        self.assertAlmostEqual([], out)

    def test_get_next_returns_right(self):
        """get_next palautetaa oikean arvon
        """

        out = getNext(self.trie, [1, 2])
        self.assertAlmostEqual(3, out)
        out = getNext(self.trie, [2, 3])
        self.assertAlmostEqual(4, out)
        out = getNext(self.trie, [3, 4])
        self.assertAlmostEqual(5, out)

    def test_do_array_returns_zero_to_ten(self):
        """do_array rakentaa oikean pituiset listat 0-10 pituuksille
        """

        test_lenght = 2
        self.trie2.insert_array(self.arr, test_lenght + 1)
        for lenght in range(10):
            self.assertAlmostEqual(
                len(doArray(self.trie2, test_lenght, lenght)), lenght)

    def test_do_array_returns_all_asked(self):
        """do_array rakentaa oikean pituisen listan pituudelle 100
        """

        test_lenght = 2
        self.trie2.insert_array(self.arr, test_lenght + 1)
        self.assertAlmostEqual(len(doArray(self.trie2, test_lenght, 100)), 100)

    def test_do_array_strict_all_can_be_found(self):
        """Kaikki sekvenssit löytyvät alkuperäisestä sekvenssistä
        """
        arr = [1, 5, 3, 2, 6, 7, 8, 3, 2, 1, 5, 4,
               6, 5, 3, 4, 2, 5, 4, 6, 7, 6, 1, 3, 2, 4]
        trie_test = Trie()
        test_lenght = 2
        trie_test.insert_array(arr, test_lenght + 1)
        for _ in range(100):
            ret = doArray_strict(trie_test, test_lenght, 10)
            for j in range(len(ret) - test_lenght):
                self.assertTrue(isSub(arr, ret[j:(j + test_lenght)]))
