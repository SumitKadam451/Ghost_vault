from tkinter import *
from tkinter import messagebox
import base64
import os


def decrypt():
    password = code.get()

    if password == "1234":
        message = Text1.get(1.0, END)
        base64_str = message.strip()  # Remove leading/trailing whitespace
        try:
            base64_bytes = base64_str.encode("ascii")
            decode_message = base64.b64decode(base64_bytes)
            decrypted_message = decode_message.decode("ascii")

            screen2 = Toplevel(screen)
            screen2.title("Decryption")
            screen2.geometry("400x200")
            screen2.configure(bg="#00bd56")

            Label(screen2, text="DECRYPTED MESSAGE", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
            text2 = Text(screen2, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)

            text2.insert(END, decrypted_message)

        except base64.binascii.Error:
            messagebox.showerror("Decryption", "Invalid Base64-encoded string")

    elif password == "":
        messagebox.showerror("Decryption", "Input Password")

    else:
        messagebox.showerror("Decryption", "Invalid Password")


def encrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = Text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)  # Encoding instead of decoding
        base64_str = base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, base64_str)

    elif password == "":
        messagebox.showerror("encryption", "Input Password")

    elif password != "1234":
        messagebox.showerror("encryption", "Invalid Password")




def main_screen():

    global screen
    global code
    global Text1

    screen=Tk()
    screen.geometry("375x398")

    #icon
    image_icon=PhotoImage(file="logo.png")
    screen.iconphoto(False,image_icon)
    screen.title("Ghost Vault")

    def reset():
        code.set("")
        Text1.delete(1.0,END)




    Label(text="Enter text for Encryption and Decryption",fg="black",font=("calbri",13)).place(x=10,y=10)
    Text1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    Text1.place(x=10,y=50,width=355,height=100)

    Label(text="Enter text for Encryption and Decryption",fg="black",font=("calbri",13)).place(x=10,y=170)

    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)

    Button(text="ENCRYPT",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT",height="2",width=23,bg="#00BD56",fg="white",bd=0,command=decrypt).place(x=200,y=250)
    Button(text="RESET",height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)



    screen.mainloop()

main_screen()

