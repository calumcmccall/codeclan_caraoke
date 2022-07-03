class Room:

    def __init__(self, _room_no):
        self.room_no = _room_no
        self.guests = []
        self.songs = []

    def add_song_to_room(self, song):
        self.songs.append(song)