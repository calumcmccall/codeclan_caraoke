import imp
from this import s
import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room(1)
        self.room_2 = Room(2)

        self.song_1 = Song("Running up that hill", "Kate Bush")
        self.song_2 = Song("Afraid to feel", "LF System")
        self.song_3 = Song("As it was", "Harry Styles")
        self.song_4 = Song("Break my soul", "Beyonce")
        self.song_5 = Song("Green green grass", "George Ezra")

        self.song_playlist = [self.song_1, self.song_2, self.song_3, self.song_4, self.song_5]

        self.room_1.songs.append(self.song_1)

        self.guest_1 = Guest("Max")
        self.guest_2 = Guest("Sarah")
        self.room_1.check_in_guest(self.guest_2)

        self.guest_3 = Guest("Ava")
        self.guest_4 = Guest("Eve")
        self.guest_5 = Guest("Martin")
        self.guest_6 = Guest("Molly")

        self.group = [self.guest_3, self.guest_4, self.guest_5, self.guest_6]


    def test_room_has_room_no(self):
        self.assertEqual(1, self.room_1.room_no)

    def test_add_song_to_room_from_start(self):
        self.assertEqual(self.room_1.songs[0], self.song_1)

    def test_add_song_on_request(self):
        self.room_1.add_song_to_room(self.song_2)
        self.assertEqual(self.room_1.songs[1], self.song_2)

    def test_add_multiple_songs(self):
        self.room_2.add_songs_to_room(self.song_playlist)
        self.assertEqual(5, len(self.room_2.songs))

    def test_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.assertEqual(2, len(self.room_1.guests))

    def test_check_in_guest_already_in_a_room(self):
        self.assertEqual("Guest already checked in", self.room_1.check_in_guest(self.guest_2))

    def test_check_in_group(self):
        self.room_2.check_in_group(self.group)
        self.assertEqual(self.room_2.guests, self.group)

    def test_check_in_group_1_already_in_room(self):
        self.room_2.check_in_guest(self.guest_3)
        self.room_2.check_in_group(self.group)
        self.assertEqual(4, len(self.room_2.guests))

    def test_check_out_guest(self):
        self.room_1.check_out_guest(self.guest_2)
        self.assertEqual(0, len(self.room_1.guests))

    def test_check_out_group(self):
        self.room_2.check_in_group(self.group)
        self.room_2.check_out_group(self.group)
        self.assertEqual(0, len(self.room_2.guests))

    def test_check_out_different_order(self):
        self.room_1.check_in_group(self.group)
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_out_guest(self.guest_4)
        self.assertNotIn(self.guest_4, self.room_1.guests)

    def test_check_out_guest_not_in_room(self):
        self.assertEqual("Guest isn't checked in to this room", self.room_1.check_out_guest(self.guest_5))

    def test_integration_test(self):
        self.room_hip_hop = Room(1)
        self.song_get_it_together = Song("Get it together", "Beastie Boys")
        self.song_through_the_wire = Song("Through the wire", "Kanye West")
        self.hip_hop_playlist = [self.song_get_it_together, self.song_through_the_wire]
        self.guest_tom = Guest("Tom")
        self.guest_mary = Guest("Mary")
        self.tom_and_mary = [self.guest_tom, self.guest_mary]

        self.room_hip_hop.add_songs_to_room(self.hip_hop_playlist)
        self.room_hip_hop.check_in_group(self.tom_and_mary)

        self.assertEqual(2, len(self.room_hip_hop.guests))
        self.assertEqual(2, len(self.room_hip_hop.songs))

        self.guest_ryan = Guest("Ryan")
        self.room_hip_hop.check_in_guest(self.guest_ryan)
        self.song_sweetest_pie = Song("Sweetest pie", "Megan Thee Stallion")
        self.room_hip_hop.add_song_to_room(self.song_sweetest_pie)

        self.assertEqual(3, len(self.room_hip_hop.guests))
        self.assertEqual(3, len(self.room_hip_hop.songs))

        self.room_hip_hop.check_out_guest(self.guest_mary)
        self.assertEqual(2, len(self.room_hip_hop.guests))