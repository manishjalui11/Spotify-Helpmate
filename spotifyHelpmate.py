from Backend.spotifyClient import SpotifyAPI
from Config.config import *
import json

class SpotifyHelpmate():
    spotify =  SpotifyAPI(clientId, clientSecret)
    print("breathe")
    tracks = []
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
        artistsInfo = info["artists"]
        artists = []
        for artistInfo in artistsInfo:
            artistName = artistInfo['name']
            artistId = artistInfo['id']
            artistUrl = artistInfo['external_urls']['spotify']
            artist = {
                'artistname': artistName,
                'artistid': artistId,
                'artisturl': artistUrl}
            artists.append(artist)
        # artist.clear()
        track = {
                'trackname': trackName,
                'trackid': trackId,
                'trackurl': trackUrl,
                'albumname': albumName,
                'albumid': albumId,
                'albumurl': albumUrl,
                'albumcover': albumCover,
                'artist': artists}
        tracks.append(track)
        # print(track)
        # print("\n\n #### \\n\n")
        # track.clear()

    print(tracks)