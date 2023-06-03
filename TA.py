from tkinter import *


class PerhitunganKelistrikan:
    def __init__(self, root):
        self.root = root
        self.root.title("Perhitungan Kelistrikan")
        self.root.config(background="#ECECEC")  

        self.l1 = Label(text="Apa yang ingin dihitung ?", bg="#ECECEC", font="Arial 30 bold", fg="#333333")  
        self.l1.grid(row=0, column=0, columnspan=4, pady=20, padx=30)

        self.iniwidgets()

    def iniwidgets(self):
        # Tombol
        self.tmbl1 = Button(text="Tegangan", bg="#4CAF50", fg="white", activebackground="#45A049",
                            border=5, relief=RIDGE, font="Arial 15 bold", width=15, command=self.jendelategangan)  
        self.tmbl1.grid(row=1, column=0, pady=10)

        self.tmbl2 = Button(text="Arus", bg="#2196F3", fg="white", activebackground="#1E88E5",
                            border=5, relief=RIDGE, font="Arial 15 bold", width=15, command=self.jendelaarus)  
        self.tmbl2.grid(row=1, column=1, pady=10)

        self.tmbl3 = Button(text="Hambatan", bg="#F44336", fg="white", activebackground="#E53935",
                            border=5, relief=RIDGE, font="Arial 15 bold", width=15, command=self.jendelahambatan)  
        self.tmbl3.grid(row=1, column=2, pady=10)

        # Tombol Keluar
        self.tmbl5 = Button(text="Keluar", bg="#9E9E9E", fg="white", activebackground="#757575",
                         border=5, relief=RIDGE, font="Arial 15 bold", width=15, command=self.exit_program)  
        self.tmbl5.grid(row=2, column=0, columnspan=3, pady=(20, 30))

    def jendelategangan(self):
        self.milih = 1
        jendela_tegangan = Toplevel(self.root)
        jendela_tegangan.title("Perhitungan Tegangan")
        jendela_tegangan.config(background="#ECECEC")  

        l1_arus = Label(jendela_tegangan, text="Masukkan nilai Arus:", bg="#ECECEC", font="Arial 20 bold", fg="#333333")  
        l1_arus.grid(row=0, column=0, pady=10)

        input_arus = Entry(jendela_tegangan, bd=5, relief=RIDGE, font="Arial 20", width=10)  
        input_arus.grid(row=0, column=1)

        l2_hambatan = Label(jendela_tegangan, text="Masukkan nilai Hambatan:", bg="#ECECEC", font="Arial 20 bold", fg="#333333")  
        l2_hambatan.grid(row=1, column=0, pady=10)

        input_hambatan = Entry(jendela_tegangan, bd=5, relief=RIDGE, font="Arial 20", width=10)  
        input_hambatan.grid(row=1, column=1)

        tmbl_hitung = Button(jendela_tegangan, text="Hitung", bg="#4CAF50", fg="white", activebackground="#45A049",
                               bd=5, relief=RIDGE, font="Arial 15 bold", width=10,
                               command=lambda: self.hitung_tegangan(input_arus.get(), input_hambatan.get()))  
        tmbl_hitung.grid(row=2, column=0, columnspan=2, pady=10)

        l3_hasil = Label(jendela_tegangan, text="Hasil Tegangan:", font="Arial 20 bold", bg="#ECECEC", fg="#333333")  
        l3_hasil.grid(row=3, column=0, columnspan=2, pady=10)

        self.label_hasiltegangan = Label(jendela_tegangan, text="", font="Arial 20", bg="#ECECEC")  
        self.label_hasiltegangan.grid(row=4, column=0, columnspan=2, pady=10)

    def jendelaarus(self):
        self.milih = 2
        jendela_arus = Toplevel(self.root)
        jendela_arus.title("Perhitungan Arus")
        jendela_arus.config(background="#ECECEC")  

        l1_tegangan = Label(jendela_arus, text="Masukkan nilai Tegangan:", bg="#ECECEC", font="Arial 20 bold", fg="#333333")  
        l1_tegangan.grid(row=0, column=0, pady=10)

        input_tegangan = Entry(jendela_arus, bd=5, relief=RIDGE, font="Arial 20", width=10)  
        input_tegangan.grid(row=0, column=1)

        l2_hambatan = Label(jendela_arus, text="Masukkan nilai Hambatan:", bg="#ECECEC", font="Arial 20 bold", fg="#333333")  
        l2_hambatan.grid(row=1, column=0, pady=10)

        input_hambatan = Entry(jendela_arus, bd=5, relief=RIDGE, font="Arial 20", width=10)  
        input_hambatan.grid(row=1, column=1)

        tmbl_hitung = Button(jendela_arus, text="Hitung", bg="#2196F3", fg="white", activebackground="#1E88E5",
                               bd=5, relief=RIDGE, font="Arial 15 bold", width=10,
                               command=lambda: self.hitung_arus(input_tegangan.get(), input_hambatan.get()))  
        tmbl_hitung.grid(row=2, column=0, columnspan=2, pady=10)

        l3_hasil = Label(jendela_arus, text="Hasil Arus Listrik:", font="Arial 20 bold", bg="#ECECEC", fg="#333333")  
        l3_hasil.grid(row=3, column=0, columnspan=2, pady=10)

        self.label_hasilarus = Label(jendela_arus, text="", font="Arial 20", bg="#ECECEC")  
        self.label_hasilarus.grid(row=4, column=0, columnspan=2, pady=10)

    def jendelahambatan(self):
        self.milih = 3
        jendela_hambatan = Toplevel(self.root)
        jendela_hambatan.title("Perhitungan Hambatan")
        jendela_hambatan.config(background="#ECECEC")  

        l1_tegangan = Label(jendela_hambatan, text="Masukkan nilai Tegangan:", bg="#ECECEC", font="Arial 20 bold", fg="#333333")  
        l1_tegangan.grid(row=0, column=0, pady=10)

        input_tegangan = Entry(jendela_hambatan, bd=5, relief=RIDGE, font="Arial 20", width=10)  
        input_tegangan.grid(row=0, column=1)

        l2_arus = Label(jendela_hambatan, text="Masukkan nilai Arus:", bg="#ECECEC", font="Arial 20 bold", fg="#333333") 
        l2_arus.grid(row=1, column=0, pady=10)

        input_arus = Entry(jendela_hambatan, bd=5, relief=RIDGE, font="Arial 20", width=10)  
        input_arus.grid(row=1, column=1)

        tmbl_hitung = Button(jendela_hambatan, text="Hitung", bg="#FF9800", fg="white", activebackground="#F57C00",
                               bd=5, relief=RIDGE, font="Arial 15 bold", width=10,
                               command=lambda: self.hitung_hambatan(input_tegangan.get(), input_arus.get()))  
        tmbl_hitung.grid(row=2, column=0, columnspan=2, pady=10)

        l3_hasil = Label(jendela_hambatan, text="Hasil Hambatan:", font="Arial 20 bold", bg="#ECECEC", fg="#333333")  
        l3_hasil.grid(row=3, column=0, columnspan=2, pady=10)

        self.label_hasilhambatan = Label(jendela_hambatan, text="", font="Arial 20", bg="#ECECEC")  
        self.label_hasilhambatan.grid(row=4, column=0, columnspan=2, pady=10)

    def hitung_tegangan(self, arus, hambatan):
        if arus and hambatan:
            try:
                arus = float(arus)
                hambatan = float(hambatan)
                tegangan = arus * hambatan
                self.label_hasiltegangan.config(text=str(tegangan))
            except ValueError:
                self.label_hasiltegangan.config(text="Input tidak valid")
        else:
            self.label_hasiltegangan.config(text="Masukkan nilai arus dan hambatan")

    def hitung_arus(self, tegangan, hambatan):
        if tegangan and hambatan:
            try:
                tegangan = float(tegangan)
                hambatan = float(hambatan)
                arus = tegangan / hambatan
                self.label_hasilarus.config(text=str(arus))
            except ValueError:
                self.label_hasilarus.config(text="Input tidak valid")
        else:
            self.label_hasilarus.config(text="Masukkan nilai tegangan dan hambatan")

    def hitung_hambatan(self, tegangan, arus):
        if tegangan and arus:
            try:
                tegangan = float(tegangan)
                arus = float(arus)
                hambatan = tegangan / arus
                self.label_hasilhambatan.config(text=str(hambatan))
            except ValueError:
                self.label_hasilhambatan.config(text="Input tidak valid")
        else:
            self.label_hasilhambatan.config(text="Masukkan nilai tegangan dan arus")

    def exit_program(self):
        self.root.destroy()


root = Tk()
app = PerhitunganKelistrikan(root)
root.mainloop()
