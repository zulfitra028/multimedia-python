import pygame
import random # Kita butuh ini untuk posisi acak koin

# --- 1. SETUP AWAL (JANGAN DIUBAH) ---
pygame.init()
LEBAR_LAYAR = 800
TINGGI_LAYAR = 600
screen = pygame.display.set_mode((LEBAR_LAYAR, TINGGI_LAYAR))
pygame.display.set_caption("Game Pemburu Koin Sederhana")

# Jam untuk mengatur kecepatan game (FPS)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30) # Font untuk skor

# --- 2. VARIABEL GAME ---
# A. Pemain (Kotak Biru)
player_size = 50
player_x = LEBAR_LAYAR // 2
player_y = TINGGI_LAYAR // 2
player_speed = 5

# B. Musuh (Kotak Merah)
enemy_size = 50
enemy_x = random.randint(0, LEBAR_LAYAR - enemy_size)
enemy_y = random.randint(0, TINGGI_LAYAR - enemy_size)
enemy_speed_x = 4
enemy_speed_y = 4

# C. Koin (Lingkaran Kuning)
coin_size = 20
coin_x = random.randint(50, LEBAR_LAYAR - 50)
coin_y = random.randint(50, TINGGI_LAYAR - 50)

# D. Skor
score = 0

# --- 3. LOOP UTAMA ---
running = True
while running:
    # --- A. EVENT LISTENER (INPUT) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- B. PERGERAKAN PEMAIN ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < LEBAR_LAYAR - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < TINGGI_LAYAR - player_size:
        player_y += player_speed

    # --- C. PERGERAKAN MUSUH (Otomatis) ---
    enemy_x += enemy_speed_x
    enemy_y += enemy_speed_y

    # Pantulkan musuh jika kena tembok
    if enemy_x <= 0 or enemy_x >= LEBAR_LAYAR - enemy_size:
        enemy_speed_x *= -1 # Balik arah horizontal
    if enemy_y <= 0 or enemy_y >= TINGGI_LAYAR - enemy_size:
        enemy_speed_y *= -1 # Balik arah vertikal

    # --- D. LOGIKA TABRAKAN (COLLISION) ---
    # Kita buat kotak imajiner (Rect) untuk mendeteksi sentuhan
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
    coin_rect = pygame.Rect(coin_x, coin_y, coin_size*2, coin_size*2)

    # 1. Kalau Kena Koin
    if player_rect.colliderect(coin_rect):
        score += 1
        # Pindah koin ke tempat acak baru
        coin_x = random.randint(50, LEBAR_LAYAR - 50)
        coin_y = random.randint(50, TINGGI_LAYAR - 50)
        # Tambah kecepatan musuh sedikit biar makin susah
        if enemy_speed_x > 0: enemy_speed_x += 0.5
        else: enemy_speed_x -= 0.5

    # 2. Kalau Kena Musuh
    if player_rect.colliderect(enemy_rect):
        print("GAME OVER! Skor Akhir:", score)
        running = False # Tutup game

    # --- E. MENGGAMBAR (DRAWING) ---
    screen.fill((30, 30, 30)) # Latar belakang abu-abu gelap

    # Gambar Pemain (Biru)
    pygame.draw.rect(screen, (0, 128, 255), player_rect)
    
    # Gambar Musuh (Merah)
    pygame.draw.rect(screen, (255, 50, 50), enemy_rect)

    # Gambar Koin (Kuning)
    pygame.draw.circle(screen, (255, 215, 0), (coin_x + 10, coin_y + 10), coin_size)

    # Tampilkan Skor
    text_score = font.render(f"Skor: {score}", True, (255, 255, 255))
    screen.blit(text_score, (10, 10))

    # --- F. UPDATE TAMPILAN ---
    pygame.display.flip()
    
    # Batasi kecepatan game (60 Frame per detik) agar tidak terlalu cepat
    clock.tick(60) 

pygame.quit()