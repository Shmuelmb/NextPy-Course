import winsound

notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }
list_notes = notes.split('-')


def main():
    for note in list_notes:
        note_name = note.split(',')
        winsound.Beep(int(freqs[note_name[0]]), int(note_name[1]))


if __name__ == '__main__':
    main()
