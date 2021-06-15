from Backend.spotifyClient import SpotifyAPI
from Config.config import *

class SpotifyHelpmate():
    def __init__(self):
        self.spotify =  SpotifyAPI(clientId, clientSecret)

    def searchTrack(self, songName):
        tracks = []
        infos = self.spotify.search({"track": songName})["tracks"]["items"]
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
        return tracks

    def getTrackName(self, track):
        return track['trackname']

    def getTrackId(self, track):
        return track['trackid']

    def getTrackUrl(self, track):
        return track['trackurl']

    def getAlbumName(self, track):
        return track['albumname']

    def getAlbumId(self, track):
        return track['albumid']

    def getAlbumUrl(self, track):
        return track['albumurl']

    def getAlbumCover(self, track):
        return track['albumcover']

    def getArtistName(self, track):
        return ', '.join(artist['artistname'] for artist in track['artist'])

    def getArtistId(self, track):
        return ', '.join(artist['artistid'] for artist in track['artist'])

    def getArtistUrl(self, track):
        return ', '.join(artist['artisturl'] for artist in track['artist'])