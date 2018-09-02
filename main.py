from browser import *


def main():
    firefox = Browser("/home/cyber-gh/Music/All")
    f = open("songs_list.txt")
    data = [line.rstrip() for line in open("songs_list.txt")]
    count = 1
    for song in data:
        print("Working on song ", count)
        firefox.get_song(song)
        count += 1


if __name__ == "__main__":
    main()