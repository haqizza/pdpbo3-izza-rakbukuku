from buku import Buku
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
import shutil
import os
import json

#Saya Muhammad Izzatul Haq mengerjakan TP3 dalam Praktek mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah di spesifikasikan. Aamiin.

rak_buku = []

window = Tk()
window.title("Rak Bukuku")

# Main Window Frames

leftFrame = Frame(window, width = 400, height = 400, padx  =  20, pady  =  20, relief = RIDGE, borderwidth = 1)
leftFrame.pack(fill = BOTH, side = LEFT, expand = True)

rightFrame = Frame(window, width = 300, height = 400, padx  =  20, pady  =  20, relief = RIDGE, borderwidth = 1)
rightFrame.pack(fill = BOTH, side = LEFT, expand = True)


# Left Frame
# INPUTS

lbl_judul = Label(leftFrame, text = "Judul")
lbl_judul.grid(row = 0, column = 0, padx = (0, 10), pady = 5, sticky = W)

tb_judul = Entry(leftFrame, width = "40")
tb_judul.grid(row = 0, column = 1)

lbl_kategori = Label(leftFrame, text = "Kategori")
lbl_kategori.grid(row = 1, column = 0, padx = (0, 10), pady = 5, sticky = W)

kategoriVar  = StringVar()
cbx_kategori = ttk.Combobox(leftFrame, textvariable = kategoriVar, width="37")
cbx_kategori['values'] = ("Adab",
                        "Aqidah",
                        "Bahasa",
                        "Fiqih",
                        "Hukum",
                        "Komik",
                        "Light Novel",
                        "Novel",
                        "Politik",
                        "Tafsir")
cbx_kategori.grid(row = 1, column = 1)
cbx_kategori.current(0)

lbl_penulis = Label(leftFrame, text = "Penulis")
lbl_penulis.grid(row = 2, column = 0, padx = (0, 10), pady = 5, sticky = W)

tb_penulis = Entry(leftFrame, width = "40")
tb_penulis.grid(row = 2, column = 1)

lbl_th_terbit = Label(leftFrame, text = "Tahun Terbit")
lbl_th_terbit.grid(row = 3, column = 0, padx = (0, 10), pady = 5, sticky = W)

tb_th_terbit = Entry(leftFrame, width = "40")
tb_th_terbit.grid(row = 3, column = 1)

lbl_penerbit = Label(leftFrame, text = "Penerbit")
lbl_penerbit.grid(row = 4, column = 0, padx = (0, 10), pady = 5, sticky = W)

tb_penerbit = Entry(leftFrame, width = "40")
tb_penerbit.grid(row = 4, column = 1)

lbl_keadaan = Label(leftFrame, text = "Keadaan")
lbl_keadaan.grid(row = 5, column = 0, rowspan = 2, padx = (0, 10), pady = 5, sticky = W)


# Radio

keadaanVar = StringVar()

rb_keadaan1 = Radiobutton(leftFrame, text = "Baru", variable = keadaanVar , value = "Baru", width = "32", anchor = W)
rb_keadaan1.grid(row = 5, column = 1)
rb_keadaan1.select()

rb_keadaan2 = Radiobutton(leftFrame, text = "Bekas", variable = keadaanVar, value = "Bekas", width = "32", anchor = W)
rb_keadaan2.grid(row = 6, column = 1)

lbl_genre = Label(leftFrame, text = "Genre")
lbl_genre.grid(row = 7, column = 0, rowspan = 3, padx = (0, 10), pady = 5, sticky = W)


# Check Box

genre1 = StringVar()
genre2 = StringVar()
genre3 = StringVar()

cb_genre1 = Checkbutton(leftFrame, text = "Sastra Klasik", variable = genre1, onvalue = "Sastra Klasik", offvalue = "")
cb_genre1.grid(row = 7, column = 1, sticky = W)

cb_genre2 = Checkbutton(leftFrame, text = "Fiksi", variable = genre2, onvalue = "Fiksi", offvalue = "")
cb_genre2.grid(row = 8, column = 1, sticky = W)

cb_genre3 = Checkbutton(leftFrame, text = "Non-fiksi", variable = genre3, onvalue = "Non-fiksi", offvalue = "")
cb_genre3.grid(row = 9, column = 1, sticky = W)


#Photo Upload
def photoUpload():
    global savePath

    path = fd.askopenfilename(initialdir = "/", title="Pilih File",filetype=(("All File Types","*.*"),("jpeg","*.jpg"),("png","*.png")))
    filename = path.split("/")
    filename = filename[-1]

    currentDir = os.getcwd()
    savePath = currentDir + "\img\\" + filename
    shutil.copy(path, savePath)


btn_foto = Button(leftFrame, text = "Pilih Foto", command = photoUpload, width = 45, pady = 5)
btn_foto.grid(row = 10, column = 0, columnspan = 2, pady = 5)


# Submit Data
def submitData():
    judul = tb_judul.get()
    kategori = kategoriVar.get()
    penulis = tb_penulis.get()

    genre = genre1.get()  + " " + genre2.get() + " " + genre3.get()
    genre = genre.replace(" ", ", ")

    tahun_terbit = tb_th_terbit.get()
    penerbit = tb_penerbit.get()
    keadaan = keadaanVar.get()
    path_foto = savePath
    print(judul, kategori, penulis, genre, int(tahun_terbit), penerbit, keadaan, path_foto)
    if(judul == "" or kategori == "" or penulis == "" or genre == "" or tahun_terbit == "" or penerbit == "" or keadaan == "" or path_foto == ""):
        messagebox.showwarning(window, "Masih ada field yang kosong")
    else:
        rak_buku.append(Buku(judul, kategori, penulis, genre, int(tahun_terbit), penerbit, keadaan, path_foto))
        jsonData = { json.dumps(rak_buku[-1].__dict__) }

        with open("rakbuku.json", "w") as outfile:
            outfile.write(jsonData)


# Submit Button

btn_submit = Button(leftFrame, text = "Simpan", command = submitData, width = 45, pady = 5)
btn_submit.grid(row = 11, column = 0, columnspan = 2, pady = 5)



# Right Frame

appTitle = Label(rightFrame, text = "Rak Bukuku", font=("TkDefaultFont", 25,))
appTitle.pack(anchor = W)

appDesc = Label(rightFrame, text = "Aplikasi pengelolaan rak bukumu")
appDesc.pack(anchor = W)

b_tampilkanBuku = Button(rightFrame, text = "Tampilkan Semua Buku", width = 25, pady = 5)
b_tampilkanBuku.pack(pady = (60, 5), anchor = S)

b_hapusBuku = Button(rightFrame, text = "Hapus Semua Buku", width = 25, pady = 5)
b_hapusBuku.pack(pady = 5, anchor = S)

b_tentang = Button(rightFrame, text = "Tentang", width = 25, pady = 5)
b_tentang.pack(pady = 5, anchor = S)

b_exit = Button(rightFrame, text = "Exit", command = window.quit, width = 25, pady = 5)
b_exit.pack(pady = (60, 5), anchor = S)



# for index, h in enumerate(hunians):
#     idx  =  Label(frame, text = str(index+1), width = 5, borderwidth = 1, relief = "solid")
#     idx.grid(row = index, column = 0)

#     type  =  Label(frame, text = h.get_jenis(), width = 15, borderwidth = 1, relief = "solid")
#     type.grid(row = index, column = 1)

#     if h.get_jenis() ! =  "Indekos": 
#         name  =  Label(frame, text = " " + h.get_nama_pemilik(), width = 40, borderwidth = 1, relief = "solid", anchor = "w")
#         name.grid(row = index, column = 2)
#     else:
#         name  =  Label(frame, text = " " + h.get_nama_penghuni(), width = 40, borderwidth = 1, relief = "solid", anchor = "w")
#         name.grid(row = index, column = 2)

#     b_detail  =  Button(frame, text = "Details ", command = lambda index = index: details(index))
#     b_detail.grid(row = index, column = 3)

window.mainloop()
