from tkinter import *

#Create a tkinter window
top = Tk()
top.title('Chess Clock Plus')

num_plays = StringVar(value=2)

message1 = 'How many players?'
message1_lab = Label(top, text=message1).pack()
players_spin = Spinbox(top, from_=2, to=8, textvariable=num_plays).pack()
confbutton = Button(top, text='Confirm', command=lambda: print(num_plays.get()))
confbutton.pack()

top.mainloop()



