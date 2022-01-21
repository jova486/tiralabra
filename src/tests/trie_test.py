import unittest
from trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.arr_3 = [1,2,3]
        self.t = Trie()


    def test_empty_trie_returns_empty_list(self):

        self.assertAlmostEqual(self.t.query([6]), [])
        self.assertAlmostEqual(self.t.query([]), [])
        self.assertAlmostEqual(self.t.query([-1]), [])

    def test_trie_insert_tallentaa_listan_ja_sen_voi_hakea(self):

        self.t.insert(self.arr_3)
        self.assertAlmostEqual(self.t.query(self.arr_3), [([1,2,3],1)])

