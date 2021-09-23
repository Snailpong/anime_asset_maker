from tkinter import *
import tkinter.ttk
import tkinterweb
from PIL import Image as Img
from PIL import ImageTk
import numpy as np

from controller import *


def compose_frame1(frame1):
    image_list = []

    Label(frame1, text="Original").place(x=10, y=10)
    Label(frame1, text="Style1").place(x=360, y=10)
    Label(frame1, text="Style2").place(x=710, y=10)
    Label(frame1, text="Style3").place(x=10, y=345)
    Label(frame1, text="Style4").place(x=360, y=345)
    Label(frame1, text="Style5").place(x=710, y=345)

    image_load = ImageTk.PhotoImage(Img.fromarray(np.zeros((300, 300, 3), dtype=np.uint8)))
    label_load = Label(frame1, width=300, height=300)
    set_label_image(label_load, image_load)
    label_load.place(x=10, y=30)
    label_gen1 = Label(frame1, width=300, height=300)
    set_label_image(label_gen1, image_load)
    label_gen1.place(x=360, y=30)
    label_gen2 = Label(frame1, width=300, height=300)
    set_label_image(label_gen2, image_load)
    label_gen2.place(x=710, y=30)
    label_gen3 = Label(frame1, width=300, height=300)
    set_label_image(label_gen3, image_load)
    label_gen3.place(x=10, y=370)
    label_gen4 = Label(frame1, width=300, height=300)
    set_label_image(label_gen4, image_load)
    label_gen4.place(x=710, y=370)
    label_gen5 = Label(frame1, width=300, height=300)
    set_label_image(label_gen5, image_load)
    label_gen5.place(x=360, y=370)

    label_list = [label_load, label_gen1, label_gen2, label_gen3, label_gen4, label_gen5]

    Button(frame1, command=lambda: load_button(label_list, image_list), text='Load').place(x=270, y=0)
    Button(frame1, command=lambda: save_picture(0), text='Save').place(x=620, y=0)
    Button(frame1, command=lambda: save_picture(1), text='Save').place(x=970, y=0)
    Button(frame1, command=lambda: save_picture(2), text='Save').place(x=270, y=340)
    Button(frame1, command=lambda: save_picture(3), text='Save').place(x=620, y=340)
    Button(frame1, command=lambda: save_picture(4), text='Save').place(x=970, y=340)

def compose_frame2(frame2):
    image_fg = ImageTk.PhotoImage(Img.fromarray(np.zeros((640, 640, 3), dtype=np.uint8)))
    label_fg = Label(frame2, width=320, height=600)
    set_label_image(label_fg, image_fg)
    label_fg.place(x=160, y=30)
    label_mask = Label(frame2, width=320, height=600)
    set_label_image(label_mask, image_fg)
    label_mask.place(x=600, y=30)

    Label(frame2, text="Image").place(x=160, y=0)
    Label(frame2, text="Mask").place(x=610, y=0)
    # Label(frame2, text="Rendered Mesh").place(x=710, y=0)
    Button(frame2, command=lambda: load_button2(label_fg, 0), text='Load Image').place(x=420, y=0)
    Button(frame2, command=lambda: load_button2(label_mask, 1), text='Load Mask').place(x=870, y=0)
    Button(frame2, command=lambda: pifu_eval(), text='Estimate Mesh').place(x=400, y=650)
    Button(frame2, command=lambda: view_mesh(), text='View Estimated Mesh').place(x=600, y=650)

def compose_frame3(frame3):
    pass

def compose_ui(window):
    notebook = ttk.Notebook(window, width=1080, height=720)
    notebook.pack()

    frame1=Frame(window)
    notebook.add(frame1, text="Background Cartoonization")
    compose_frame1(frame1)

    frame2=Frame(window)
    notebook.add(frame2, text="Mesh Reconstruction")
    compose_frame2(frame2)

    # label2=Label(frame2, text="페이지2의 내용")
    # label2.pack()

    frame3=Frame(window)
    notebook.add(frame3, text="MIXAMO Rigging")
    compose_frame3(frame2)
    # label3=Label(frame3, text="페이지3의 내용")
    # label3.pack()

    frame4=Frame(window)
    notebook.add(frame4, text="Blender Animating")

    label4=Label(frame4, text="페이지4의 내용")
    label4.pack()

def start_window():
    window = Tk()
    window.title("Anime Asset Maker")
    window.geometry("1080x720+100+100")
    window.resizable(False, False)
    compose_ui(window)
    window.mainloop()