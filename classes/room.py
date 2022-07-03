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

    def check_in_guest(self, guest):
        if guest.in_room == False:
            self.guests.append(guest)
            guest.checked_in = True
            guest.in_room = self.room_no
        else:
            return "Guest already checked in"