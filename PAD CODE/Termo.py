# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 17:27:12 2022

@author: Gallery
"""

# import semua fungsi dari tkinter
from tkinter import *

# import kelas messagebox dari tkinter
from tkinter import messagebox

def ulang():
    clsField.delete(0, END)
    fahField.delete(0, END)
    rmrField.delete(0, END)

def cekError():
    if(clsField.get() == ""):
        messagebox.showerror("Input Error")
        ulang()
        
        return -1

def konversiCelsius():
    value = cekError()
    
    if(value == -1):
        return
    else:
        celsius_input =clsField.get()
        
        celsius_val = float(celsius_input)
        fahrenheit_val = (9/ 5) * celsius_val + 32
        reamur_val = (4 / 5) * celsius_val
        
        fahField.insert(13, str(fahrenheit_val))
        rmrField.insert(13, str(reamur_val))

if __name__ == "__main__" :

	# Create a GUI window
	gui = Tk()

	# Set the background colour of GUI window
	gui.configure(background = "white")

	# set the name of tkinter GUI window
	gui.title("Konversi Celsius")

	# Set the configuration of GUI window
	gui.geometry("500x250")

	# Create a Date Of Birth : label
	inputCls = Label(gui, text = "Masukkan Suhu Celsius", bg = "light blue")

	# Create a Given Date : label
	hasilFah = Label(gui, text = "Suhu Fahrenheit : ", bg = "brown")

	# Create a Day : label
	hasilRmr = Label(gui, text = "Suhu Reamur", bg = "brown")
    # Create a Resultant Age Button and attached to calculateAge function
	konversBut = Button(gui, text = "Konversi", fg = "Black", bg = "Red", 
                     command = konversiCelsius)

	# Create a Clear All Button and attached to clearAll function
	ulangBut = Button(gui, text = "Ulang", fg = "Black", bg = "Red", 
                   command = ulang)

	clsField = Entry(gui)
	fahField = Entry(gui)
	rmrField = Entry(gui)
    
	konversBut.grid(row = 7, column =4)
    
	inputCls.grid(row = 0, column = 3)
	clsField.grid(row = 3, column = 3)
    
	ulangBut.grid(row = 22, column = 4)
    
	hasilFah.grid(row = 10, column = 3)
	fahField.grid(row = 13, column = 3)
    
	hasilRmr.grid(row = 10, column = 5)
	rmrField.grid(row = 13, column = 5)
    
gui.mainloop()
    
    
    
    
	

	
    
    
    
    
    
    
    