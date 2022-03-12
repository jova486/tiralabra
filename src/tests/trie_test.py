"""
Created on Fri Jan 14 18:26:35 2022

@author: jovajova
"""
import unittest
from trie import Trie


class TestTrie(unittest.TestCase):
    """Trien testeistä vastaava luokka
    """
    def setUp(self):
        """Testien alustus
        """
        self.arr_3 = [1, 2, 3]
        self.trie = Trie()

    def test_default_parent_node_value_is_default(self):
        """Testaa onko tyhjän trien arvo -1
        """
        self.assertEqual(self.trie.root.note, -1)

    def test_default_end_value_is_false(self):
        """Testaa tyhjän trien loppu merkitty oikein
        """
        self.assertEqual(self.trie.root.end, False)

    def test_empty_trie_returns_empty_list(self):
        """Testaa että tyhjä trie palauttaa tyhjän listan
        """

        self.assertAlmostEqual(self.trie.query([6]), [])
        self.assertAlmostEqual(self.trie.query([]), [])
        self.assertAlmostEqual(self.trie.query([-1]), [])

    def test_trie_insert_store_sequence(self):
        """Testaa trie tallentaa ja palauttaa yhden listan oikein
        """
        self.trie.insert(self.arr_3)
        self.assertAlmostEqual(self.trie.query([1, 2]), [([1, 2, 3], 1)])

    def test_trie_insert_array_store_sequence_and_returns_right(self):
        """Testaa trie tallentaa listan oikein ja että haku toimii oikein
        """
        self.trie.insert_array(self.arr_3, 3)
        self.assertAlmostEqual(self.trie.query([1]), [([1, 2], 1)])
        self.assertAlmostEqual(self.trie.query([2]), [([2, 3], 1)])
        self.assertAlmostEqual(self.trie.query([1, 2]), [([1, 2, 3], 1)])
        self.assertAlmostEqual(self.trie.query([2, 3]), [])
        self.assertAlmostEqual(self.trie.query(
            []), [([1], 1), ([2], 1), ([3], 1)])
