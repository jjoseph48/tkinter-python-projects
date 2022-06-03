# -*- coding: utf-8 -*-
"""
Created on Wed May  4 22:17:31 2022

@author: Gallery
"""

# create sebuah kelas dengan nama RectangleArea
class RectangleArea: 
	# definisikan konstruktor dari kelas ini, dimana atribut length dan width diset
	# menjadi 0 saat sebuah objek diinisiasi
    def __init__(self): 
        self.length = 0 
        self.width = 0 

    # definisikan sebuah method dengan nama set_parameter yang membutuhkan dua 
    # parameter yaitu length dan width 
    def set_parameters(self, input_length, input_width): 
        # panggil atribut length dari kelas ini dan beri nilai berupa argumen
        # input_length yang telah dikonversi menjadi tipe float
        self.length = float(input_length) 
        # panggil atribut width dari kelas ini dan beri nilai berupa argumen
        # input_width yang telah dikonversi menjadi tipe float
        self.width = float(input_width) 

    # definisikan sebuah method get_area yang akan mengembalikan nilai berupa luas
    # dari bangun datar
    def get_area(self): 
        # method ini akan mengembalikan hasil perkalian dari length dan width yang
        # keduanya adalah atribut dari instance
        return self.length*self.width 

if __name__ == "__main__": 
	# lakukan sebuah inputan dengan memanggil method input, dimana user akan diminta 
	# memasukkan nilai dari length (panjang). Inputan akan disimpan pada sebuah
    # variabel bernama input_length
    input_length = input("Please key in the length: ") 
    # lakukan sebuah inputan dengan memanggil method input, dimana user akan diminta 
	# memasukkan nilai dari width(lebar). Inputan akan disimpan pada sebuah
    # variabel bernama input_width
    input_width = input("Please key in the width: ") 

    # inisiasi sebuah objek bertipe RectangleAre dengan nama rectangle  
    rectangle = RectangleArea()
    # set agar atribut length dan width pada obje rectangle memiliki nilai berupa 
    # input_length dan input_width dengan memanggil method set_parameter.
    rectangle.set_parameters(input_length, input_width) 
    # print nilai dari luas objek rectangle dengan mengeprint hasil dari memanggil method # get_area( )
    print (rectangle.get_area())