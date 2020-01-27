# Homework 3

# 1. Import musicbox @ the top
import musicbox

# 2. Create a music box that you can use globally
my_music = musicbox.MusicBox()

# INITIALIZATION
NOTES = [("C", 60, 500), ("D", 62, 500), ("E", 64, 500), ("F", 65, 500), ("G", 67, 500), ("A", 69, 500), ("B", 71, 500)]
MAJOR_INTERVALS = [2, 2, 1, 2, 2, 2, 1]
MINOR_INTERVALS = [2, 1, 2, 2, 1, 2, 2]

## -----// methods //----------------------------------------------------------

# 1. Given a string representing a note, returns the integer value of that note
def note_to_int(note):
    # INITIALIZATION
    int_value = -1
    # EACH_TUPLE = NOTE_LETTERS
    for EACH_TUPLE in NOTES:
        # Unpack each tuple:
        (note_letter, note_int, msecs) = EACH_TUPLE
        # note_index is set to the index of each note_letter (from list) in given note
        note_index = note.rfind(note_letter)
        # Note letter must be a valid note; Note letter must be in the list of NOTES
        if note_letter == note[note_index]:
            int_value = note_int
    # If given note contains more than just the note letter, checks if other characters are valid input
    if len(note) > 1:
        valid_symbol = False
        # For every ^ before, increase its integer value by 12
        for each_char in (range(len(note))):
            if note[each_char] == "^":
                int_value += 12
                valid_symbol = True
        # If a # follows, increase its integer value by 1
        if note[note.rfind("#")] == "#":
            int_value += 1
            valid_symbol = True
        # If a b follows, decrease its integer value by 1
        if note[note.rfind("b")] == "b":
            int_value -= 1
            valid_symbol = True
        # If the given note contains anything but a # or b, the int_value = -1
        if valid_symbol == False:
            int_value = -1
    return int_value

# 2. Prints the program's main menu
def print_menu():
    print("""
    Main menu:
    1. Play scale
    2. Play song
    3. Quit
    """)

# 3. Gets user's menu choice
def get_menu_choice():
    result = True
    while result == True:
        menu_choice = int(input("Please enter a selection: "))
        if menu_choice >= 1 or menu_choice <= 3:
            return menu_choice

# 4. Asks the user to input the name of a scale
def get_scale():
    result = True
    while result == True:
        scale_name = input("Please enter a scale name: ")
        space_index = scale_name.rfind(" ")
        # Note letter is anything before the space in a given scale_name
        note_letter = scale_name[0:space_index]
        # Scale_type is anything after the space in a given scale_name
        scale_type = scale_name[space_index+1:]
        note_int = note_to_int(note_letter)
        # Packing:
        scale = (note_int, scale_type)
        # Input parameters; Validates note & scale_type & Asks user for input again if invalid
        if (note_to_int(note_letter) != -1) and(scale_type == "major" or scale_type == "minor"):
            return scale

# 5. Given a tuple (ie. (60, "major")),
# creates a list of 8 integers according to given starting note & scale type
def scale_to_ints(scale):
    # Unpacking:
    (first_note, scale_type) = scale
    # Initialize an array
    notes = [first_note]
    note = first_note
    if scale_type == "major":
        scale_intervals = MAJOR_INTERVALS
    else:
        scale_intervals = MINOR_INTERVALS
    for each_interval in scale_intervals:
        # No more than two lines allowed when altering list called "notes"
        note += each_interval
        notes.append(note)
    return notes

# 6. Plays scale
def menu_play_scale():
    notes_list = scale_to_ints(get_scale())
    for each_note in notes_list:
        my_music.play_note(each_note, 500)

# 7. User inputs file_name of song to play, returns the file name in form of a string
def get_song_file():
    file_name = input("Please enter a song file name: ")
    return file_name

# 8. Given a file name of a song, plays the song in that file
def play_song(file_name):
    results = []
    # Converts given file into a list of tuples representing each line in the file
    for line in open(file_name):
        if line.startswith("/") == False:
            line_split = line.split(" ")
            # When a line has more than two items; when a line contains more than just one note
            if len(line_split) > 2:
                # Initializes a list called chord
                chord = []
                # Defines what's included in a tuple, "split"
                split = (line_split[0], line_split[1], line_split[2], int(line_split[3]))
                #print(split) # Prints ('D', 'F', 'A', 800)
                results.append(split)
                print(results)
            else:
                note_tuple = (line_split[0], int(line_split[1]))
                # Unpacking tuple, "note"
                (first_note, msecs) = note_tuple
##                note_int = [note_to_int(first_note)]
##                note = (note_int, msecs)
                results.append(note_tuple)
##------------// test runs //-----------------------------------------------
##    (chord, msecs) = results[0]
##    my_music.play_chord(chord, msecs)
##    print(len(results[0]))
##-----------------------------------------------------
    # Unpacks each tuple
    for each_note in results:
        # Unpacking:
        if len(each_note) == 4:
            # Unpacking tuple, "each_note"
            (first_note, second_note, third_note, msecs) = each_note
            # Converts notes to respective integer values (list format)
            notes_int = [note_to_int(first_note), note_to_int(second_note), note_to_int(third_note)]
            my_music.play_chord(notes_int, msecs)
        if len(each_note) <= 2:
            # Unpacking:
            (note_letter, msecs) = each_note
            if note_letter == "P":
                my_music.pause(msecs)
            elif note_letter == "I":
                my_music.change_instrument(msecs)
            else:
                # Converts note_letter to its integer value
                note_int = note_to_int(note_letter)
                # plays note
                my_music.play_note(note_int, msecs)

# 9. Plays song
def menu_play_song():
    play_song(get_song_file())

## ----------------------------------------------------------------------------
    
def main():
    choice = 0
    while choice != 3:
        print_menu()
        choice = get_menu_choice()
        if choice == 1:
            menu_play_scale()
        elif choice == 2:
            menu_play_song()
        elif choice == 3:
            exit()
            
## -----// test runs //--------------------------------------------------------
##    print(note_to_int("^^C#"))
##    play_song("shark.txt")
##    EXAMPLE
##    noteToPlay = 61 # This is C sharp
##    my_music.play_note(noteToPlay, 500) # plays C sharp for 500 milliseconds
##    (note_letter, note_int, msecs) = NOTES[0] # Unpacks first tuple in list of "NOTES"
##    my_music.play_note(note_int, msecs) # Output
## ----------------------------------------------------------------------------

main()

# 3. Write my_music.close() after main() @ bottom of the program
my_music.close()

# INTEGER NOTATION
# Major: 2, 2, 1, 2, 2, 2, 1
# minor: 2, 1, 2, 2, 1, 2, 2

# MIDI files -> MIDI player
# Each line: "[1+ note(s)] [# of milliseconds]"
# ie) "C E G 1000"

# TUPLES LIST
# List of tuples:
# -> "people = [("Mike", "Michaelson", 21), ("Jennifer", "Johnson", 23)]"
# Unpacking first tuple in list:
# -> "student_first, student_last, student_age = people[1]"
# Output:
# -> "print(student_first)"

# TUPLES
# Packing:
# -> "student = ("Bob", "Roberts", 19)
# Unpacking:
# -> "student_first, student_last, student_age = student
# Output:
# print(student_first)
