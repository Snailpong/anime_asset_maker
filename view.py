from tkinter import *
import tkinter.ttk
from PIL import Image as Img
from PIL import ImageTk
import numpy as np

from controller import *


# Background cartoonization frame
def compose_frame_bg(frame):
    Label(frame, text="Original").place(x=10, y=10)
    Label(frame, text="Style1").place(x=360, y=10)
    Label(frame, text="Style2").place(x=710, y=10)
    Label(frame, text="Style3").place(x=10, y=345)
    Label(frame, text="Style4").place(x=360, y=345)
    Label(frame, text="Style5").place(x=710, y=345)

    image_load = ImageTk.PhotoImage(Img.fromarray(np.zeros((300, 300, 3), dtype=np.uint8)))
    label_load = Label(frame, width=300, height=300)
    set_label_image(label_load, image_load)
    label_load.place(x=10, y=30)
    label_gen1 = Label(frame, width=300, height=300)
    set_label_image(label_gen1, image_load)
    label_gen1.place(x=360, y=30)
    label_gen2 = Label(frame, width=300, height=300)
    set_label_image(label_gen2, image_load)
    label_gen2.place(x=710, y=30)
    label_gen3 = Label(frame, width=300, height=300)
    set_label_image(label_gen3, image_load)
    label_gen3.place(x=10, y=370)
    label_gen4 = Label(frame, width=300, height=300)
    set_label_image(label_gen4, image_load)
    label_gen4.place(x=710, y=370)
    label_gen5 = Label(frame, width=300, height=300)
    set_label_image(label_gen5, image_load)
    label_gen5.place(x=360, y=370)

    label_list = [label_load, label_gen1, label_gen2, label_gen3, label_gen4, label_gen5]

    Button(frame, command=lambda: load_button_bg(label_list), text='Load').place(x=270, y=0)
    Button(frame, command=lambda: save_picture(0), text='Save').place(x=620, y=0)
    Button(frame, command=lambda: save_picture(1), text='Save').place(x=970, y=0)
    Button(frame, command=lambda: save_picture(2), text='Save').place(x=270, y=340)
    Button(frame, command=lambda: save_picture(3), text='Save').place(x=620, y=340)
    Button(frame, command=lambda: save_picture(4), text='Save').place(x=970, y=340)

# Mesh reconstruction frame
def compose_frame_mesh(frame):
    Label(frame, text="Image").place(x=160, y=0)
    Label(frame, text="Mask").place(x=610, y=0)

    Button(frame, command=lambda: load_button_mesh(label_fg, 0), text='Load Image').place(x=420, y=0)
    Button(frame, command=lambda: load_button_mesh(label_mask, 1), text='Load Mask').place(x=870, y=0)
    Button(frame, command=lambda: pifu_eval(), text='Estimate Mesh').place(x=400, y=650)
    Button(frame, command=lambda: view_mesh(), text='View Estimated Mesh').place(x=600, y=650)
    
    image_fg = ImageTk.PhotoImage(Img.fromarray(np.zeros((640, 640, 3), dtype=np.uint8)))
    label_fg = Label(frame, width=320, height=600)
    set_label_image(label_fg, image_fg)
    label_fg.place(x=160, y=30)
    label_mask = Label(frame, width=320, height=600)
    set_label_image(label_mask, image_fg)
    label_mask.place(x=600, y=30)

# Compose overall UI (label, button)
def compose_ui(window):
    notebook = ttk.Notebook(window, width=1080, height=720)
    notebook.pack()

    frame_bg = Frame(window)
    notebook.add(frame_bg, text="Background Cartoonization")
    compose_frame_bg(frame_bg)

    frame_mesh = Frame(window)
    notebook.add(frame_mesh, text="Mesh Reconstruction")
    compose_frame_mesh(frame_mesh)

# Set and start window
def start_window():
    window = Tk()
    window.title("Anime Asset Maker")
    window.geometry("1080x720+100+100")
    window.resizable(False, False)
    compose_ui(window)
    window.mainloop()