import pygame
import random

# --- 1. SETUP AWAL ---
pygame.init()
LEBAR = 800
TINGGI = 600
screen = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Game Pantul Bola")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

# --- 2. VARIABEL GAME ---
# A. Raket Pemain (Papan bawah)
paddle_width = 120
paddle_height = 20
paddle_x = LEBAR // 2 - paddle_width // 2
paddle_y = TINGGI - 40
paddle_speed = 10

# B. Bola
ball_size = 20
ball_x = LEBAR // 2
ball_y = TINGGI // 2
# Bola bergerak miring acak
ball_speed_x = 5 * random.choice([1, -1]) 
ball_speed_y = -5 

# C. Skor
score = 0
game_over = False

# --- 3. LOOP GAME ---
running = True
while running:
    # A. Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Fitur Restart kalau Game Over (Tekan Spasi)
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_SPACE:
                # Reset semua variabel
                game_over = False
                score = 0
                ball_x = LEBAR // 2
                ball_y = TINGGI // 2
                ball_speed_y = -5
                ball_speed_x = 5 * random.choice([1, -1])

    if not game_over:
        # B. Gerakan Raket (Kiri-Kanan)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < LEBAR - paddle_width:
            paddle_x += paddle_speed

        # C. Gerakan Bola (Memantul)
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Pantulan Tembok Kiri & Kanan
        if ball_x <= 0 or ball_x >= LEBAR - ball_size:
            ball_speed_x *= -1 # Balik arah horizontal

        # Pantulan Tembok Atas (Langit-langit)
        if ball_y <= 0:
            ball_speed_y *= -1 # Balik arah vertikal

        # D. Logika Kena Raket
        paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
        ball_rect = pygame.Rect(ball_x, ball_y, ball_size, ball_size)

        if ball_rect.colliderect(paddle_rect):
            ball_speed_y *= -1 # Pantulkan ke atas
            score += 1
            # Sedikit persulit: Bola makin cepat tiap kelipatan skor 5
            if score % 5 == 0:
                if ball_speed_x > 0: ball_speed_x += 1
                else: ball_speed_x -= 1

        # E. Cek Kalah (Bola jatuh ke bawah)
        if ball_y > TINGGI:
            game_over = True

    # --- F. GAMBAR LAYAR ---
    screen.fill((50, 0, 50)) # Latar Ungu Gelap

    # Gambar Raket (Cyan)
    pygame.draw.rect(screen, (0, 255, 255), (paddle_x, paddle_y, paddle_width, paddle_height))

    # Gambar Bola (Putih)
    pygame.draw.ellipse(screen, (255, 255, 255), (ball_x, ball_y, ball_size, ball_size))

    # Tampilkan Skor
    text_score = font.render(f"Skor: {score}", True, (255, 255, 255))
    screen.blit(text_score, (10, 10))

    # Pesan Game Over
    if game_over:
        text_kalah = font.render("GAME OVER! Tekan SPASI untuk Ulang", True, (255, 50, 50))
        # Taruh tulisan di tengah layar
        text_rect = text_kalah.get_rect(center=(LEBAR/2, TINGGI/2))
        screen.blit(text_kalah, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()