import musicbox
def main():
    m = musicbox.MusicBox()
    m.play_note(60, 1000)
    m.play_chord([60, 64, 67], 1000)
    m.close()
main()
