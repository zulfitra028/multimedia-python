import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("Multimedia Application")

#Menampilkan Gambar
from PIL import Image, ImageTk

# Memuat gambar menggunakan Pillow
image = Image.open('cropped_result.jpg')
photo = ImageTk.PhotoImage(image)

# Membuat label untuk menampilkan gambar
label = tk.Label(root, image=photo)
label.pack()

#Menampilkan Audio
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play
import winsound

# Definisikan fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)
       # play(audio)
       #saya ganti ini dikarnakan tidak bisa menginstall simpleaudio
        audio.export("temp_lagu.wav", format="wav")
        winsound.PlaySound("temp_lagu.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

# Membuat tombol untuk memutar musik
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

# Menjalankan loop acara Tkinter
root.mainloop()