from tkinter import*
from tkinter import messagebox
import pyqrcode


ws = Tk()
ws.title("AIDS -2 a,b oops crt")
ws.config(bg='orange')
def generate_qr():
    if len(user_input.get())!=0:
        global qr,img
        qr = pyqrcode.create(user_input.get())
        img = BitmapImage(data = qr.xbm(scale=8))

    else:
        messagebox.showwarning('warning','all fields are requried!')
    try:
        display_code()
    except:
        pass
def display_code():
    img_ibl.config(image = img)
    output.config(text="qr code of " + user_input.get())

lbl = Label(ws,text="Enter a message or url",bg = 'red')
lbl.pack()


user_input = StringVar()
Entry = Entry(ws, textvariable = user_input)
Entry.pack(padx = 40)

Button = Button (ws,text="click to generate",width=20,command = generate_qr)

Button.pack(pady=40)

img_ibl = Label(ws,bg = 'blue')
img_ibl.pack()

output = Label(ws,text =" ",bg="pink")
output.pack()
ws.mainloop()
