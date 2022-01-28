import unittest
from trie import Trie
from markov_chain import getNext, doArray


class Test_markov_chain(unittest.TestCase):
    def setUp(self):
        self.arr_3 = [1, 2, 3]
        self.t = Trie()
        self.t.insert_array(self.arr_3,3)

    def test_getNext_returns_empty_list(self):
        out = getNext(self.t,[6])
        self.assertAlmostEqual([], out)


    def test_getNext_returns_right(self):

        out = getNext(self.t,[1,2])
        self.assertAlmostEqual(3, out)

    def test_doArray_returns_something(self):

        arr = [[1],[2],[3]]
        self.assertTrue(doArray(self.t, 2, 1) in arr)
    def test_doArray_returns_something_ELSE(self):

        arr = [1,2,3]
        ret = doArray(self.t, 1, 10)
        for i in ret:
            self.assertTrue((i in arr))
