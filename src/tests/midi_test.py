import unittest
import midiIO
class TestTrie(unittest.TestCase):

    def test_get_file_info(self):
        """Testaa palauttaako get_file_info midifilen raitojen lukumäärän oikein
        """

        self.assertAlmostEqual(midiIO.get_file_info("./data/testit/midi_io_test_out.mid"), 1)

    def test_opened_and_saved_file_equals(self):
        """testaa että from_midi_To_list ja arr_To_midifile toimivat oikein
        """
        out = midiIO.from_midi_To_list("./data/testit/midi_io_test_in.mid")
        midiIO.arr_To_midifile("./data/testit/midi_io_test_out.mid",out,4,2)
        self.assertAlmostEqual(midiIO.from_midi_To_list("./data/testit/midi_io_test_out.mid"), out)