from tkinter import *
from tkinter import *

from time import strftime

root= Tk()
root.title('clock')

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(100,time)



lbl=Label(root,font=('TIMES', 120 ,'bold'),
          background= 'black',
          foreground='white')

lbl.pack(anchor='center')
time()
mainloop()
