from flask import Flask,request, redirect, url_for, render_template
import os # Diperlukan untuk menyimpan file
import time # Diperlukan untuk membuat timestamp

# Membuat Objek
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'kasus template/static/uploads/'

# Route utama
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/fakultas')
def fakultas():
    fakultas = ["FIKR", "FEB"]
    return render_template ('fakultas.html', fakultas=fakultas)

@app.route('/prodi')
def prodi():
    prodi = [
        {"nama": "Informatika", "fakultas": "FIKR"},
        {"nama": "Sistem Informsi", "fakultas": "FIKR"},
        {"nama": "Akuntasi", "fakultas": "FEB"},
    ]
    return render_template ('prodi.html', prodi=prodi)

@app.route('/hubungiKami', methods = ['GET', 'POST'])
def hubungiKami():
    if request.method == 'POST':
        nama = request.form['nama'],
        email = request.form['email'],
        pesan = request.form['pesan'],
        #tampilkan di terminal
        print(f"Nama : {nama}, Email: {email}, Pesan: {pesan}")

     #pesan konfirmasi 
        pesan_konfirmasi = f"Halo {nama}, data anda berhasil dikirim"
        return render_template('hubungiKami.html', nama=nama, email=email,pesan = pesan, pesan_konfirmasi=pesan_konfirmasi)

    return render_template ('hubungiKami.html')


@app.route('/registrasi', methods = ['GET', 'POST'])
def registrasi():
    if request.method == 'POST':
        nisn = request.form['nisn']
        nama = request.form['nama'],
        email = request.form['email'],
        tglLahir = request.form['tglLahir'],
        asalSekolah = request.form['asalSekolah'],
        pilihanProgramStudi = request.form['pilihanProgramStudi'],

         # Cek jika ada file yang diunggah
        foto = request.files['foto']
        if foto:
            # Mengambil timestamp saat ini untuk menambahkan ke nama file
            timestamp = str(int(time.time()))
         # Mengambil ekstensi file asli
            ext = foto.filename.split('.')[-1]

            # Menambahkan ekstensi ke nama file unik
            unique_filename = f"{timestamp}.{ext}"

          # Menyimpan file dengan nama unik
            foto_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            foto.save(foto_path)
            foto_path = f'uploads/{unique_filename}'  # Menyimpan path relatif dengan menggunakan '/uploads/'
        else:
            foto_path = None

        #tampilkan di terminal
        # print(f"NISN : {nisn}, Nama : {nama}, Email: {email}, tglLahir: {tglLahir}, Asal Sekolah: {asalSekolah}, Pilihan Program Studi: {pilihanProgramStudi}, foto: {foto}")

     #pesan konfirmasi 
        pesan_konfirmasi = f"Terimah Kasih {nama}, Anda telah mendaftarkan diri di Universitas MDP"
        return render_template('registrasi.html',nisn=nisn,nama=nama,email=email,tglLahir=tglLahir,asalSekolah=asalSekolah,pilihanProgramStudi=pilihanProgramStudi, pesan_konfirmasi=pesan_konfirmasi, foto=foto_path)
    
    return render_template("registrasi.html")

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)