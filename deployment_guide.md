# Panduan Deployment IliaChan TechWell 🚀

Dokumen ini berisi panduan langkah demi langkah untuk mengunggah proyek IliaChan TechWell ke GitHub dan melakukan *deploy* (publikasi) secara publik dan gratis menggunakan **Streamlit Community Cloud**, tanpa membocorkan kunci rahasia (*API keys*) di `.env`.

---

## 1. Persiapan Repositori Lokal & Keamanan (`.gitignore`)

Sebelum mengunggah ke GitHub, pastikan file `.env` yang berisi rahasia (API Key Gemini, Groq, Ngrok) **TIDAK** ikut terunggah.

1. Buka file `.gitignore` di folder proyek Anda (buat file baru bernama `.gitignore` jika belum ada).
2. Pastikan baris-baris berikut ada di dalam `.gitignore`:
   ```text
   # Environments
   .env
   __pycache__/
   *.pyc
   .pytest_cache/
   
   # Database
   health_db.sqlite
   
   # Virtual Environment (jika ada)
   venv/
   env/
   .venv/
   ```
   > **PENTING**: Dengan memasukkan `.env` ke `.gitignore`, Git akan mengabaikan file tersebut sehingga API key Anda aman dan tidak akan bocor ke publik.

---

## 2. Mengunggah ke GitHub (Push)

Ikuti langkah ini untuk membuat repositori di GitHub dan mengunggah kode Anda.

### A. Buat Repositori di GitHub
1. Buka [github.com](https://github.com) dan login ke akun Anda.
2. Klik tombol **New** (atau ikon `+` di kanan atas > **New repository**).
3. Isi **Repository name** (misal: `IliaChanTechWell`).
4. Pilih **Public** (agar orang lain bisa melihat).
5. Jangan centang "Add a README file" (karena kita akan push dari komputer).
6. Klik **Create repository**.

### B. Push Kode dari Terminal
Buka terminal (Command Prompt/PowerShell/Terminal VS Code) dan pastikan posisi Anda berada di folder proyek: `c:\Users\febry\Downloads\Folder Baru\IliaChanTechWell\`. Jalankan perintah berikut secara berurutan:

```bash
git init
git add .
git commit -m "Initial commit: IliaChan TechWell Final Project"
git branch -M main
git remote add origin https://github.com/USERNAME_GITHUB_ANDA/IliaChanTechWell.git
git push -u origin main
```
*(Catatan: Ganti `USERNAME_GITHUB_ANDA` dengan username GitHub asli Anda).*

---

## 3. Deploy ke Streamlit Community Cloud

Streamlit Community Cloud adalah platform gratis untuk mempublikasikan aplikasi Streamlit langsung dari GitHub.

### Langkah-langkah:
1. Buka [share.streamlit.io](https://share.streamlit.io/) dan login (bisa langsung "Continue with GitHub").
2. Setelah masuk ke *dashboard*, klik tombol **New app**.
3. Di halaman "Deploy an app", isi formulir berikut:
   - **Repository**: Pilih repositori Anda (misal: `Username/IliaChanTechWell`).
   - **Branch**: Pilih `main`.
   - **Main file path**: Ketik `app.py`.
4. **Jangan klik Deploy dulu!** Kita perlu memasukkan rahasia (Secrets) terlebih dahulu.

### Mengatur Rahasia (Secrets)
Agar aplikasi bisa berjalan (karena file `.env` tidak diunggah), kita harus memasukkan API key langsung ke pengaturan Streamlit Cloud.

1. Pada halaman formulir "Deploy an app" tadi, klik tombol **Advanced settings...** di bagian bawah.
2. Akan muncul sebuah kotak teks bernama **Secrets**.
3. Salin isi dari file `.env` di komputer Anda, lalu *paste* ke dalam kotak Secrets tersebut. Formatnya harus seperti ini:
   ```toml
   GEMINI_API_KEY="AIzaSy..."
   GROQ_API_KEY="gsk_uOq..."
   NGROK_AUTH_TOKEN="3DW09..."
   ```
   *(Catatan: Sebenarnya Ngrok tidak diperlukan jika di-deploy di Streamlit Cloud, tapi boleh tetap dimasukkan agar kode tidak error).*
4. Klik **Save**.
5. Sekarang, klik tombol **Deploy!**

Tunggu beberapa menit. Streamlit akan menginstal dependensi dari `requirements.txt` dan menjalankan `app.py`. Jika berhasil, aplikasi Anda akan live dan mendapatkan URL publik (misal: `https://iliachantechwell.streamlit.app/`).

---

## 4. Menambahkan Link Demo di Halaman About & README GitHub

Saya sudah menambahkan tombol **Live Demo** di halaman About (`pages/4_About.py`). Namun tombol tersebut saat ini masih mengarah ke `#` (belum ada linknya).

Setelah Anda berhasil deploy dan mendapatkan URL dari Streamlit Cloud, Anda perlu mencantumkannya:

### A. Mengupdate Halaman About (pages/4_About.py)
1. Buka file `pages/4_About.py` di VS Code.
2. Cari bagian tombol Live Demo yang kodenya seperti ini:
   ```html
   <a href="#" target="_blank" ...>
   ```
3. Ganti `#` dengan URL Streamlit Anda, misalnya:
   ```html
   <a href="https://iliachantechwell.streamlit.app/" target="_blank" ...>
   ```
4. Simpan file tersebut.

### B. Mengupdate README.md di GitHub
1. Buka atau buat file `README.md` di folder proyek Anda.
2. Tambahkan baris ini di bagian atas:
   ```markdown
   # IliaChan TechWell 🩺
   
   **Live Demo:** [Klik di sini untuk mencoba IliaChan TechWell](https://URL_STREAMLIT_ANDA_DISINI)
   ```

### C. Push Perubahan Terakhir
Jalankan perintah ini di terminal agar perubahan link tersimpan di GitHub dan otomatis ter-update di Streamlit Cloud:
```bash
git add .
git commit -m "Add live demo link"
git push
```
