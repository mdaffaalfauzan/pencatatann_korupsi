import csv


data_korupsi = []

korupsi_by_nama = {}

FILE_NAME = "data_korupsi.csv"


def load_data():
    try:
        with open(FILE_NAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data_korupsi.append(row)
                korupsi_by_nama[row['Nama']] = row
    except FileNotFoundError:
        pass

def save_data():
    with open(FILE_NAME, mode='w', newline='') as file:
        fieldnames = ['Nama', 'Instansi', 'Status', 'Tahun', 'Nominal']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for data in data_korupsi:
            writer.writerow(data)

def tambah_data():
    nama = input("Masukkan nama: ")
    instansi = input("Masukkan instansi: ")
    status = input("Masukkan status (pejabat/non pejabat): ")
    tahun = input("Masukkan tahun: ")
    nominal = input("Masukkan nominal (Rp): ")  
    data = {'Nama': nama, 'Instansi': instansi, 'Status': status, 'Tahun': tahun, 'Nominal': nominal}
    data_korupsi.append(data)
    korupsi_by_nama[nama] = data
    print("Data berhasil ditambahkan.\n")

def ubah_data():
    nama = input("Masukkan nama yang datanya ingin diubah: ")
    if nama in korupsi_by_nama:
        print("Masukkan data baru (biarkan kosong jika tidak ingin diubah):")
        data = korupsi_by_nama[nama]
        instansi = input(f"Instansi [{data['Instansi']}]: ") or data['Instansi']
        status = input(f"Status [{data['Status']}]: ") or data['Status']
        tahun = input(f"Tahun [{data['Tahun']}]: ") or data['Tahun']
        nominal = input(f"Nominal [{data['Nominal']}]: ") or data['Nominal']

        data.update({'Instansi': instansi, 'Status': status, 'Tahun': tahun, 'Nominal': nominal})
        print("Data berhasil diperbarui.\n")
    else:
        print("Data tidak ditemukan.\n")

def hapus_data():
    nama = input("Masukkan nama yang datanya ingin dihapus: ")
    if nama in korupsi_by_nama:
        data_korupsi.remove(korupsi_by_nama[nama])
        del korupsi_by_nama[nama]
        print("Data berhasil dihapus.\n")
    else:
        print("Data tidak ditemukan.\n")

def sortir_berdasarkan_tahun():
    tahun = input("Masukkan tahun yang ingin dicari: ")
    hasil = [d for d in data_korupsi if d['Tahun'] == tahun]
    if hasil:
        print("Data pada tahun", tahun)
        for d in hasil:
            print(d)
    else:
        print("Tidak ada data untuk tahun tersebut.")
    print()

def lihat_data():
    if not data_korupsi:
        print("Belum ada data.")
    for d in data_korupsi:
        print(d)
    print()

def menu():
    while True:
        print("\n=== SISTEM PENCATATAN DATA KORUPSI INDONESIA ===")
        print("1. Tambah Data Korupsi")
        print("2. Ubah Data Korupsi")
        print("3. Hapus Data Korupsi")
        print("4. Sortir Data Berdasarkan Tahun")
        print("5. Lihat Semua Data")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            ubah_data()
        elif pilihan == '3':
            hapus_data()
        elif pilihan == '4':
            sortir_berdasarkan_tahun()
        elif pilihan == '5':
            lihat_data()
        elif pilihan == '6':
            save_data()
            print("Data disimpan. Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.\n")

load_data()
menu()
