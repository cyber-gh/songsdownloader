import numpy
import json

json_file = open("general.playlist.json")
json_str = json_file.read()


def song_list(json_str):
    json_data = json.loads(json_str)
    tracks = json_data["items"]
    songs = []
    for el in tracks:
        track = el["track"]
        songs.append([track["name"] + " " + track["artists"][0]["name"]])
        print(track["name"], end="  ")
        print(track["artists"][0]["name"])
    f = open("songs_list.txt", 'a')
    for el in songs:
        f.write(str(el[0]))
        f.write("\n")



song_list(json_str)
