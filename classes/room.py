class Room:

    def __init__(self, _room_no):
        self.room_no = _room_no
        self.guests = []
        self.songs = []

    def add_song_to_room(self, song):
        self.songs.append(song)

    def add_songs_to_room(self, songs_to_add):
        for song in songs_to_add:
            self.add_song_to_room(song)