"""
Created on Fri Jan 14 18:26:35 2022

@author: jovajova
"""
from trie import Trie
import midi_io
import markov_chain as mc


def make_harmony_table(arr):
    """Apumetodi joka rakentaa matriisin harmonioista jokaiselle tahtiosalle

        Args:
            arr: Taulukko jossa nuotrie_tenori ja rytmi arvot

        Returns:
            list: taulukko taulukko johon harmoniat tallennetaan
        """
    harmonies = []
    for k in range(0, len(arr)):
        temp = []
        for j in range(0, len(arr[k])):
            for i in range(0, arr[k][j][0]):
                temp.append(arr[k][j][1])
        harmonies.append(temp)
    return harmonies


def make_rythm_table(arr, rythms):
    """Apumetodi joka rakentaa matriisin rymeistä

        Args:
            arr: Taulukko jossa rytmi arvot

        Returns:
            list: taulukko taulukko johon rytmit tallennetaan
        """

    for k in range(0, len(arr)):
        for j in range(0, len(arr[k])):
            rythms[k].append(arr[k][j][0] * 2)
    return rythms


class Service:
    """Ohjelman toimintalogiikasta vastaava luokka
    """

    def __init__(self):
        """Luokan konstruktori.

        """
        self.use_original_rythm = False
        self.midifile_name_melody = ""
        self.midifile_name_melody_array = []
        self.midifile_name_rythm = ""
        self.out_file = []
        self.num_tracks = 0
        self.time_signature_numerator = 4
        self.time_signature_denominator = 2
        self.markov_depth = 2
        self.trie = Trie()

    def set_time_signature(self, text):
        """Asetrie_tenoraa tahtilajin.
        Args:
            text: tahtilaji merkkijonona
        """
        text_split = text.split("/")
        self.time_signature_numerator = int(text_split[0])
        denominator = int(text_split[1])
        if denominator == 4:
            self.time_signature_denominator = 2
        elif denominator == 8:
            self.time_signature_denominator = 3
        else:
            self.time_signature_denominator = 4

    def set_markov_depth(self, text):
        """Asetrie_tenoraa markovin ketjun asteen.
        Args:
            text: ketjun aste merkkijonona
        """

        self.markov_depth = int(text)
        self.trie = Trie()
        for file in self.midifile_name_melody_array:
            self.add_to_trie(file)

    def reset_trie(self):
        """Alustaa trien uudelleen

        """

        self.midifile_name_melody_array = []
        self.midifile_name_melody_array.append(self.midifile_name_melody)
        self.trie = Trie()
        for file in self.midifile_name_melody_array:
            self.add_to_trie(file)

    def add_to_trie(self, filename):
        """Lisää tiedoston sisällön trieeen
        Args:
            filename: ketjun lisätrie_tenorävän tiedoston nimi

        """

        data = midi_io.from_midi_to_list(filename)[0]

        melody = []
        for i in range(0, len(data)):
            melody.append(data[i][1])

        trie = self.trie
        trie.insert_array(melody, self.markov_depth + 1)

    def add_file_name(self, filename, text):
        """asetrie_tenoraa tallennetrie_tenoravan midi tiedoston nimen
        Args:
            filename: miditiedoston nimi
            text: melodia tai rytmi
        """
        if text == "melody":
            self.midifile_name_melody = filename
            self.midifile_name_melody_array.append(filename)
            self.add_to_trie(filename)
        else:
            self.midifile_name_rythm = filename

    def save_midi_file(self, filename):
        """Tallentaa midi tiedoston
        Args:
            filename: tallennetrie_tenoravan tiedoston nimi
        """
        if self.midifile_name_melody == "":
            return
        self.num_tracks = midi_io.get_file_info(self.midifile_name_melody)
        if self.num_tracks > 1:
            self.do_four_track(self.midifile_name_melody, 0)
        else:
            self.do_one_track_melody(self.midifile_name_melody, 0)

        midi_io.arr_to_midifile(
            filename,
            self.out_file,
            self.time_signature_numerator,
            self.time_signature_denominator)


    def do_one_track_melody(self, filename, lenght):
        """Tekee yksiäänisen koosteen tiedoston materiaalista
        Args:
            filename: tiedosto jonka materiaalista tehdään markovin ketju
            lenght: ei käytössä vielä
        """

        data = midi_io.from_midi_to_list(filename)[0]

        if self.midifile_name_rythm != "":
            data = midi_io.from_midi_to_list(self.midifile_name_rythm)[0]
        rythm = []
        for i in range(0, len(data)):
            rythm.append(data[i][0])

        melody_out = mc.doArray(self.trie, self.markov_depth, len(rythm))

        if not self.use_original_rythm:
            rythm_trie = Trie()
            rythm_trie.insert_array(rythm, self.markov_depth + 1)
            rythm = mc.doArray(rythm_trie, self.markov_depth, len(rythm))

        out = []
        for i in range(len(rythm)):
            out.append((rythm[i], melody_out[i]))
        self.out_file = [out]

    def do_four_track(self, filename, lenght):
        """Tekee neliäänisen koosteen tiedoston materiaalista
        Args:
            filename: tiedosto jonka materiaalista tehdään markovin ketju
            lenght: ei käytössä vielä
        """
        data = midi_io.from_midi_to_list(filename)

        trythm1 = Trie()
        trythm2 = Trie()
        trythm3 = Trie()
        trythm4 = Trie()

        trie_alto = Trie()
        trie_tenor = Trie()
        trie_bass = Trie()

        melody = []
        for i in range(0, len(data[0])):
            melody.append(data[0][i][1])
        tm = Trie()
        tm.insert_array(melody, 3)
        m = mc.doArray(tm, 2, len(data[0]))

        harmonies = make_harmony_table(data)
        rythms = [[], [], [], []]
        rythms = make_rythm_table(data, rythms)

        trythm1.insert_array(rythms[0], 3)
        trythm2.insert_array(rythms[1], 3)
        trythm3.insert_array(rythms[2], 3)
        trythm4.insert_array(rythms[3], 3)

        for i in range(0, len(harmonies[0])):

            trie_alto.insert([harmonies[0][i], harmonies[2][i],
                              harmonies[3][i], harmonies[1][i]])
            trie_tenor.insert(
                [harmonies[0][i], harmonies[3][i], harmonies[2][i]])
            trie_bass.insert([harmonies[0][i], harmonies[3][i]])

        rt1 = [[], [], [], []]
        rt1[0] = mc.doArray(trythm1, 2, 100)
        rt1[1] = mc.doArray(trythm2, 2, 200)
        rt1[2] = mc.doArray(trythm3, 2, 200)
        rt1[3] = mc.doArray(trythm4, 2, 200)

        rythms = [[], [], [], []]
        rythms = make_rythm_table(data, rythms)
        if self.use_original_rythm:
            rt1 = [rythms[0], rythms[1], rythms[2], rythms[3]]

        voices = [[], [], [], []]
        max_lenght = 0
        for i in range(0, len(m)):
            for j in range(0, rt1[0][i]):
                voices[0].append(m[i])
        max_lenght = len(voices[0])

        out = [rt1[0], m, rt1[1], [], rt1[2], [], rt1[3], []]

        time = 0
        next_value = mc.getNext(trie_bass, [voices[0][time]])

        for i in range(0, len(rt1[3])):

            next_value = mc.getNext(trie_bass, [voices[0][time]])
            if next_value == []:
                #print("basso ei löytynyt")
                next_value = [voices[0][time]] - 24
            for j in range(0, rt1[3][i]):
                voices[3].append(next_value)

            out[7].append(next_value)
            time += rt1[3][i]
            if time >= (max_lenght - 1):
                break
        max_lenght = min(max_lenght, len(voices[3]))

        time = 0

        for i in range(0, len(rt1[2])):

            next_value = mc.getNext(trie_tenor, [voices[0][time], voices[3][time]])
            if next_value == []:
                #print("tenori ei löytynyt")
                next_value = voices[0][time] - 12
            for j in range(0, rt1[2][i]):
                voices[2].append(next_value)
            time += rt1[2][i]
            out[5].append(next_value)
            if time >= (max_lenght - 1):
                break

        max_lenght = min(max_lenght, len(voices[2]))

        time = 0

        for i in range(0, len(rt1[1])):
            next_value = mc.getNext(
                trie_alto, [voices[0][time], voices[2][time], voices[3][time]])
            if next_value == []:
                #print("altrie_tenoro ei löytynyt")
                next_value = voices[3][time] + 12
            time += rt1[1][i]
            out[3].append(next_value)
            if time >= (max_lenght - 1):
                break

        out2 = [[], [], [], []]
        for j in range(0, 4):
            for i in range(0, len(out[j * 2 + 1])):
                out2[j].append((out[j * 2][i], out[j * 2 + 1][i]))

        self.out_file = out2


service = Service()
