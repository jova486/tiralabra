import unittest
import midiIO
class TestTrie(unittest.TestCase):

    def test_opened_and_saved_file_equals(self):
        out = midiIO.from_midi_To_list("./data/midi_io_test_in.mid")
        midiIO.arr_To_midifile("./data/midi_io_test_out.mid",out,4,2)
        self.assertAlmostEqual(midiIO.from_midi_To_list("./data/midi_io_test_out.mid"), out)