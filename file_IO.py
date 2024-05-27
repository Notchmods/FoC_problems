"""Read files""""
def approximate_song("song.txt"):
    with open("fakesong.txt","r") as songs:
        for lines in songs.read().split("\n"):
            print(lines)
    
    songs.close()
    return
