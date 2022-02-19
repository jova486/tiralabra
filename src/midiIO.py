from midiutil import MIDIFile
import mido


def get_file_info(file_name):
    mid = mido.MidiFile(file_name, clip=True)
    return len(mid.tracks)-1



def from_midi_To_list(filename):
    mid = mido.MidiFile(filename, clip=True)
    data = []
    min_value = 100000

    for track in mid.tracks:

        notes = []
        values = []
        has_notes = False
        for m in track:



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
                    has_notes = True
                    notes.append(m['note'])
                    values.append(note_value)
        if has_notes == True:
            arr = []
            for j, i in enumerate(values):
                arr.append((i, notes[j]))


            data.append(arr)
    out = []
    for j in range(len(data)):
        temp = []
        for data_value in data[j]:

            temp.append((data_value[0]//min_value, data_value[1]))
        out.append(temp)

    return out



def arr_To_midifile(out_file_name, arr, numerator, denominator):
    channel = 0
    time = 0
    channel = 0
    tempo = 120
    volume = 100
    MyMIDI = MIDIFile(len(arr))
    MyMIDI.addTimeSignature(0, time, numerator, denominator, 24)

    MyMIDI.addTempo(0, time, tempo)

    for track_nro,track in enumerate(arr):
        time = 0
        for note in track:

            notevalue = note[0]/4

            MyMIDI.addNote(track_nro, channel, note[1], time, notevalue, volume)

            time = time + notevalue


    with open(out_file_name, "wb") as output_file:
        MyMIDI.writeFile(output_file)
