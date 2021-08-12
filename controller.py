from tkinter import *
from tkinter import filedialog
from PIL import Image as Img
from PIL import ImageTk

from model_predict import *


def set_label_image(label, image):
    label.image = image
    label.configure(image=image)

def load_button(label_list, image_list):
    image_load = load_picture(label_list[0])
    image_load_tk = ImageTk.PhotoImage(image_load)
    set_label_image(label_list[0], image_load_tk)

    cartoons = predict_cartoon(image_load)

def load_picture(label_load):
    file_name = filedialog.askopenfilename(initialdir=".", title="Select file",
        filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"),))
    return Img.open(file_name)

def save_picture():
    file_name = filedialog.asksaveasfilename(initialdir="/", title="Select file",
        filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"),))
    print(file_name)