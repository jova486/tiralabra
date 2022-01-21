from src.trie import Trie
import src.midiIO as r
import src.markov_chain as mc
def main():
    arr = r.from_midi_To_list("data/chords.mid")
    print(arr)
    t = Trie()

    print(t.query([7]))


    t.insert([1,2,3])
    t.insert([1,2,4])
    t.insert([1,2,5])
    t.insert([1,2,6])
    t.insert([1,2,6])
    print(t.query([1,2]))
    arr = []
    for i in range(0,100):
        arr.append(mc.getNext(t,[1,2]))
    print(arr)





if __name__ == "__main__":
    main()