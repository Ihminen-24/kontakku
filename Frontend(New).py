import tkinter as tk
from tkinter import messagebox, ttk

import Backend


# Function Refresh
def muat_tabel_gui():
    for item in list_kontak.get_children():
        list_kontak.delete(item)

    for kontak in Backend.daftar_kontak:
        list_kontak.insert("", tk.END, values=(kontak["Nama"], kontak["Nomor"]))


# Window
window = tk.Tk()
window.title("Kontakku V0.1")
window.geometry("600x400")
window.resizable(False, False)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
# Frame
frame_kanan = ttk.Frame(window)
frame_kanan.grid(row=0, column=1, sticky="nsew")
frame_kanan.rowconfigure(0, weight=1)
frame_kanan.columnconfigure(0, weight=1)
frame_kiri = ttk.Frame(window)
frame_kiri.grid(row=0, column=0, sticky="nsew")
# Label
label_nama = ttk.Label(frame_kiri, text="Nama")
label_nama.grid(row=0, column=0)
label_nomor = ttk.Label(frame_kiri, text="Nomor")
label_nomor.grid(row=2, column=0)
# Entry
input_nama = ttk.Entry(frame_kiri)
input_nama.grid(row=1, column=0, pady=5, padx=10)
input_nomor = ttk.Entry(frame_kiri)
input_nomor.grid(row=3, column=0, pady=5, padx=10)
# Treeview
list_kontak = ttk.Treeview(frame_kanan, columns=("Nama", "Nomor"))
list_kontak.heading("Nama", text="Nama Kontak")
list_kontak.heading("Nomor", text="Nomor Kontak")
list_kontak.grid(row=0, column=0, padx=10, pady=10)
list_kontak.column("#0", width=0, stretch=False)
list_kontak.column("Nama", width=150)
list_kontak.column("Nomor", width=150)


# Function Tambahkan Kontak
def tambah_kontak_gui():
    nama = input_nama.get()
    nomor = input_nomor.get()

    if nama == "" or nomor == "":
        messagebox.showerror(title="Error", message="Harus di Isi")
        return

    respon = Backend.tambah_kontak(nama, nomor)

    if respon == "Kontak Berhasil dimasukkan":
        muat_tabel_gui()
        messagebox.showinfo(
            title="Info Mas`e", message="Berhasil dimasukkan ke Kontakku"
        )
    else:
        messagebox.showerror(title="Failed", message=respon)

    muat_tabel_gui()

    input_nama.delete(0, tk.END)
    input_nomor.delete(0, tk.END)


# Button Input Kontak
button_input = ttk.Button(
    frame_kiri, text="Tambahkan ke Kontakku", command=tambah_kontak_gui
)
button_input.grid(row=4, column=0, pady=5, padx=10)


# Function Hapus Kontak
def hapus_kontak_gui():
    item_terpilih = list_kontak.selection()

    if not item_terpilih:
        messagebox.showwarning(
            title="Warning", message="Pilih Kontak yang ingin dihapus"
        )
        return

    target_item = item_terpilih[0]
    indeks_angka = list_kontak.index(target_item)

    respon = Backend.hapus_kontak(indeks_angka)

    if respon == "Kontak Berhasildi hapus":
        muat_tabel_gui()
        messagebox.showinfo(title="Sukses", message=respon)
    else:
        messagebox.showerror(title="Gagal", message=respon)

    muat_tabel_gui()


# Button Hapus Kontak
button_hapus = ttk.Button(
    frame_kiri, text="Hapus dari Kontakku", command=hapus_kontak_gui
)
button_hapus.grid(row=5, column=0, pady=5, padx=10)

# Function Search Kontak

def search_kontak_gui():
    kata_kunci = input_cari.get()

    if kata_kunci == "":
        messagebox.showerror(title="Error", message="Harus Masukkan Kontak yang dicari")
        return

    hasil = Backend.search_kontak(kata_kunci)

    for item in list_kontak.get_children():
        list_kontak.delete(item)
    for hasil in
        hasil.insert("", tk.END, values=(kontak["Nama"],kontak["Nomor"]))

def reset_cari_gui():
    input_cari




muat_tabel_gui()
window.mainloop()
