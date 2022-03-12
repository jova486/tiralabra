"""
Created on Fri Jan 14 18:26:35 2022

@author: jovajova
"""
import unittest
import midi_io


class TestMidi(unittest.TestCase):
    """Midifilen avaamisen ja tallentamisen testeistä vastaava luokka
    """

    def test_get_file_info(self):
        """Testaa palauttaako get_file_info midifilen raitojen lukumäärän oikein
        """

        self.assertAlmostEqual(midi_io.get_file_info(
            "./data/testit/midi_io_test_out.mid"), 1)

    def test_opened_and_saved_file_equals(self):
        """testaa että from_midi_To_list ja arr_To_midifile toimivat oikein
        """
        out = midi_io.from_midi_to_list("./data/testit/midi_io_test_in.mid")
        midi_io.arr_to_midifile("./data/testit/midi_io_test_out.mid", out, 4, 2)
        self.assertAlmostEqual(midi_io.from_midi_to_list(
            "./data/testit/midi_io_test_out.mid"), out)
