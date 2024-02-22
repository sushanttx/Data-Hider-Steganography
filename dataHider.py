from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import tkinter as tk
from stegano import lsb

root = Tk()
root.title("Hide Text In Your Image !")
root.geometry("700x600+150+180")
root.resizable(False, False)
root.configure(bg="#2f4155")

def showimage():
    global filename
    file = filedialog.askopenfile(initialdir=os.getcwd(), title='Select image file', filetypes=(("PNG file","*.png"), ("JPG file", "*.jpg"),("All file",".txt")))
    if file:
        filename = file.name
        img = Image.open(filename)
        img = ImageTk.PhotoImage(img)
        lbl.configure(image=img, width=250, height = 250)
        lbl.image = img
def Hide():
    global secret
    message = text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)
    message_label.config(text="Data hidden successfully.")

def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)
    message_label.config(text="Data revealed successfully.")

def save():
    secret.save("hidden.png")
    message_label.config(text="Image saved successfully.")
    
# Add a label to display messages
message_label = Label(root, text="", bg="#2f4155", fg="white")
message_label.place(x=450, y=20)

# Add a function to reset the interface
def reset_interface():
    lbl.config(image="")
    text1.delete(1.0, END)
    message_label.config(text="Interface reset successfully.")

#icon
image_icon = PhotoImage(file="logo.jpg")
root.iconphoto(False, image_icon)
#logo
logo = PhotoImage(file="logo1.png")
Label(root,image=logo,bg="#2f4155").place(x = 10, y = 0)

Label(root, text="CYBER SECURITY", bg = "#2d4155", fg="white", font= "arial 25 bold").place(x = 100, y = 20)

#firstframe
f = Frame(root,bd=3,bg="black", width = 340, height = 280, relief=GROOVE)
f.place(x = 10, y = 80)

lbl = Label(f, bg="black")
lbl.place(x = 40, y =10)

#secondFrame
frame2 = Frame(root, bd = 3, width = 340, height = 280, bg="white", relief = GROOVE)
frame2.place(x = 350, y = 80)

text1 = Text(frame2, font = "Robote 20", bg = "white", fg = "black", relief = GROOVE, wrap=WORD)
text1.place(x = 0, y = 0, width=320, height = 295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x = 320, y = 0, height = 300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#thirdframe
frame3 = Frame(root, bd = 3, bg= "#2f4155", width= 330, height = 100, relief = GROOVE)
frame3.place(x = 10, y = 370)

Button(frame3, text = "Open Image", width = 10, height = 2, font = "arial 14 bold", command=showimage).place(x = 20, y = 30)
Button(frame3, text = "Save Image", width = 10, height = 2, font = "arial 14 bold", command=save).place(x = 180, y = 30)
Label(frame3, text = "Picture, Image, Photo.", bg = "#2f4155", fg = "yellow").place (x = 20, y = 5)

#fourthframe
frame4 = Frame(root, bd = 3, bg = "#2f4155", width = 330, height = 100, relief = GROOVE)
frame4.place(x = 360, y = 370)

Button(frame4, text = "Hide Data", width = 10, height = 2, font = "arial 14 bold", command=Hide).place(x = 20, y = 30)
Button(frame4, text = "Show Data", width = 10, height = 2, font = "arial 14 bold", command=Show).place(x = 180, y = 30)
Label(frame4, text = "Picture, Image, Photo.", bg ="#2f4155", fg = "yellow").place(x = 20, y = 5)

#fifthframe

frame5 = Frame(root, bd = 3, bg = "#2f4155", width = 130, height = 40, relief = GROOVE)
frame5.place(x = 280, y = 480)

# Add a button to reset the interface
Button(frame5, text="Reset", width=10, height=1, font="arial 14 bold", command=reset_interface).place(x= 0, y=0)




root.mainloop()