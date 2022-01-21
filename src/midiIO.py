import mido
def from_midi_To_list(s):
    s1 = []
    mid = mido.MidiFile(s, clip=True)
    counter = 0
    arr = []
    temp = []
    note_on = True
    for m in mid.tracks[1][:]:

        m = str(m)
        m=m.split(" ")
        if m[0] == "note_on":
            if note_on == False:
                counter = -1
            note_on = True


        if m[0] == "note_off" and note_on == True:
            counter = 0
            note_on = False

        for i in range(1,len(m)):
            if m[0] == "note_off" :
                m[i]= int(''.join(filter(str.isdigit, m[i])))
        if m[0] == "note_off":
            if counter == 0:
                temp.append(m[4])
                counter = 1
            temp.append(m[2])

        if counter == -1:
            arr.append(temp)
            counter = 0
            temp = []

    return arr


from midiutil import MIDIFile

def arr_To_midifile(s, arr):
    track = 0
    channel = 0
    time = 0
    tempo = 80
    volume = 100
    MyMIDI = MIDIFile(1)

    MyMIDI.addTempo(track,time, tempo)

    for i in arr:
        notevalue =i[0]/1024
        for n in range(1,len(i)):
            MyMIDI.addNote(track, channel, i[n], time, notevalue, volume)


        time = time + notevalue

    with open(s, "wb") as output_file:
        MyMIDI.writeFile(output_file)
