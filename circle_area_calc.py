import numpy as np
import tkinter as tk
from tkinter import font
import ttkbootstrap as ttk

root = ttk.Window(themename='darkly')
root.geometry('500x300')
root.title('circle area calc')

def find_area():
    if not exact.get():
        square_radi = np.square(radi.get())
        area.set(np.multiply(square_radi,np.pi))
    
    if exact.get():
        square_radi = np.square(radi.get())
        area.set(square_radi)
        area.set(area.get() + 'π')
       

radi = tk.IntVar()
area = tk.StringVar()
exact = tk.BooleanVar()

area_display = ttk.Label(root, textvariable=area, font='P052 25 bold')
radius_input = ttk.Entry(root, textvariable=radi)
select_frame = ttk.Frame(root)
exact_select = ttk.Checkbutton(select_frame, text='exact area', variable=exact)
area_button = ttk.Button(select_frame, text='find area', command=find_area)


area_display.pack()
radius_input.pack()
select_frame.pack()
exact_select.pack(side='left')
area_button.pack(side='right')


root.mainloop()
