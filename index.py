from src.trie import Trie
import src.midiIO as r
import src.markov_chain as mc
import random
def main():
    arr = r.from_midi_To_list("data/chords.mid")
    arr += r.from_midi_To_list("data/chords1.mid")

    melody = []
    rythm = []

    for i in arr:

        melody.append(i[-1])
        rythm.append(i[0])


    tm1 = Trie()
    tm2 = Trie()
    tr = Trie()


    tm1.insert_array(melody,2)
    tm2.insert_array(melody,3)
    tr.insert_array(rythm,3)
    a = random.choice(melody)
    print(a)
    b = mc.getNext(tm1,[a])
    out = []
    for i in range(0,10):
        a = mc.getNext(tm1,[b])
        if a ==[]:
            break
        out.append(a)
        b=a

    print(out)
    a = random.choice(melody)
    print(a)
    b = mc.getNext(tm1,[a])
    print(b)
    out = []
    for i in range(0,10):
        c = mc.getNext(tm2,[a,b])
        if c ==[]:
            break
        out.append(c)
        a=b
        b=c
    print(out)







if __name__ == "__main__":
    main()