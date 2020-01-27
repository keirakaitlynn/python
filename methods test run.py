import musicbox
my_music = musicbox.MusicBox()
file_name = "shark.txt"

def play_song(file_name):
    results = []
    # Converts given file into a list of tuples representing each line in the file
    for line in open(file_name):
        if line.startswith("/") == False:
            line_split = line.split(" ")
            if len(line_split) == 4:
                note = (line_split[0], line_split[1], line_split[2], int(line_split[3]))
            else:
                note = (line_split[0], (line_split[1]))
            results.append(note)
    # results = [('D', 800), ('E', 800), ('G', 300), (...) ]
    # Unpacks each tuple
    for each_note in results:
        # Unpacking:
        if len(each_note) == 4:
            # Unpacking:
            (first, second, third, msecs) = each_note
            print(each_note)
##            my_music.play_chord(each_note, msecs)
        else:
            # Unpacking:
            (note_letter, msecs) = each_note
            if note_letter == "P":
                my_music.pause(msecs)
            elif note_letter == "I":
                my_music.change_instrument(msecs)
            else:
                # Converts note_letter to its integer value
                note_int = note_to_int(note_letter)
                my_music.play_note(note_int, msecs)



##file_name = "shark.txt"
##
##def play_song(file_name):
##    results = []
##    # Converts given file into a list of tuples representing each line in the file
##    for line in open(file_name):
##        if line.startswith("/") == False:
##            line_split = line.split(" ")
##            note = (line_split[0], int(line_split[1]))
##            results.append(note)
##    # results = [('D', 800), ('E', 800), ('G', 300), (...) ]
##    # Unpacks each tuple
##    for each_tuple in results:
##        (note_letter, msecs) = note
        

# creates a list of tuples (each tuple = each note)
print(play_song(file_name))

##note = "^^C"
##
##num_carats = 0
### For every ^ before, increase its integer value by 12
##for each_char in (range(len(note))):
##    if note[each_char] == "^":
##        num_carats += 1
##
##int_value = 60
##if num_carats > 0:
##    int_value += 12*num_carats
##
##print(int_value)

##
##MAJOR_INTERVALS = [2, 2, 1, 2, 2, 2, 1]
##MINOR_INTERVALS = [2, 1, 2, 2, 1, 2, 2]
##
##scale = (60, "major")
##
##def scale_to_ints(scale):
##    (first_note, scale_type) = scale
##    notes = [first_note]
##    note = first_note
##    if scale_type == "major":
##        for each_interval in MAJOR_INTERVALS:
##            note += each_interval
##            notes.append(note)
##    return notes
##
##print(scale_to_ints(scale))

