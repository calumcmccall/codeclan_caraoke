import imp
from this import s
import unittest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room(1)
        self.room_2 = Room(2)

        self.song_1 = Song("Running up that hill", "Kate Bush")
        self.song_2 = Song("Afraid to feel", "LF System")
        self.song_3 = Song("As it was", "Harry Styles")
        self.song_4 = Song("Break my soul", "Beyonce")
        self.song_5 = Song("Green green grass", "George Ezra")

        self.room_1.songs.append(self.song_1)



    def test_room_has_room_no(self):
        self.assertEqual(1, self.room_1.room_no)

    def test_add_song_to_room_from_start(self):
        self.assertEqual(self.room_1.songs[0], self.song_1)

    def test_add_song_on_request(self):
        self.room_1.add_song_to_room(self.song_2)
        self.assertEqual(self.room_1.songs[1], self.song_2)