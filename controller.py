from tkinter import *
from tkinter import filedialog
from PIL import Image as Img
from PIL import ImageTk

from model_predict import *

def set_label_image(label, image):
    label.image = image
    label.configure(image=image)

def set_predicted_cartoon(image_load, label_list):
    cartoons = predict_cartoon(image_load)
    image_gen1_tk = ImageTk.PhotoImage(cartoons[0])
    image_gen2_tk = ImageTk.PhotoImage(cartoons[1])
    set_label_image(label_list[1], image_gen1_tk)
    set_label_image(label_list[2], image_gen2_tk)

def load_button(label_list, image_list):
    image_load = load_picture(label_list[0])
    image_load_tk = ImageTk.PhotoImage(image_load)
    set_label_image(label_list[0], image_load_tk)
    set_predicted_cartoon(image_load, label_list)

def load_picture(label_load):
    file_name = filedialog.askopenfilename(initialdir=".", title="Select file",
        filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"),))
    return Img.open(file_name)

def save_picture():
    file_name = filedialog.asksaveasfilename(initialdir="/", title="Select file",
        filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"),))
    print(file_name)