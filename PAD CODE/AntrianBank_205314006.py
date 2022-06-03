# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 15:19:19 2022

@author: Gallery
"""
# import module tkinter yang akan digunakan untuk membuat GUI. Module 
# diberi nama alias sebagai tk
import tkinter as tk

# import module numpy yang akan digunakan untuk menyimpan data suhu input
# maupun suhu hasil konversi. Module ini diberi nama alias np
import numpy as np

# import module matplotlib, khususnya submodule pyplot digunakan untuk 
# menampilkan plot dan diberi nama alias plot
import matplotlib.pyplot as plot

# import ttk dan messagebox dari module tkinter
from tkinter import ttk, messagebox

# definisikan variabel global value_cs yang menunjukkan nomor antrian CS, nomor
# ini dimulai dari 0
value_cs = 0
# definisikan variabel global value_teller yang menunjukkan nomor antrian Teller,
# nomor dimulai dari 0
value_teller = 0

# kelas antrianCS digunakan sebagai abstraksi dari antrian CS di dunia nyata.
# Pada kelas ini terdapa konstruktor __init__ dan fungsi tambahCS.
# Pada konstruktor (__init__), nilai max antrian dapat dimasukkan untuk 
# memberikan batasan jumlah antrian CS per harinya
class antrianCS:
    def __init__(self, maxAntrian):
        self.maxAntrian = maxAntrian
    
    # fungsi tambahCS akan mengakses global variabel value_cs dan melakukan 
    # penambahan pada variabel tersebut. Ketika dipanggil, fungsi akan mengem-
    # balikkan variabel globa value_cs yang nilainya telah bertambah
    def tambahCS(self):
        global value_cs
        value_cs = int(value_cs) + 1
        return value_cs
 
# kelas antrianTeller digunakan sebagai abstraksi dari antrian Teller di dunia 
# nyata. Pada kelas ini terdapa konstruktor __init__ dan fungsi tambahTeller.
# Pada konstruktor (__init__), nilai max antrian dapat dimasukkan untuk 
# memberikan batasan jumlah antrian Teller per harinya       
class antrianTeller:
    value_teller = 0
    def __init__(self, maxAntrian):
        self.maxAntrian = maxAntrian
    
    # fungsi tambahTeller akan mengakses global variabel value_teller dan melakukan 
    # penambahan pada variabel tersebut. Ketika dipanggil, fungsi akan mengem-
    # balikkan variabel globa value_teller yang nilainya telah bertambah
    def tambahTeller(self):
        global value_teller
        value_teller = int(value_teller) + 1
        return value_teller

# kelas konterCS digunakan sebagai abstraksi dari konter CS di dunia nyata.
# Terdapat konstruktor (__init__) dan fungsi beriNoKonter. Ketika menginisialisasi
# kelas ini, dibutuhkan parameter berupa no konter dari CS 
class konterCS:
    def __init__(self, noKonter):
        self.noKonter = noKonter
    
    # fungsi beriNoKonter akan mengembalikan nomor konter CS ketika dipanggil
    def getNoKonter(self):
        return self.noKonter

# kelas konterTeller digunakan sebagai abstraksi dari konter Teller di dunia nyata.
# Terdapat konstruktor (__init__) dan fungsi beriNoTeller. Ketika menginisialisasi
# kelas ini, dibutuhkan parameter berupa no konter dari Teller 
class konterTeller:
    def __init__(self, noKonter):
        self.noKonter = noKonter
        
    # fungsi beriNoKonter akan mengembalikan nomor konter Teller ketika dipanggil
    def getNoKonter(self):
        return self.noKonter

# fungsi ini akan menghapus isi dari entry yang menunjukkan nomor antrian,
# sehingga no antrian berikutnya dapat ditampilkan dengan baik
def ulang():
    # perintah ini untuk menghapus kolom entry pada antrian cs, dimana penghapusan
    # dilakukan pada index 0 sampai 50
    cs_entry.delete(0, 50)
    # perintah ini untuk menghapus kolom entry pada antrian teller, dimana 
    # penghapusan dilakukan pada index 0 sampai 50
    teller_entry.delete(0, 50)

# fungsi isiCS() akan menambahkan nilai antrian dan menampilkannya pada entry
# cs serta menanpilkan konter cs yang dapat dituju nasabah
def isiCS():
    # definisikan sebuah variabel untuk menyimpan nilai value_cs yang telah 
    # ditambahkan
    no_cs = antrianCs1.tambahCS()
    # definisikan sebuah variabel no_konter yang merupakan hasil modulo 2 dari
    # no_cs. Hal ini dilakukan agar no_cs yang genap dilayani oleh konter
    # dengan no genap dan sebaliknya. 
    no_konter = int(no_cs) % 2
    # definisikan maxAntrianCS untuk menyimpan nilai max antrian dari objek
    # antrian CS
    maxAntrianCs = antrianCs1.maxAntrian
    
    # selanjutnya, no_cs akan dicek apakah melebihi maxAntrianCs atau tidak
    # jika no_cs masih kurang atau sama dengan max antrian yang diberikan,
    # eksekusi perintah selanjutnya
    if no_cs <= maxAntrianCs:
        # jika no_konter hasil modulo bernilai 0 yang artinya no_cs bernilai 
        # genap, definisikan konterCS yang menyimpan nilai no konter dari objek
        # konterCS2
        if no_konter == 0:
            konterCs = konterCs2.getNoKonter()
        else :
         # jika no_konter hasil modulo tidak bernilai 0 yang artinya no_cs bernilai 
         # ganjil, definisikan konterCS yang menyimpan nilai no konter dari objek
         # konterCS1
            konterCs = konterCs1.getNoKonter()
        # definisikan variabel antrian_cs yang menyimpan gabungan string "CS" 
        # dengan no_cs yang telah dikonversi menjadi string
        antrian_cs = "CS" + str(no_cs)
        # masukkan variabel antrian_cs pada cs_entry dengan perintah insert
        # dengan argumen berupa index dan antrian_cs
        cs_entry.insert(4, antrian_cs)
        # perintah di bawah digunakan untuk menambahkan text pada konterCs_label
        # berupa no konter CS dengan mengkonversi konterCs menjadi string
        konterCs_label['text'] = "Silahkan ke Konter CS - " + str(konterCs)
    else :
        # jika no_cs telah melebihi batas max antrian CS, akan muncul error
        # message dengan pesan bahwa antrian CS habis
        messagebox.showerror("PERINGATAN", "Antrian CS habis!")
    
# fungsi isiTeller() akan menambahkan nilai antrian dan menampilkannya pada entry
# teller serta menanpilkan konter Teller yang dapat dituju nasabah    
def isiTeller():
    # definisikan sebuah variabel untuk menyimpan nilai value_teller yang telah 
    # ditambahkan
    no_teller = antrianTel1.tambahTeller()
    # definisikan sebuah variabel no_konter yang merupakan hasil modulo 2 dari
    # no_teller. Hal ini dilakukan agar no_teller yang genap dilayani oleh konter
    # dengan no genap dan sebaliknya. 
    no_konter = int(no_teller) % 2
    # definisikan maxAntrianTel untuk menyimpan nilai max antrian dari objek
    # antrian Teller
    maxAntrianTel = antrianTel1.maxAntrian
    
    # selanjutnya, no_teller akan dicek apakah melebihi maxAntrianTel atau tidak
    # jika no_teller masih kurang atau sama dengan max antrian yang diberikan,
    # eksekusi perintah selanjutnya
    if no_teller <= maxAntrianTel:
        # jika no_konter hasil modulo bernilai 0 yang artinya no_teller bernilai 
        # genap, definisikan konterTel yang menyimpan nilai no konter dari objek
        # konterTel2
        if no_konter == 0:
            konterTel = konterTel2.getNoKonter()
        else :
         # jika no_konter hasil modulo tidak bernilai 0 yang artinya no_teller bernilai 
         # ganjil, definisikan konterTel yang menyimpan nilai no konter dari objek
         # konterTel1
            konterTel = konterTel1.getNoKonter()
        # definisikan variabel antrian_teller yang menyimpan gabungan string "T" 
        # dengan no_teller yang telah dikonversi menjadi string
        antrian_teller = "T" + str(no_teller)
        # masukkan variabel antrian_teller pada teller_entry dengan perintah insert
        # dengan argumen berupa index dan antrian_teller
        teller_entry.insert(4, antrian_teller)
        # perintah di bawah digunakan untuk menambahkan text pada konterTel_label
        # berupa no konter Teller dengan mengkonversi konterTel menjadi string
        konterTel_label['text'] = "Silahkan ke Konter Teller - " + str(konterTel)
    else :
        # jika no_teller telah melebihi batas max antrian Teller, akan muncul error
        # message dengan pesan bahwa antrian Teller habis
        messagebox.showerror("PERINGATAN", "Antrian Teller habis!")

# Fungsi cetakPlot() digunakan untuk menampilkan bagan pie yang berkaitan dengan
# jumlah antrian CS dan antrian teller
def cetakPlot():
    # definisikan variabel jumlahAntrian yang menyimpan data array berupa 
    # variabel global value_cs dan value_teller, dimana keduanya telah ditambahkan
    # sesuai jumlah antrian masing-masing
    jumlahAntrian = np.array([value_cs, value_teller])
    # definisikan variabel antrianLabel yang digunakan untuk menyimpan label 
    # berupa "Total Antrian CS" dan "Total Antrian Teller"
    antrianLabel  = np.array(["Total Antrian CS", "Total Antrian Teller"])
    # panggil fungsi pie dari variabel plot dengan argumen berupa variabel 
    # jumlahAntrian dan label dari pie yang akan dibentuk
    plot.pie(jumlahAntrian, labels = antrianLabel)
    # bagan pie akan ditampilkan dengan fungsi show( ) dari variabel plot
    plot.show()

# module tkinter yang sudah diimport akan dijadikan variabel bernama 'root'
root = tk.Tk()
# atur panjang dan lebar dari window GUI yang akan dibuat menggunakan
# method geometry. Di sini, window akan memiliki lebar 445 dan lebar 250
root.geometry('445x250')
# atur agar window tidak dapat diubah dengan method resizable dan diberi 
# argumen bernilai false
root.resizable(False, False)
# atur judul pada window dengan method title dan diberi argumen berupa string
root.title('Antrian Bank BNI')
  
# definisikan variabel antrianCs1 dari kelas antrianCS dan memiliki nilai max
# antrian sebesar 25 nomor
antrianCs1  = antrianCS(25) 
# definisikan variabel antrianCs1 dari kelas antrianTeller dan memiliki nilai max
# antrian sebesar 20 nomor
antrianTel1 = antrianTeller(20)
# definisikan variabel konterCs1 dari kelas konterCS dengan no konter yaitu 1
konterCs1 = konterCS(1)
# definisikan variabel konterCs2 dari kelas konterCS dengan no konter yaitu 2
konterCs2 = konterCS(2)
# definisikan variabel konterTel1 dari kelas konterTeller dengan no konter yaitu 1
konterTel1 = konterTeller(1)
# definisikan variabel konterTel2 dari kelas konterTeller dengan no konter yaitu 2
konterTel2 = konterTeller(2)

# definisikan variabel judul_label dengan tipe Label dari variabel ttk. 
# Atur agar labels ditampilkan pada jendela utama yaitu root dengan isi berupa 
# text. Label ini digunakan untuk menunjukkan kegunaan dari GUI ini yaitu antrian
# bank
judul_label = ttk.Label(
    root,
    text='ANTRIAN BANK BRI'
)
# atur letak variabel judul_label dengan fungsi grid. Variabel akan diletakkan
# pada baris 0 dan kolom 1.
judul_label.grid(
    row=0,
    column=1,
    # sticky digunakan ketika tidak ada ruang pada root, label akan diletakkan
    # di bagian utara (north)
    sticky='n',
    # atur label memiliki 10 pixel di luar area label seacara horizontal
    ipadx=10,
    # atur label memiliki 10 pixel di luar area label seacara vertikal
    ipady=10
)

# definisikan variabel value_cs_label dengan tipe Label dari variabel ttk. 
# Atur agar labels ditampilkan pada jendela utama yaitu root dengan isi berupa 
# text. Label ini digunakan untuk menunjukkan nomor antrian cs
value_cs_label = ttk.Label(
    root,
    text='ANTRIAN CS : '
)
# atur letak variabel value_cs_label dengan fungsi grid. Variabel akan diletakkan
# pada baris 1 dan kolom 0.
value_cs_label.grid(
    row=1,
    column=0,
    # sticky digunakan ketika tidak ada ruang pada root, label akan diletakkan
    # di bagian utara (north)
    sticky='n',
    # atur label memiliki 10 pixel di luar area label seacara horizontal
    ipadx=10,
    # atur label memiliki 10 pixel di luar area label seacara vertikal
    ipady=10
)   

# definisikan variabel value_teller_label dengan tipe Label dari variabel ttk. 
# Atur agar label ditampilkan pada jendela utama yaitu root dengan isi berupa 
# text. Label ini digunakan untuk menunjukkan nomor antrian teller
value_teller_label = ttk.Label(
    root,
    text='ANTRIAN TELLER : '
)
# atur letak variabel value_teller_label dengan fungsi grid. Variabel akan diletakkan
# pada baris 1 dan kolom 2.
value_teller_label.grid(
    row=1,
    column=2,
    # sticky digunakan ketika tidak ada ruang pada root, label akan diletakkan
    # di bagian utara (north)
    sticky='n',
    # atur label memiliki 10 pixel di luar area label seacara horizontal
    ipadx=10,
    # atur label memiliki 10 pixel di luar area label seacara vertikal
    ipady=10
)

# definisikan variabel cs_entry dengan tipe Entry dari variabel ttk. 
# Atur agar entry ditampilkan pada jendela utama yaitu root sehingga dapat
# menampilkan nomor antrian cs
cs_entry = ttk.Entry(
    root)
# atur letak variabel cs_entry dengan fungsi grid. Variabel akan diletakkan
# pada baris 2 dan kolom 0.
cs_entry.grid(
    row = 2,
    column = 0)

# definisikan variabel teller_entry dengan tipe Entry dari variabel ttk. 
# Atur agar entry ditampilkan pada jendela utama yaitu root sehingga dapat
# menampilkan nomor antrian teller
teller_entry = ttk.Entry(
    root)
# atur letak variabel teller_entry dengan fungsi grid. Variabel akan diletakkan
# pada baris 2 dan kolom 2.
teller_entry.grid(
    row = 2,
    column = 2)

# definisikan variabel tambah_cs_but dengan tipe Button dari variabel ttk. 
# Atur agar button ini ditampilkan pada jendela utama yaitu root dengan isi berupa 
# text serta memanggil fungsi isiCs()) tiap kali diklik. Button ini akan
# menambahkan nomor antrian cs dan menampilkan nomor tersebut pada kolom
# entry cs
tambah_cs_but = ttk.Button(root, 
            text = "PILIH CS",
            command = isiCS)
# atur letak variabel tambah_cs_but dengan fungsi grid. Variabel akan  
# diletakkan pada baris 4 dan kolom 0.
tambah_cs_but.grid(
    row = 4,
    column = 0)

# definisikan variabel tambah_teller_but dengan tipe Button dari variabel ttk. 
# Atur agar button ini ditampilkan pada jendela utama yaitu root dengan isi berupa 
# text serta memanggil fungsi isiTeller()) tiap kali diklik. Button ini akan
# menambahkan nomor antrian teller dan menampilkan nomor tersebut pada kolom
# entry teller
tambah_teller_but = ttk.Button(root, 
            text = "PILIH TELLER",
            command = isiTeller)
# atur letak variabel tambah_teller_but dengan fungsi grid. Variabel akan  
# diletakkan pada baris 4 dan kolom 2.
tambah_teller_but.grid(
    row = 4,
    column = 2)

# definisikan variabel konterCs_label dengan tipe Label dari variabel ttk. 
# Atur agar label ditampilkan pada jendela utama yaitu root dengan isi berupa 
# text. Label ini digunakan untuk menunjukkan konter cs dari no antrian cs
konterCs_label = ttk.Label(
    root,
    text= "Silahkan ke konter CS"
)
# atur letak variabel konterCs_label dengan fungsi grid. Variabel akan diletakkan
# pada baris 6 dan kolom 0.
konterCs_label.grid(
    row=6,
    column=0,
    # sticky digunakan ketika tidak ada ruang pada root, label akan diletakkan
    # di bagian selatan (south)
    sticky='s',
    # atur label memiliki 10 pixel di luar area label seacara horizontal
    ipadx=10,
    # atur label memiliki 10 pixel di luar area label seacara vertikal
    ipady=10
)

# definisikan variabel konterTel_label dengan tipe Label dari variabel ttk. 
# Atur agar label ditampilkan pada jendela utama yaitu root dengan isi berupa 
# text. Label ini digunakan untuk menunjukkan konter teller dari no antrian teller
konterTel_label = ttk.Label(
    root,
    text= "Silahkan ke konter Teller"
)
# atur letak variabel konterTel_label dengan fungsi grid. Variabel akan diletakkan
# pada baris 6 dan kolom 2.
konterTel_label.grid(
    row=6,
    column=2,
    # sticky digunakan ketika tidak ada ruang pada root, label akan diletakkan
    # di bagian selatan (south)
    sticky='s',
    # atur label memiliki 10 pixel di luar area label seacara horizontal
    ipadx=10,
    # atur label memiliki 10 pixel di luar area label seacara vertikal
    ipady=10
)

# definisikan variabel print_but dengan tipe Button dari variabel ttk. 
# Atur agar button ini ditampilkan pada jendela utama yaitu root dengan isi berupa 
# text serta memanggil fungsi ulang()) tiap kali diklik. Button akan mengosongkan
# kedua kolom entry dan antrian dapat ditambahkan kembali
print_but = ttk.Button(root, 
            text = "CETAK NO ANTRIAN",
            command = ulang)
# atur letak variabel print_but_but dengan fungsi grid. Variabel akan  
# diletakkan pada baris 8 dan kolom 1.
print_but.grid(
    row = 8,
    column = 1)

# definisikan variabel close_but dengan tipe Button dari variabel ttk. 
# Atur agar button ini ditampilkan pada jendela utama yaitu root dengan isi berupa 
# text serta memanggil fungsi cetakPlot()) tiap kali diklik. Button ini akan 
# menampilkan bagan pie dari jumlah total kedua antrian
close_but = ttk.Button(root, 
            text = "TUTUP ANTRIAN",
            command = cetakPlot)
# atur letak variabel close_but dengan fungsi grid. Variabel akan  
# diletakkan pada baris 9 dan kolom 1.
close_but.grid(
    row = 9,
    column = 1)

# code diakhir dengan memanggil fungsi mainloop() dari variabel root agar
# tkinter dapat berjalan dan menampilkan GUI
root.mainloop()

