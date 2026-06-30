import json

daftar_kontak = []


def search_kontak(kata_kunci):
    hasil_pencarian = []
    for kontak in daftar_kontak:
        if kata_kunci.lower() in kontak["Nama"].lower():
            hasil_pencarian.append(kontak)

    return hasil_pencarian


def muat_kontak():
    global daftar_kontak

    try:
        with open("Kontak.json", "r") as file:
            daftar_kontak = json.load(file)
        daftar_kontak.sort(key=lambda x: x["Nama"].lower())
    except FileNotFoundError:
        pass


def tambah_kontak(nama, nomor):
    # Validation Kosong
    if nama == "" or nomor == "":
        return "Data Tidak Boleh Kosong"
    # Validation Tipe data int
    if not nomor.isdigit():
        return "Nomor harus Angka"
    # Validation Data Duplikat
    for kontak in daftar_kontak:
        if str(kontak["Nomor"]) == nomor:
            return "Nomor tidak boleh sama"
    #
    dict_kontak = {"Nama": nama, "Nomor": nomor}
    daftar_kontak.append(dict_kontak)
    #
    daftar_kontak.sort(key=lambda x: x["Nama"].lower())
    with open("Kontak.json", "w") as file:
        json.dump(daftar_kontak, file)

    return "Kontak Berhasil dimasukkan"


def hapus_kontak(indeks):
    if indeks < 0 or indeks >= len(daftar_kontak):
        return "Gagal: Kontak tidak ditemukan!"
    del daftar_kontak[indeks]
    with open("Kontak.json", "w") as file:
        json.dump(daftar_kontak, file)

    return "Kontak Berhasil di hapus"


def edit_kontak(indeks, nomor_baru, nama_baru):
    if nama_baru == "" or nomor_baru == "":
        return "Masukkan Nama dan Nomor yang baru"
    if indeks < 0 or indeks >= len(daftar_kontak):
        return "Gagal: Kontak tidak ditemukan!"
    try:
        nomor_baru = int(nomor_baru)
    except ValueError:
        return "Nomor harus angka"

    for kontak in range(len(daftar_kontak)):
        nomor_database = daftar_kontak[kontak]["Nomor"]
        if (kontak != indeks) and (nomor_database == nomor_baru):
            return "Kontak Sudah di pakai orang lain"
    dict_kontak_baru = {"Nama": nama_baru, "Nomor": nomor_baru}
    daftar_kontak[indeks] = dict_kontak_baru
    daftar_kontak.sort(key=lambda x: x["Nama"].lower())
    with open("Kontak.json", "w") as file:
        json.dump(daftar_kontak, file)

    return "Kontak Berhasil di ubah"


muat_kontak()
