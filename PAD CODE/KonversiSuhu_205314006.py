# import module tkinter yang akan digunakan untuk membuat GUI. Module 
# diberi nama alias sebagai tk
import tkinter as tk

# import module numpy yang akan digunakan untuk menyimpan data suhu input
# maupun suhu hasil konversi. Module ini diberi nama alias np
import numpy as np

# import module matplotlib, khususnya submodule pyplot digunakan untuk 
# menampilkan plot dan diberi nama alias plot
import matplotlib.pyplot as plot

# import ttk dari module tkinter
from tkinter import ttk


# module tkinter yang sudah diimport akan dijadikan variabel bernama 'root'
root = tk.Tk()
# atur panjang dan lebar dari window GUI yang akan dibuat menggunakan
# method geometry. Di sini, window akan memiliki lebar 400 dan lebar 300
root.geometry('400x300')
# atur agar window tidak dapat diubah dengan method resizable dan diberi 
# argumen bernilai false
root.resizable(False, False)
# atur judul pada window dengan method title dan diberi argumen berupa string
root.title('Konversi Suhu Celsius')

# variabel current_value digunakan untuk menunjukkan value pada slider 
# dengan nilai berupa return dari fungsi DoubleVar() dari objek tk
current_value  = tk.DoubleVar()

# variabel current_value akan dipanggil dengan method ini, dimana terdapat
# format, yaitu nilai yang dikembalikan dapat memiliki dua angka dibelakang koma.
# nilai current_value dipanggil dengan fungsi get( )
def get_current_value():
    return '{: .2f}'.format(current_value.get())

# fungsi di bawah ini digunakan untuk mengupdate text pada label suhu_cel_label
# atau label yang digunakan untuk menunjukkan besarnya input suhu celsius
# argumen dari fungsi ini adalah event dan memanggil fungsi configure dari
# objek suhu_cel_label dengan argumen yaitu mengubah text label menjadi variabel
# return dari fungsi get_current_value()
def slider_changed(event):
    suhu_cel_label.configure(text=get_current_value())

# fungsi konversi_suhu() digunakan untuk menngkonversi suhu celsius menjadi 
# fahrenheit dan reamur
def konversi_suhu():
    # fungsi get_current_value() dipanggil kembali dimana nilai yang 
    # dikembalikan akan menjadi nilai celsius_input
    celsius_input = get_current_value()
    
    # celsius_input dikonversikan menjadi float dengan nama variabel 
    # calsius_val
    celsius_val = float(celsius_input) 
    # variabel fahrenheit_val akan diisi dengan hasil perhitungan konversi dari
    # suhu celsius ke suhu fahrenheit
    fahrenheit_val = (9/ 5) * celsius_val + 32
    # variabel reamur_val akan diisi dengan hasil perhitungan konversi dari
    # suhu celsius ke suhu reamur
    reamur_val = (4 / 5) * celsius_val
    
    # suhu celsius yang telah dikonversi menjadi suhu fahrenheit akan diisikan
    # pada kolom text field dengan memanggil fungsi insert dari objek Entry
    # yaitu fah_entry, diperlukan letak baris dari fah_entry serta string data   
    # yang akan diisikan sebagai argumen
    fah_entry.insert(6, str(fahrenheit_val))
    # suhu celsius yang telah dikonversi menjadi suhu reamur akan diisikan 
    # pada kolom text fiedl dengan memanggil fungsi insert dari objek Entry 
    # yaitu rmr_entry, diperlukan letak baris dari rmr_entry serta string data
    # yang akan diisikan sebagai argumen 
    rmr_entry.insert(7, str(reamur_val))
    
    # definisikan variabel labelArray bertipe numpy dengan isi berupa array
    # besaran suhu
    labelArray = np.array(['Suhu Celsius', 'Suhu Fahrenheit', 'Suhu Reamur'])
    # definisikan variabel labelKonversi bertipe numpty dengan isi berupa array
    # suhu inputan dan suhu hasil konversi
    labelKonversi = np.array([float(celsius_val), 
                              float(fahrenheit_val),
                              float(reamur_val)])
    # dari variabel plot panggil fungsi bar yang akan menampilkan bar dengan 
    # garis horizontal merupakan besaran suhu dan garis vertical adalah suhu 
    # celsius dan suhu hasil konversi. Atur agar lebar tiap bar menjadi 0,5
    # menggunakan perintah width serta ubah warnanya menjadi hijau dengan 
    # perintah color
    plot.bar(labelArray, labelKonversi, width = 0.5, color = 'green')
    # agar bar dapat terlihat, panggil fungsi show() dari variabel plot 
    plot.show()

# fungsi ulang() digunakan untuk melakukan reset agar kolom hasil konversi 
# kosong dan suhu celsius dapat dihitung kembali
def ulang():
    # untuk melakukan reset, data pada text field akan dihapus dengan fungsi
    # delete dari variabel fah_entry dengan rentang data yaitu 0 sampai 50
    fah_entry.delete(0, 50)
    # untuk melakukan reset, data pada text field akan dihapus dengan fungsi
    # delete dari variabel rmr_entry dengan rentang data yaitu 0 sampai 50
    rmr_entry.delete(0, 50)


# definisikan variabel slider_label dengan tipe Label dari variabel ttk. Atur
# agar label ditampilkan pada jendela utama yaitu root dan diberi teks 'Slider'
slider_label = ttk.Label(
    root,
    text='Slider:'
)
# atur letak variabel slider_label dengan fungsi grid. Variabel akan diletakkan 
# pada baris 0 dan kolom 0. 
slider_label.grid(
    column=0,
    row=0,
    # sticky digunakan ketika tidak ada ruang pada root, label akan diletakkan
    # di bagian barat (west)
    sticky='w'
)

# definisikan variabel slider dengan tipe Scale dari variabel ttk. Atur agar
# slider ditampilkan pada jendela utama yaitu root dan rentang angka yaitu 0 
# sampai 100 dengan orientasinya horizontal
slider = ttk.Scale(
    root,
    from_= 0,
    to = 100,
    orient = 'horizontal',
    # slider akan memanggil method slider_changed tiap kali slider digerakkan
    command = slider_changed,
    # variabel control untuk objek ini berasal dari class DoubleVar()
    variable = current_value
)
# atur letak variabel slider dengan fungsi grid. Variabel akan diletakkan 
# pada baris 0 dan kolom 2.
slider.grid(
    column=2,
    row=0,
    # sticky digunakan ketika tidak ada ruang pada root, slider akan diletakkan
    # di bagian timur (east)
    sticky='e'
)

# definisikan variabel current_value_label dengan tipe Label dari variabel ttk. 
# Atur agar labels ditampilkan pada jendela utama yaitu root dengan isi berupa 
# text. Label ini digunakan untuk menunjukkan suhu celsius yang diinputkan
current_value_label = ttk.Label(
    root,
    text='Suhu Celsius:'
)
# atur letak variabel current_value_label dengan fungsi grid. Variabel akan  
# diletakkan pada baris 1 dan kolom 2.
current_value_label.grid(
    row=1,
    column=2,
    # sticky digunakan ketika tidak ada ruang pada root, label akan diletakkan
    # di bagian utara (north)
    sticky='n'
)

# definisikan variabel suhu_cel_label dengan tipe Label dari variabel ttk. 
# Atur agar variabel ini ditampilkan pada jendela utama yaitu root dengan isi berupa 
# return dari method get_current_label. Label ini akan menampilkan suhu celsius
# yang sama dengan nilai pada slider tiap kali digerakkan
suhu_cel_label = ttk.Label(
    root,
    text=get_current_value()
)
# atur letak variabel suhu_cel_label dengan fungsi grid. Variabel akan  
# diletakkan pada baris 2 dan kolom 2.
suhu_cel_label.grid(
    row=2,
    column=2,
    # sticky digunakan ketika tidak ada ruang pada root, label ini akan diletakkan
    # di bagian utara (north)
    sticky='n'
)

# definisikan variabel konvers_but dengan tipe Button dari variabel ttk. 
# Atur agar Button ditampilkan pada jendela utama yaitu root dengan isi berupa 
# text serta memanggil fungsi konversi_suhu() tiap kali diklik
konvers_but = ttk.Button(
    root, 
    text = "Hitung",
    command = konversi_suhu)
# atur letak variabel konvers_but dengan fungsi grid. Variabel akan  
# diletakkan pada baris 5 dan kolom 2.
konvers_but.grid(
    row = 5,
    column = 2,
    # sticky digunakan ketika tidak ada ruang pada root, button ini akan 
    # diletakkan di bagian utara (north)
    sticky = 'n')

# definisikan variabel suhu_fah_label dengan tipe Label dari variabel ttk. 
# Atur agar variabel ini ditampilkan pada jendela utama yaitu root dengan isi 
# text. Label ini digunakan untuk menunjukkan suhu fahrenheit hasil konversi
suhu_fah_label = ttk.Label(
    root,
    text = "Suhu Fahrenheit     : " )
# atur letak variabel suhu_fahrenheit_label dengan fungsi grid. Variabel akan  
# diletakkan pada baris 7 dan kolom 1.
suhu_fah_label.grid(
    row =7,
    column = 1,
    # sticky digunakan ketika tidak ada ruang pada root, label ini akan 
    # diletakkan di bagian utara (north)
    sticky = 'n')

# definisikan variabel suhu_rmr_label dengan tipe Label dari variabel ttk. 
# Atur agar variabel ini ditampilkan pada jendela utama yaitu root dengan isi 
# text. Label ini digunakan untuk menunjukkan suhu reamur hasil konversi
suhu_rmr_label = ttk.Label(
    root,
    text = "Suhu Reamur         : ")
# atur letak variabel suhu_rmr_label dengan fungsi grid. Variabel akan  
# diletakkan pada baris 8 dan kolom 1.
suhu_rmr_label.grid(
    row = 8,
    column = 1,
    # sticky digunakan ketika tidak ada ruang pada root, label ini akan 
    # diletakkan di bagian utara (north)
    sticky = 'n')

# definisikan variabel fah_entry dengan tipe Entry dari variabel ttk. 
# Atur agar variabel ini ditampilkan pada jendela utama yaitu root. Entry ini 
# digunakan untuk menampilkan suhu fahrenheit hasil konversi
fah_entry = ttk.Entry(
    root)
# atur letak variabel fah_entry dengan fungsi grid. Variabel akan  
# diletakkan pada baris 7 dan kolom 3.
fah_entry.grid(
    row = 7,
    column = 3)

# definisikan variabel rmr_entry dengan tipe Entry dari variabel ttk. 
# Atur agar variabel ini ditampilkan pada jendela utama yaitu root. Entry ini 
# digunakan untuk menampilkan suhu reamur hasil konversi
rmr_entry = ttk.Entry(
    root)
# atur letak variabel rmr_entry dengan fungsi grid. Variabel akan  
# diletakkan pada baris 8 dan kolom 3.
rmr_entry.grid(
    row = 8,
    column = 3)

# definisikan variabel ulang_but dengan tipe Button dari variabel ttk. 
# Atur agar button ini ditampilkan pada jendela utama yaitu root dengan isi berupa 
# text serta memanggil fungsi ulang() tiap kali diklik
ulang_but = ttk.Button(root, 
            text = "Reset",
            command = ulang)
# atur letak variabel ulang_but dengan fungsi grid. Variabel akan  
# diletakkan pada baris 9 dan kolom 2.
ulang_but.grid(
    row = 9,
    column = 2)

# code diakhir dengan memanggil fungsi mainloop() dari variabel root agar
# tkinter dapat berjalan dan menampilkan GUI
root.mainloop()
