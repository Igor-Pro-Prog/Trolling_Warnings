import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

cont =0

msg_box = messagebox.showwarning("Warning", "VOCÊ FOI HACKEADO")

if msg_box == 'ok':
   msg_box = messagebox.askquestion("PERA AI!", "PARA SER DESHACKEADO CONTINUE!!")

if msg_box == "ok":
   msg_box = messagebox.askquestion("O QUE ACHA?", "VOCÊ QUER NAMORAR COMIGO?")

while msg_box == 'no':
   cont += 1
   msg_box = messagebox.askquestion("O QUE ACHA?", "VOCÊ QUER NAMORAR COMIGO?")
   if cont == 5:
        msg_box = messagebox.showerror("TO INDO AI!!", "VOCÊ FOI BLOQUEADA")
        break

if msg_box =='yes':
    msg_box = messagebox.showinfo("BOA", "SABIA ESCOLHA <3")
