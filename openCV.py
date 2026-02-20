import cv2

# Membaca gambar
image = cv2.imread("image.jpg")

if image is not None:
    resized = cv2.resize(image, (300, 200))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    cv2.imwrite("opencv_gray.jpg", gray)
    cv2.imwrite("opencv_edges.jpg", edges)
else:
    print("Gambar tidak ditemukan")