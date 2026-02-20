import pygame
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
import winsound # Tambahan wajib buat laptopmu biar gak error permission
import os

# --- TAHAP 1: Setup Awal ---
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game - Tahap 1")

# Loop Tahap 1 (Layar Kosong)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

# --- TAHAP 2: Menampilkan Gambar ---
# Memuat gambar
# Pastikan ada file 'image.png'
try:
    image = pygame.image.load('image.png')
except:
    image = pygame.Surface((50,50)) # Kotak pengganti kalau gambar gak ada

pygame.display.set_caption("Simple Game - Tahap 2 (Gambar)")

# Loop Tahap 2 (Gambar Diam)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0)) # Layar hitam
    screen.blit(image, (100, 100)) # Gambar diam
    pygame.display.flip()

# --- TAHAP 3: Suara & Animasi ---
# Memuat suara (Perbaiki typo 'reult' jadi 'result')
if os.path.exists('result.wav'):
    sound = pygame.mixer.Sound('result.wav')
    sound.play()
elif os.path.exists('reult.wav'):
    sound = pygame.mixer.Sound('reult.wav')
    sound.play()

pygame.display.set_caption("Simple Game - Tahap 3 (Animasi)")

# Loop Tahap 3 (Animasi Bergerak)
x = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += 5
    if x > 800:
        x = 0

    screen.fill((0, 0, 0))
    screen.blit(image, (x, 100))
    pygame.display.flip()

# Menutup Pygame sebelum masuk ke Tkinter
pygame.quit()

# --- TAHAP 4: Music Player (Tkinter) ---
# Membuat jendela utama
root = tk.Tk()
root.title("Music Player")

# Fungsi memutar musik (Disini kita pakai trik winsound agar tidak error di laptopmu)
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Code dosen pakai: play(audio) 
        # Kita ganti pakai winsound karena pydub error di laptopmu
        audio = AudioSegment.from_file(file_path)
        audio.export("temp_lagu.wav", format="wav")
        winsound.PlaySound("temp_lagu.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

# Membuat tombol play
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack(pady=20)

# Menjalankan Tkinter
root.mainloop()