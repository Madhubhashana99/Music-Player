import tkinter as tk
from tkinter import filedialog  # Import filedialog separately
import os
import random
from player import MusicPlayer
from playlist import Playlist

class MusicPlayerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Music Player")

        self.player = MusicPlayer()
        self.playlist = Playlist()

        self.initialize_ui()

    def initialize_ui(self):
        # Create and arrange GUI elements here (buttons, playlist view, etc.)

        # Create a listbox to display the playlist
        self.playlist_box = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.playlist_box.pack(pady=20)

        # Create buttons for controls (Play, Pause, Stop, Next, Previous)
        play_button = tk.Button(self.root, text="Play", command=self.play_music)
        pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        next_button = tk.Button(self.root, text="Next", command=self.next_music)
        prev_button = tk.Button(self.root, text="Previous", command=self.prev_music)

        play_button.pack()
        pause_button.pack()
        stop_button.pack()
        next_button.pack()
        prev_button.pack()

        # Create a button to add songs to the playlist
        add_button = tk.Button(self.root, text="Add Song", command=self.add_song)
        add_button.pack()

        # Create a button to remove songs from the playlist
        remove_button = tk.Button(self.root, text="Remove Song", command=self.remove_song)
        remove_button.pack()

    def play_music(self):
        selected_index = self.playlist_box.curselection()
        if selected_index:
            selected_index = selected_index[0]
            selected_song = self.playlist.get_song(selected_index)

            if selected_song:
                if not self.player.is_playing():
                    self.player.load_track(selected_song)  # Load the selected song
                    self.player.play()  # Play the loaded track

    def pause_music(self):
        if self.player.is_playing():
            self.player.pause()  # Assuming you have a pause method in your MusicPlayer class

    def stop_music(self):
        if self.player.is_playing():
            self.player.stop()  # Assuming you have a stop method in your MusicPlayer class

    def next_music(self):
        current_index = self.playlist_box.curselection()
        if current_index:
            current_index = current_index[0]
            next_index = (current_index + 1) % len(self.playlist.tracks)
            self.playlist_box.selection_clear(current_index)
            self.playlist_box.selection_set(next_index)
            self.playlist_box.see(next_index)
            self.play_music()

    def prev_music(self):
        current_index = self.playlist_box.curselection()
        if current_index:
            current_index = current_index[0]
            prev_index = (current_index - 1) % len(self.playlist.tracks)
            self.playlist_box.selection_clear(current_index)
            self.playlist_box.selection_set(prev_index)
            self.playlist_box.see(prev_index)
            self.play_music()

    def add_song(self):
        file_path = filedialog.askopenfilename(title="Select a song", filetypes=[("Audio files", "*.mp3 *.wav")])
        if file_path:
            self.playlist.add_song(file_path)  # Assuming you have a method to add songs to your playlist
            song_name = os.path.basename(file_path)
            self.playlist_box.insert(tk.END, song_name)

    def remove_song(self):
        selected_index = self.playlist_box.curselection()
        if selected_index:
            selected_index = selected_index[0]
            self.playlist.remove_song(
                selected_index)  # Assuming you have a method to remove a song by index from your playlist
            self.playlist_box.delete(selected_index)

    def run(self):
        self.root.mainloop()

# Entry point
if __name__ == "__main__":
    app = MusicPlayerGUI()
    app.run()
