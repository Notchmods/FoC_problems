"""Read files, (same thing for CSV)""""
def read_files("song.txt"):
        """r: read the file"""
    with open("song.txt","r") as songs:
        for lines in songs.read().split("\n"):
            print(lines)
    
    songs.close()
    return


"""Write files"""
def write_files("songs.txt"):   
    """a: Append things into the file without erasing
        c: Erase everything and write into file"""
    with open("song.txt","a") as writing:
        writing.write("Let me sing a song ") 
    
    
    writing.close()
    return

