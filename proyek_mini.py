import tkinter as tk
from tkinter import filedialog, messagebox
from pydub import AudioSegment
import winsound  # Alat bantu agar Windows mau bersuara
import os

# --- LOGIKA PROGRAM ---
global file_path
file_path = "" # Variabel untuk menyimpan lokasi lagu

def pilih_lagu():
    global file_path
    # Membuka jendela pilih file
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    
    if file_path:
        # Menampilkan nama file di layar (ambil nama file saja, bukan folder panjangnya)
        nama_lagu = os.path.basename(file_path)
        label_status.config(text=f"Lagu Terpilih: {nama_lagu}", fg="blue")
    else:
        label_status.config(text="Belum ada lagu yang dipilih", fg="red")

def putar_musik():
    global file_path
    if not file_path:
        messagebox.showwarning("Peringatan", "Pilih lagu dulu dong!")
        return

    try:
        label_status.config(text="Sedang Memutar... 🎵", fg="green")
        root.update() # Update layar biar tulisan muncul dulu baru lagu main
        
        # 1. GUNAKAN PYDUB (Sesuai tugas)
        # Kita load lagunya pakai Pydub
        lagu = AudioSegment.from_file(file_path)
        
        # 2. KONVERSI KE WAV BERSIH (Solusi Error Permission Windows)
        temp_file = "temp_now_playing.wav"
        lagu.export(temp_file, format="wav")
        
        # 3. PUTAR (Pakai Winsound biar lancar)
        # SND_ASYNC = Biar aplikasi tidak macet saat lagu main
        winsound.PlaySound(temp_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
        
    except Exception as e:
        messagebox.showerror("Error", f"Gagal memutar: {e}")

def stop_musik():
    # Menghentikan suara
    winsound.PlaySound(None, winsound.SND_PURGE)
    label_status.config(text="Musik Dihentikan", fg="red")

# --- TAMPILAN ANTARMUKA (GUI TKINTER) ---
root = tk.Tk()
root.title("Aplikasi Pemutar Musik Sederhana")
root.geometry("400x300")
root.configure(bg="#f0f0f0") # Warna background abu-abu muda

# Judul Aplikasi
judul = tk.Label(root, text="🎵 Music Player Pro 🎵", font=("Arial", 16, "bold"), bg="#f0f0f0")
judul.pack(pady=20)

# Tombol Pilih Lagu
btn_pilih = tk.Button(root, text="📂 Pilih File Audio", command=pilih_lagu, width=20, bg="white")
btn_pilih.pack(pady=5)

# Label Status Lagu
label_status = tk.Label(root, text="Silakan pilih lagu...", font=("Arial", 10), bg="#f0f0f0")
label_status.pack(pady=20)

# Frame untuk Tombol Kontrol (Play & Stop)
frame_kontrol = tk.Frame(root, bg="#f0f0f0")
frame_kontrol.pack(pady=10)

btn_play = tk.Button(frame_kontrol, text="▶ PUTAR", command=putar_musik, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=10)
btn_play.pack(side=tk.LEFT, padx=10)

btn_stop = tk.Button(frame_kontrol, text="⏹ STOP", command=stop_musik, bg="#f44336", fg="white", font=("Arial", 10, "bold"), width=10)
btn_stop.pack(side=tk.LEFT, padx=10)

# Footer
footer = tk.Label(root, text="Dibuat dengan Python Tkinter & Pydub", font=("Arial", 8), bg="#f0f0f0", fg="gray")
footer.pack(side=tk.BOTTOM, pady=10)

# Jalankan Aplikasi
root.mainloop()