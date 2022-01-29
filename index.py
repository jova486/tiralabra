from src.trie import Trie
import src.midiIO as r
import src.markov_chain as mc
import random

def make_harmony_table(arr, harmonies):

    for k in range(0,len(arr)):
        for j in range(0, len(arr[k])):
            for i in range(0, arr[k][j][0]):
                harmonies[k].append(arr[k][j][1])
    return harmonies

def make_rythm_table(arr):
    rythms = [[], [], [], []]

    for k in range(0,len(arr)):
        for j in range(0, len(arr[k])):
            rythms[k].append(arr[k][j][0])
    return rythms

def main():

    #arr = r.from_midi_To_list("data/midi.mid")
    temp = r.from_midi_To_list_3("data/midi1.mid")
    h = [[], [], [], []]
    harmonies = make_harmony_table(temp,h)

    rythms = make_rythm_table(temp)

    trythm1 = Trie()
    trythm1.insert_array(rythms[0],4)

    trythm2 = Trie()
    trythm2.insert_array(rythms[1],4)

    trythm3 = Trie()
    trythm3.insert_array(rythms[2],4)

    trythm4 = Trie()
    trythm4.insert_array(rythms[3],4)




    ta = Trie()
    tt = Trie()
    tb = Trie()

    melody = []
    for i in range(0,len(temp[0])):
        melody.append(temp[0][i][1])

    #print(len(harmonies[0]),len(harmonies[1]),len(harmonies[2]),len(harmonies[3]))
    for i in range(0, len(harmonies[0])):

        ta.insert([harmonies[0][i], harmonies[2][i], harmonies[3][i], harmonies[1][i]])
        tt.insert([harmonies[0][i], harmonies[3][i], harmonies[2][i]])
        tb.insert([harmonies[0][i], harmonies[3][i]])


    tm = Trie()


    tm.insert_array(melody, 3)

    m = mc.doArray(tm,2,20)


    rt1 = [[], [], [], []]
    rt1[0] = mc.doArray(trythm1,2,50)
    rt1[1] = mc.doArray(trythm2,2,200)
    rt1[2] = mc.doArray(trythm3,2,200)
    rt1[3] = mc.doArray(trythm4,2,200)




    voices = [[], [], [], []]
    max_lenght = 0
    for i in range(0, len(m)):
        for j in range(0, rt1[0][i]):
            voices[0].append(m[i])
    max_lenght = len(voices[0])


    out = [rt1[0],m,rt1[1],[],rt1[2],[],rt1[3],[]]


    time = 0
    b = mc.getNext(tb, [voices[0][time]])

    for i in range(0, len(rt1[3])):

        b = mc.getNext(tb, [voices[0][time]])
        if b == []:
            b=[voices[0][time]]-24
        for j in range(0, rt1[3][i]):
            voices[3].append(b)

        out[7].append(b)
        time += rt1[3][i]
        if time >= (max_lenght-1):
            break
    max_lenght = min(max_lenght,len(voices[3]))

    time = 0

    for i in range(0, len(rt1[2])):

        b = mc.getNext(tt, [voices[0][time],voices[3][time]])
        if b == []:
            b=voices[0][time]-12
        for j in range(0, rt1[2][i]):
            voices[2].append(b)
        time += rt1[2][i]
        out[5].append(b)
        if time >= (max_lenght-1):
            break

    max_lenght = min(max_lenght,len(voices[2]))

    time = 0


    for i in range(0, len(rt1[1])):
        b = mc.getNext(ta, [voices[0][time],voices[2][time],voices[3][time]])
        if b == []:
            b=voices[3][time]+12
        time += rt1[1][i]
        out[3].append(b)
        if time >= (max_lenght-1):
            break


    out2 = [[], [], [], []]
    for j in range(0,4):
        for i in range(0,len(out[j*2+1])):
            out2[j].append((out[j*2][i],out[j*2+1][i]))


    r.arr_To_midifile_4("tira4.mid", out2)


if __name__ == "__main__":
    main()
