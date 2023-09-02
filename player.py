import pygame

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()

    def load_track(self, track_path):
        pygame.mixer.music.load(track_path)

    def play(self):
        pygame.mixer.music.play()

    def pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()

    def is_playing(self):
        return pygame.mixer.music.get_busy()
