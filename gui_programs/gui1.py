from tkinter import *
master = Tk()
whatever_you_do = "Hello"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack( )
mainloop( )
