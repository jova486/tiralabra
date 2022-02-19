from trie import Trie
import midiIO as r
import markov_chain as mc


def make_harmony_table(arr):
    """Apumetodi joka rakentaa matriisin harmonioista jokaiselle tahtiosalle

        Args:
            arr: Taulukko jossa nuotti ja rytmi arvot

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

    for k in range(0, len(arr)):
        for j in range(0, len(arr[k])):
            rythms[k].append(arr[k][j][0]*2)
    return rythms


class Service:
    """Ohjelman toimintalogiikasta vastaava luokka
    """

    def __init__(self):
        """Luokan konstruktori.

        """
        self.use_original_rythm = False
        self.midifile_name_melody = ""
        self.midifile_name_rythm = ""
        self.out_file = []
        self.num_tracks = 0
        self.time_signature_numerator = 4
        self.time_signature_denominator = 2
        self.markov_depth = 2
        self.trie = Trie()

    def set_time_signature(self, text):
        """Asettaa tahtilajin.
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
        """Asettaa markovin ketjun asteen.
        Args:
            text: ketjun aste merkkijonona
        """

        self.markov_depth = int(text)

    def reset_trie(self):
        self.trie = Trie()


    def add_file_name(self, filename, text):
        """asettaa tallennettavan midi tiedoston nimen
        Args:
            filename: miditiedoston nimi
            text: melodia tai rytmi
        """
        if text == "melody":
            self.midifile_name_melody = filename
        else:
            self.midifile_name_rythm = filename

    def save_midi_file(self, filename):
        """Tallentaa midi tiedoston
        Args:
            filename: tallennettavan tiedoston nimi
        """
        if self.midifile_name_melody == "":
            return
        self.num_tracks = r.get_file_info(self.midifile_name_melody)
        if self.num_tracks > 1:
            self.do_four_track(self.midifile_name_melody, 0)
        else:
            self.do_one_track_melody(self.midifile_name_melody, 0)
        if self.num_tracks > 1:
            r.arr_To_midifile(
                filename, self.out_file, self.time_signature_numerator, self.time_signature_denominator)
        else:
            r.arr_To_midifile(
                filename, self.out_file, self.time_signature_numerator, self.time_signature_denominator)

    def do_one_track_melody(self, filename, lenght):
        """Tekee yksiäänisen koosteen tiedoston materiaalista
        Args:
            filename: tiedosto jonka materiaalista tehdään markovin ketju
            lenght: ei käytössä vielä
        """

        data = r.from_midi_To_list(filename)[0]

        melody = []
        for i in range(0, len(data)):
            melody.append(data[i][1])

        trie =  self.trie
        trie.insert_array(melody, self.markov_depth+1)

        if self.midifile_name_rythm != "":
            data = r.from_midi_To_list(self.midifile_name_rythm)[0]
        rythm = []
        for i in range(0, len(data)):
            rythm.append(data[i][0])

        melody_out = mc.doArray(trie, self.markov_depth, len(rythm))

        if self.use_original_rythm == False:
            rythm_trie = Trie()
            rythm_trie.insert_array(rythm, self.markov_depth+1)
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
        data = r.from_midi_To_list(filename)
        trythm1 = Trie()
        trythm2 = Trie()
        trythm3 = Trie()
        trythm4 = Trie()

        ta = Trie()
        tt = Trie()
        tb = Trie()

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

            ta.insert([harmonies[0][i], harmonies[2][i],
                      harmonies[3][i], harmonies[1][i]])
            tt.insert([harmonies[0][i], harmonies[3][i], harmonies[2][i]])
            tb.insert([harmonies[0][i], harmonies[3][i]])

        rt1 = [[], [], [], []]
        rt1[0] = mc.doArray(trythm1, 2, 100)
        rt1[1] = mc.doArray(trythm2, 2, 200)
        rt1[2] = mc.doArray(trythm3, 2, 200)
        rt1[3] = mc.doArray(trythm4, 2, 200)

        rythms = [[], [], [], []]
        rythms = make_rythm_table(data, rythms)
        if self.use_original_rythm == True:
            rt1 = [rythms[0], rythms[1], rythms[2], rythms[3]]

        voices = [[], [], [], []]
        max_lenght = 0
        for i in range(0, len(m)):
            for j in range(0, rt1[0][i]):
                voices[0].append(m[i])
        max_lenght = len(voices[0])

        out = [rt1[0], m, rt1[1], [], rt1[2], [], rt1[3], []]

        time = 0
        b = mc.getNext(tb, [voices[0][time]])

        for i in range(0, len(rt1[3])):

            b = mc.getNext(tb, [voices[0][time]])
            if b == []:
                #print("basso ei löytynyt")
                b = [voices[0][time]]-24
            for j in range(0, rt1[3][i]):
                voices[3].append(b)

            out[7].append(b)
            time += rt1[3][i]
            if time >= (max_lenght-1):
                break
        max_lenght = min(max_lenght, len(voices[3]))

        time = 0

        for i in range(0, len(rt1[2])):

            b = mc.getNext(tt, [voices[0][time], voices[3][time]])
            if b == []:
                #print("tenori ei löytynyt")
                b = voices[0][time]-12
            for j in range(0, rt1[2][i]):
                voices[2].append(b)
            time += rt1[2][i]
            out[5].append(b)
            if time >= (max_lenght-1):
                break

        max_lenght = min(max_lenght, len(voices[2]))

        time = 0

        for i in range(0, len(rt1[1])):
            b = mc.getNext(
                ta, [voices[0][time], voices[2][time], voices[3][time]])
            if b == []:
                #print("altto ei löytynyt")
                b = voices[3][time]+12
            time += rt1[1][i]
            out[3].append(b)
            if time >= (max_lenght-1):
                break

        out2 = [[], [], [], []]
        for j in range(0, 4):
            for i in range(0, len(out[j*2+1])):
                out2[j].append((out[j*2][i], out[j*2+1][i]))

        self.out_file = out2


service = Service()
