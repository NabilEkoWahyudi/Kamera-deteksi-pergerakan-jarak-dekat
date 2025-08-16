# 🔍 Sistem Pendeteksi Pergerakan Jarak Dekat Berbasis Kamera

## 📝 Ringkasan
Proyek ini adalah aplikasi **Computer Vision** berbasis **Python + OpenCV** yang dapat mendeteksi **pergerakan objek** dalam jangkauan kamera, sekaligus mengidentifikasi entitas (manusia, kendaraan, hewan, dll.) menggunakan model **MobileNet SSD**.  

Sistem dilengkapi dengan **radius deteksi jarak dekat** (lingkaran di tengah layar). Jika objek yang bergerak terdeteksi berada di dalam radius tersebut, sistem akan memberikan label khusus `[DEKAT]`.  

---

## ⚙️ Fitur Utama
- **Deteksi Pergerakan**  
  - Menggunakan perbedaan frame (frame differencing dengan `cv2.absdiff`).  
  - Identifikasi entitas hanya dilakukan jika terdapat gerakan → lebih efisien.  

- **Deteksi Objek & Identifikasi Entitas**  
  - Menggunakan model **MobileNet SSD (Caffe)** untuk mengenali objek umum:  
    - `person` (manusia)  
    - `car`, `bus`, `truck` (kendaraan)  
    - `cat`, `dog` (hewan peliharaan)  
    - dll.  

- **Radius Jarak Dekat**  
  - Lingkaran radius digambar di tengah layar.  
  - Objek yang masuk area radius ditandai `[DEKAT]` dengan warna merah.  

- **Visualisasi Real-time**  
  - Bounding box objek + confidence score.  
  - Lingkaran radius.  
  - Label entitas + status `[DEKAT]` bila terdeteksi di radius.  

---

## 🚀 Instalasi & Menjalankan
### 1. Clone repository & masuk ke folder proyek
```bash
git clone https://github.com/NabilEkoWahyudi/Kamera-deteksi-pergerakan-jarak-dekat.git
cd Camera_Project
python3 main.py

