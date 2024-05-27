"""Read files""""
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

#Reading CSV files
"""Same thing as reading and writing files except
you need to specify reader or writer"""
import csv
def csvplay(csvfiles):
    with open(csvfiles,"r") as files:
            #This
        csv_reader=csv.reader(files)
        for lines in csv_reader:
            print(lines)
    files.close()
    return
