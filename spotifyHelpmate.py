from Backend.spotifyClient import SpotifyAPI
from Config.config import *
import json

class SpotifyHelpmate():
    spotify =  SpotifyAPI(clientId, clientSecret)
    # print(spotify.search({"track": "breathe"}))
    print(json.dumps(spotify.search({"track": "breathe"}), indent=4, sort_keys=True))