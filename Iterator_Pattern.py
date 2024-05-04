class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def __repr__(self):
        return f"{self.title} by {self.artist}"

class SongIterator:
    def __init__(self, songs):
        self.songs = songs
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.songs):
            song = self.songs[self.index]
            self.index += 1
            return song
        else:
            raise StopIteration

class PlaylistImpl:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def create_iterator(self):
        return SongIterator(self.songs)

def main():
    # Create a playlist
    my_playlist = PlaylistImpl()

    # Add songs to the playlist
    my_playlist.add_song(Song("Yesterday", "The Beatles"))
    my_playlist.add_song(Song("Bohemian Rhapsody", "Queen"))
    my_playlist.add_song(Song("Stairway to Heaven", "Led Zeppelin"))

    # Get an iterator for the playlist
    iterator = my_playlist.create_iterator()

    # Iterate through the playlist
    for song in iterator:
        print(song)

if __name__ == "__main__":
    main()
