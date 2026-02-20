import cv2

# Masukkan nama file video Anda di sini (beserta ekstensinya .mp4, .avi, dll)
video_path = 'video.mp4' 
cap = cv2.VideoCapture(video_path)

# Cek apakah file video berhasil dibuka
if not cap.isOpened():
    print("Error: Video tidak ditemukan atau format tidak didukung")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    
    # Jika ret False, berarti video sudah habis
    if not ret:
        print("Video selesai atau tidak ada frame lagi.")
        break

    # --- PROSES VIDEO (Contoh: Negative Effect) ---
    negative_frame = 255 - frame

    # Tampilkan hasil
    cv2.imshow('Hasil Pemrosesan Video', negative_frame)

    # Atur kecepatan putar (25ms standar untuk 40fps, sesuaikan jika perlu)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()