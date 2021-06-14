from Backend.spotifyClient import SpotifyAPI
from Config.config import *
import json

class SpotifyHelpmate():
    spotify =  SpotifyAPI(clientId, clientSecret)
    print("breathe")
    infos = spotify.search({"track": "Free Spirit"})["tracks"]["items"]
    for info in infos:
        
        trackName = info["name"]
        trackUrl = info["external_urls"]['spotify']
        trackId = info["id"]
        album = info["album"]
        albumName = album['name']
        albumId = album['id']
        albumCover = album['images'][0]['url']
        albumUrl = album['external_urls']['spotify']
        artist = info["artists"]
        artistName = artist[0]['name']
        artistId = artist[0]['id']
        artistUrl = artist[0]['external_urls']['spotify']
        track = {
                'trackname': trackName,
                'trackid': trackId,
                'trackurl': trackUrl,
                'albumname': albumName,
                'albumid': albumId,
                'albumurl': albumUrl,
                'albumcover': albumCover,
                'artistname': artistName,
                'artistid': artistId,
                'artisturl': artistUrl}
    # print(spotify.search({"track": "Free Spirit"}))
        print(track)