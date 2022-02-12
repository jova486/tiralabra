from midiutil import MIDIFile
import mido


def get_file_info(file_name):
    mid = mido.MidiFile(file_name, clip=True)
    return len(mid.tracks)-1


def from_midi_To_list1(s):
    mid = mido.MidiFile(s, clip=True)
    notes = []
    values = []
    start = 0
    min_value = 100000
    if len(mid.tracks)>1:
        start = 1


    for m in mid.tracks[start][:]:

        m = m.dict()

        if m['type'] == "note_on":

            if m['velocity'] == 0:
                m['type'] = "note_off"

        if m['type'] == "note_off":
            note_value = m['time']
            if note_value != 0:
                if note_value % 2 != 0:
                    note_value += 1

                if min_value > note_value:
                    min_value = note_value

                notes.append(m['note'])
                values.append(note_value)
    arr = []
    for j, i in enumerate(values):
        i = i//min_value
        arr.append((i, notes[j]))

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


def arr_To_midifile(s, arr, numerator,denominator):
    track = 0
    channel = 0
    time = 0
    tempo = 120
    volume = 100
    MyMIDI = MIDIFile(1)
    MyMIDI.type = 0
    MyMIDI.addTimeSignature(track, time, numerator, denominator, 24)

    MyMIDI.addTempo(track, time, tempo)

    for i in arr:
        notevalue = i[0] / 4
        for n in range(1, len(i)):
            MyMIDI.addNote(track, channel, i[n], time, notevalue, volume)

        time = time + notevalue

    with open(s, "wb") as output_file:
        MyMIDI.writeFile(output_file)


def arr_To_midifile_4(s, arr, numerator,denominator):
    num_tracks = len(arr)
    track = 0
    channel = 0
    time = 0
    tempo = 120
    volume = 100
    MyMIDI = MIDIFile(num_tracks)
    MyMIDI.addTimeSignature(track, time, numerator, denominator, 24)

    MyMIDI.addTempo(track, time, tempo)

    for j in range(len(arr)):
        time = 0
        for i in arr[j]:

            notevalue = i[0]/4

            MyMIDI.addNote(track, channel, i[1], time, notevalue, volume)

            time = time + notevalue
        track += 1

    with open(s, "wb") as output_file:
        MyMIDI.writeFile(output_file)
