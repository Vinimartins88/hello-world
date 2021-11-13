from tkinter import *
from pyqrcode import QRCode
import pyqrcode
from PIL import Image, ImageTk
import tkinter as tk


# Código do Projeto QR-Code
def create_img():
    url = pyqrcode.create(codigo_entry.get())
    url.png("QR-Code12321.png", scale=6)

# Salvar imagem
#def salvar_img():
   

# Mostrar Imagem
def open_img():
    create_img()
    img = Image.open("QR-Code12321.png")
    img = img.resize((222, 222), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(jan, image=img)
    panel.image = img
    panel.place(relx=0.15, rely=0.37)


# Criar nossa janela e logo
jan = Tk()
jan.title("PROJETO QR-CODE")
jan["bg"] = "#00BFFF"
jan.geometry("350x450")
img = PhotoImage(file="icons/logo.png")
label_imagem = Label(jan, image=img).place(relx=0.13, rely=0.02)
jan.iconbitmap("icons/iconqr.ico")

# Criação da Label e Entry:
lb_codigo = Label(jan, text="URL:", fg="blue")
lb_codigo.place(relx=0.03, rely=0.31)
codigo_entry = Entry(jan)
codigo_entry.place(relx=0.13, rely=0.31, relwidth=0.85)

# Add os botões
bt = Button(jan, text="Gerar QRCode", bd=3, bg="lightblue", command=open_img)
bt.place(relx=0.37, rely=0.23, relwidth=0.25)

bt2 = Button(jan, text="Salvar", bd=3, bg="lightblue") #command=)
bt2.place(relx=0.37, rely=0.92, relwidth=0.25)

jan.mainloop()