from midiutil import MIDIFile
import mido


def from_midi_To_list(s):
    s1 = []
    mid = mido.MidiFile(s, clip=True)
    counter = 0
    arr = []
    temp = []
    note_on = True

    for m in mid.tracks[4][:]:

        m = str(m)
        m = m.split(" ")
        if m[0] == "note_on":
            if not note_on:
                counter = -1
            note_on = True

        if m[0] == "note_off" and note_on:
            counter = 0
            note_on = False

        for i in range(1, len(m)):
            if m[0] == "note_off":
                m[i] = int(''.join(filter(str.isdigit, m[i])))
        if m[0] == "note_off":
            if counter == 0:
                temp.append(m[4])
                counter = 1
            temp.append((m[2]))

        if counter == -1:
            arr.append(temp)
            counter = 0
            temp = []

    return arr


def from_midi_To_list_2(s):
    s1 = []
    mid = mido.MidiFile(s, clip=True)
    counter = 0
    arr = []

    note_on = True
    for i in range(1, len(mid.tracks)):
        temp_arr = []
        temp = []
        for m in mid.tracks[i][:]:
            print(m)
            m = str(m)
            m = m.split(" ")
            if m[0] == "note_on":
                if not note_on:
                    counter = -1
                note_on = True

            if m[0] == "note_off" and note_on:
                counter = 0
                note_on = False

            for i in range(1, len(m)):
                if m[0] == "note_off":
                    m[i] = int(''.join(filter(str.isdigit, m[i])))
            if m[0] == "note_off":
                if counter == 0:
                    temp.append(m[4] // 512)
                    counter = 1
                temp.append(m[2])

            if counter == -1:
                temp_arr.append(temp)
                counter = 0
                temp = []
        arr.append(temp_arr)

    return arr


def from_midi_To_list_3(s):

    mid = mido.MidiFile(s, clip=True)
    arr = []

    for i in range(1, (len(mid.tracks))):

        temp_arr = []

        for m in mid.tracks[i][:]:

            m = str(m)
            m = m.split(" ")
            if m[0] == "note_off":
                temp = []

                for i in range(1, len(m)):
                    m[i] = int(''.join(filter(str.isdigit, m[i])))
                temp.append(m[4] // 256)
                temp.append(m[2])
                temp_arr.append(temp)

        arr.append(temp_arr)

    return arr


def arr_To_midifile(s, arr):
    track = 0
    channel = 0
    time = 0
    tempo = 120
    volume = 100
    MyMIDI = MIDIFile(1)
    MyMIDI.addTimeSignature(track, time, 3, 2, 1)

    MyMIDI.addTempo(track, time, tempo)

    for i in arr:
        notevalue = i[0] / 1024
        for n in range(1, len(i)):
            MyMIDI.addNote(track, channel, i[n], time, notevalue, volume)

        time = time + notevalue

    with open(s, "wb") as output_file:
        MyMIDI.writeFile(output_file)


def arr_To_midifile_2(s, arr):
    track = 0
    channel = 0
    time = 0
    tempo = 120
    volume = 100
    MyMIDI = MIDIFile(2)
    MyMIDI.addTimeSignature(track, time, 3, 2, 1)

    MyMIDI.addTempo(track, time, tempo)

    for i in arr:
        notevalue = i[0] / 1024

        MyMIDI.addNote(0, channel, i[1], time, notevalue, volume)

        time = time + notevalue

    time = 0
    for i in arr:
        notevalue = i[2] / 1024

        MyMIDI.addNote(1, channel, i[3], time, notevalue, volume)

        time = time + notevalue

    with open(s, "wb") as output_file:
        MyMIDI.writeFile(output_file)

def arr_To_midifile_4(s, arr):
    track = 0
    channel = 0
    time = 0
    tempo = 120
    volume = 100
    MyMIDI = MIDIFile(4)
    MyMIDI.addTimeSignature(track, time, 3, 2, 1)

    MyMIDI.addTempo(track, time, tempo)

    for i in arr[0]:
        notevalue = i[0]/4

        MyMIDI.addNote(0, channel, i[1], time, notevalue, volume)

        time = time + notevalue

    time = 0
    for i in arr[1]:
        notevalue = i[0]/4

        MyMIDI.addNote(1, channel, i[1], time, notevalue, 60)

        time = time + notevalue

    time = 0
    for i in arr[2]:
        notevalue = i[0]/4

        MyMIDI.addNote(2, channel, i[1], time, notevalue, 60)

        time = time + notevalue
    time = 0
    for i in arr[3]:
        notevalue = i[0]/4

        MyMIDI.addNote(3, channel, i[1], time, notevalue, 80)

        time = time + notevalue

    with open(s, "wb") as output_file:
        MyMIDI.writeFile(output_file)