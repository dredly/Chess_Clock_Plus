from tkinter import *
from tkinter import ttk

def render_main_window():
    """Divides the main window into areas for each player"""
    #Remove the "main menu" widgets
    message1_lab.destroy()
    players_spin.destroy()
    confbutton.destroy()

    #Divide the window into regions equal to the number of players
    num_regions = num_plays.get()

    #Determines which colours to use for the regions
    region_colours = [
            'red',
            'blue',
            'yellow',
            'green',
            'purple',
            'pink',
            'orange',
            'brown'
        ]

    #Determines the grid layout based on number of players
    grid_configs = {
            2: [2, 1],
            3: [2, 2],
            4: [2, 2],
            5: [3, 2],
            6: [3, 2],
            7: [4, 2],
            8: [4, 2]
        }

    rownum = 0
    colnum = 0
    canv_frame = Frame(top)
    canv_frame.grid(row=0, column=0)
    grid_config = grid_configs[int(num_plays.get())]
    for i in range(int(num_plays.get())):
        canv = Canvas(canv_frame, bg=region_colours[i])
        canv.grid(row=rownum, column=colnum, sticky=(N, S, E, W))
        #Check if current grid position is in the last column
        if colnum + 1 == grid_config[1]:
            rownum += 1
            colnum = 0
        else:
            colnum += 1

    top.columnconfigure(0, weight=1)
    top.rowconfigure(0, weight=1)

    for row in range(grid_config[0]):
        canv_frame.rowconfigure(row, weight=1)
    for col in range(grid_config[1]):
        canv_frame.columnconfigure(col, weight=1)
        
#Create a tkinter window
top = Tk()
top.title('Chess Clock Plus')
top.geometry('600x600')

num_plays = StringVar(value=2)

message1 = 'How many players?'
message1_lab = Label(top, text=message1)
message1_lab.pack()

players_spin = Spinbox(top, from_=2, to=8, textvariable=num_plays)
players_spin.pack()

confbutton = Button(top, text='Confirm',
                    command=render_main_window)
confbutton.pack()

top.mainloop()



