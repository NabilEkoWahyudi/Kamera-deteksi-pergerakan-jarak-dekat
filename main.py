import cv2
import numpy as np

net = cv2.dnn.readNetFromCaffe(
    "deploy.prototxt",
    "res10_300x300_ssd_iter_140000.caffemodel"
)

CLASSES = ["background", "person", "bicycle", "car", "motorbike", "aeroplane", 
           "bus", "train", "truck", "boat", "traffic light", "fire hydrant", 
           "stop sign", "bench", "bird", "cat", "dog"]

# Inisialisasi kamera
cap = cv2.VideoCapture(0)

# Baca frame pertama sebagai referensi
ret, frame1 = cap.read()
frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
frame1_gray = cv2.GaussianBlur(frame1_gray, (21, 21), 0)

while True:
    ret, frame2 = cap.read()
    if not ret:
        break

    # Konversi ke grayscale
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    frame2_gray = cv2.GaussianBlur(frame2_gray, (21, 21), 0)

    # Hitung perbedaan antara frame awal dan frame sekarang
    diff = cv2.absdiff(frame1_gray, frame2_gray)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    # Fokus hanya di area tengah (radius jarak dekat simulasi)
    h, w = thresh.shape
    roi = thresh[int(h/3):int(2*h/3), int(w/3):int(2*w/3)]

    # Cari kontur di area ROI
    contours, _ = cv2.findContours(roi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c) > 500:  # Batas minimum deteksi gerakan
            print("Gerakan terdeteksi di jarak dekat!")
            cv2.rectangle(frame2, 
                          (int(w/3), int(h/3)), 
                          (int(2*w/3), int(2*h/3)), 
                          (0, 0, 255), 2)

    # Tampilkan hasil
    cv2.imshow("Kamera", frame2)
    cv2.imshow("Deteksi Gerakan", thresh)

    frame1_gray = frame2_gray  # Update frame referensi

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()