
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox 
import random

class gachasystem():
    def daffa():
        for n in range (1):
            bebatuan=['Daffa','besi','batu','intan','perak']
            hasil=random.choice(bebatuan)
            if hasil=='Daffa':
                pesan='Selamat anda mendapatkan Daffa'
            elif hasil=='besi':
                pesan='Anda mendapatkan besi'
            elif hasil=='batu':
                pesan='Anda mendapatkan batu'
            elif hasil=='intan':
                pesan='Anda mendapatkan intan'
            elif hasil=='perak':
                pesan='Anda mendapatkan perak'
            messagebox.showinfo(hasil, pesan)
            return 0


    def faizal():
        for n in range (1):
            bebatuan=['Faizal','besi','batu','intan','perak']
            hasil=random.choice(bebatuan)
            if hasil=='Faizal':
                pesan='Selamat anda mendapatkan Faizal'
            elif hasil=='besi':
                pesan='Anda mendapatkan besi'
            elif hasil=='batu':
                pesan='Anda mendapatkan batu'
            elif hasil=='intan':
                pesan='Anda mendapatkan intan'
            elif hasil=='perak':
                pesan='Anda mendapatkan perak'
            messagebox.showinfo(hasil, pesan)
            return 0

    def ahmad():
        for n in range (1):
            bebatuan=['Ahmad','besi','batu','intan','perak']
            hasil=random.choice(bebatuan)
            if hasil=='Ahmad':
                pesan='Selamat anda mendapatkan Ahmad'
            elif hasil=='besi':
                pesan='Anda mendapatkan besi'
            elif hasil=='batu':
                pesan='Anda mendapatkan batu'
            elif hasil=='intan':
                pesan='Anda mendapatkan intan'
            elif hasil=='perak':
                pesan='Anda mendapatkan perak'
            messagebox.showinfo(hasil, pesan)
            return 0

class banners():
    def banner1():
        global bg1
        tap = Toplevel()
        tap.title('BANNER LIMITED AHMAD')
        tap.iconbitmap('E:/2020/media/mim/icon1.ico')

        bg1 = PhotoImage(file="E:/2020/media/mim/ahmad.png")
        my_canvas = Canvas(tap, width=800, height=500)
        my_canvas.pack(fill="both", expand=True)
        my_canvas.create_image(0,0, image=bg1, anchor="nw")

        button7 = Button(tap, bg="#D3B5E5", command=gachasystem.ahmad, text="Pull").place(x = 650,y = 450)
        button10 = Button(tap, bg="#D3B5E5", command=tap.destroy, text="EXIT").place(x = 750,y = 450)

    def banner2():
        global bg2
        tip = Toplevel()
        tip.title('BANNER LIMITED FAIZAL')
        tip.iconbitmap('E:/2020/media/mim/icon1.ico')

        bg2 = PhotoImage(file="E:/2020/media/mim/isal.png")
        my_canvas = Canvas(tip, width=800, height=500)
        my_canvas.pack(fill="both", expand=True)
        my_canvas.create_image(0,0, image=bg2, anchor="nw")

        button5 = Button(tip, bg="#D3B5E5", command=gachasystem.faizal, text="Pull").place(x = 650,y = 450)
        button10 = Button(tip, bg="#D3B5E5", command=tip.destroy, text="EXIT").place(x = 750,y = 450)

    def banner3():
        global bg3
        tup = Toplevel()
        tup.title('BANNER LIMITED DAFFA')
        tup.iconbitmap('E:/2020/media/mim/icon1.ico')

        bg3 = PhotoImage(file="E:/2020/media/mim/daffa.png")
        my_canvas = Canvas(tup, width=800, height=500)
        my_canvas.pack(fill="both", expand=True)
        my_canvas.create_image(0,0, image=bg3, anchor="nw")

        button6 = Button(tup, bg="#D3B5E5", command=gachasystem.daffa, text="Pull").place(x = 650,y = 450)
        button10 = Button(tup, bg="#D3B5E5", command=tup.destroy, text="EXIT").place(x = 750,y = 450)


class tosandexit():
    def termsofservice():
        global bg4
        tep = Toplevel()
        tep.title('GACHA DETAILS')
        tep.iconbitmap('E:/2020/media/mim/icon1.ico')
        tep.geometry("300x125")

        bg4 = PhotoImage(file="E:/2020/media/mim/mostimaapp.png")
        my_canvas = Canvas(tep, width=800, height=500)
        my_canvas.pack(fill="both", expand=True)
        my_canvas.create_image(0,0, image=bg4, anchor="nw")


        my_canvas.create_text(140, 42, text="""
        kami memberi anda kesempatan untuk 
        mendapatkan karakter limited sebesar 20%.
        Kami tidak memiliki sistem pity apapun 
        dalam sistem gacha kami karena menggunakan 
        sistem random dan tidak chance. Dikarenakan 
        kami tidak memberi pity pada banner manapun.
        Terima Kasih

        dwico.ltd
        """, font=("Helvetica", 10), fill="white")
        button11 = Button(tep, bg="#D3B5E5", command=tep.destroy, text="EXIT").place(x = 255,y = 93)  


    def exit():
        bye = "Have a nice day and remember to GACHA ! GACHA ! GACHA !"
        messagebox.showinfo("GACHA",bye)
        exit(0)

def login():
    perkenalan=""
    if len(stringuser.get()) == 0:
        messagebox.showerror("Error","BELUM MENGISI USERNAME")
        return
    pesan = "Anda Telah Login dengan akun " + stringuser.get() + "!!!"
    messagebox.showinfo("Berhasil Login", pesan)

    button2 = Button(top, bg="#D3B5E5", command=banners.banner1, text="BANNER AHMAD LIMITED").place(x = 220,y = 225)
    button3 = Button(top, bg="#D3B5E5", command=banners.banner2, text="BANNER FAIZAL LIMITED").place(x = 220,y = 485)
    button4 = Button(top, bg="#D3B5E5", command=banners.banner3, text="BANNER DAFFA LIMITED").place(x = 220,y = 350)

top = Tk()  
top.geometry("400x600")
top.title("GACHA")
top.iconbitmap('E:/2020/media/mim/icon1.ico')

bg = PhotoImage(file="E:/2020/media/mim/mostimaap2.png")
my_canvas = Canvas(top, width=800, height=500)
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0,0, image=bg, anchor="nw")
my_canvas.create_text(200, 40, text="GACHA!", font=("Helvetica", 50), fill="#D3B5E5")

lbl1 = Label(top, bg="#D3B5E5", text = "Username\t:")
label1_window = my_canvas.create_window(30, 80, anchor="nw", window=lbl1)

stringuser = StringVar()
inama = Entry(top,width = 20, bg="#D3B5E5", textvariable=stringuser).place(x = 140, y = 80)  

button1 = Button(top, bg="#D3B5E5", command=login, text="MAIN").place(x = 30,y = 107)
button8 = Button(top, bg="#D3B5E5", command=tosandexit.exit, text="EXIT").place(x = 30,y = 140)   
button9 = Button(top, bg="#D3B5E5", command=tosandexit.termsofservice, text="Ketentuan Gacha Kami").place(x = 75 ,y = 140)  

top.mainloop()    

