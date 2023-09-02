

import random

class Playlist:
    def __init__(self):
        self.tracks = []

    def add_song(self, track_path):
        self.tracks.append(track_path)

    def remove_song(self, index):
        if 0 <= index < len(self.tracks):
            del self.tracks[index]

    def get_song(self, index):
        if 0 <= index < len(self.tracks):
            return self.tracks[index]

    def get_song_count(self):
        return len(self.tracks)

    def shuffle(self):
        random.shuffle(self.tracks)


    def clear_playlist(self):
        self.tracks = []
