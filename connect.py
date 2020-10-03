import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_info():
    script_dir = os.path.dirname(__file__)
    all_dir = script_dir.split("/")
    conf_file="/".join(all_dir[:-1])+"/conf.txt"
    with open(conf_file,"r") as f:
        c_id=0
        c_secret_id=0
        contents = f.readlines()
        all_elem=contents[0].split("=")
        c_id = all_elem[1].replace(" ", "").strip()
        all_elem=contents[1].split("=")
        c_secret_id = all_elem[1].replace(" ", "").strip()

    return (c_id, c_secret_id)

def connexion(client_id, client_secret):
    con = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    return con



def get_results(con, song_id) :
    res = con.audio_analysis(song_id)
    return res

