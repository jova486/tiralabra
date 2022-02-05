from midiutil import MIDIFile
import mido


def get_file_info(file_name):
    mid = mido.MidiFile(file_name, clip=True)
    return len(mid.tracks)


def from_midi_To_list1(s):
    mid = mido.MidiFile(s, clip=True)
    notes = []
    values = []

    min_value = 100000
    for m in mid.tracks[0][:]:

        m = m.dict()

        if m['type'] == "note_on":

            if m['velocity'] == 0:
                m['type'] = "note_off"

        if m['type'] == "note_off":
            note_value = m['time']
            if note_value != 0:
                if note_value % 2 != 0:
                    note_value += 1
                print(note_value)
                if min_value > note_value:
                    min_value = note_value

                notes.append(m['note'])
                values.append(note_value)
    arr = []
    for j, i in enumerate(values):
        i = i//min_value
        arr.append((i, notes[j]))

    return arr


def from_midi_To_list1_backUp(s):
    mid = mido.MidiFile(s, clip=True)
    counter = 0
    arr = []
    temp = []
    note_on = True
    '''
    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        for msg in track:
            print(msg.dict())
            if msg.is_meta:
                print(msg.dict())
                if msg.type == 'key_signature':
                    print(msg.dict())
                if msg.type == 'time_signature':
                    print(str(msg))
    '''
    for m in mid.tracks[0][:]:
        # print(m)
        m = str(m)

        m = m.split(" ")
        if m[0] == "note_on":
            msg = int(''.join(filter(str.isdigit, m[3])))
            if msg == 0:
                m[0] = "note_off"

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
                    temp.append(m[4] // 256)
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
        notevalue = i[0] / 4
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


def arr_To_midifile_4(s, arr, time_signature):
    num_tracks = len(arr)
    track = 0
    channel = 0
    time = 0
    tempo = 120
    volume = 100
    MyMIDI = MIDIFile(num_tracks)
    MyMIDI.addTimeSignature(track, time, time_signature, 2, 1)

    MyMIDI.addTempo(track, time, tempo)

    for j in range(len(arr)):
        time = 0
        for i in arr[j]:

            notevalue = i[0]/4

            MyMIDI.addNote(track, channel, i[1], time, notevalue, volume)

            time = time + notevalue
        track += 1
    '''
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
'''
    with open(s, "wb") as output_file:
        MyMIDI.writeFile(output_file)
