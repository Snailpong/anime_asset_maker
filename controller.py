from tkinter import *
from tkinter import filedialog
from PIL import Image as Img
from PIL import ImageTk

from model_predict import *

image_path = None
mask_path = None
cartoon_images = None

def set_label_image(label, image):
    label.image = image
    label.configure(image=image)

def set_predicted_cartoon(image_load, label_list):
    global cartoon_images

    cartoons = predict_cartoon(image_load)
    cartoon1 = predict_anime(image_load)
    cartoon_images = cartoons + cartoon1
    print(len(cartoon_images))
    image_gen1_tk = ImageTk.PhotoImage(cartoons[0])
    image_gen2_tk = ImageTk.PhotoImage(cartoons[1])
    image_gen3_tk = ImageTk.PhotoImage(cartoon1[0])
    image_gen4_tk = ImageTk.PhotoImage(cartoon1[1])
    image_gen5_tk = ImageTk.PhotoImage(cartoon1[2])
    set_label_image(label_list[1], image_gen1_tk)
    set_label_image(label_list[2], image_gen2_tk)
    set_label_image(label_list[3], image_gen3_tk)
    set_label_image(label_list[4], image_gen4_tk)
    set_label_image(label_list[5], image_gen5_tk)

def load_button(label_list, image_list):
    image_load = load_picture(label_list[0])
    image_load_tk = ImageTk.PhotoImage(image_load)
    set_label_image(label_list[0], image_load_tk)
    set_predicted_cartoon(image_load, label_list)

def load_button2(label, path):
    global image_path, mask_path
    
    file_name = filedialog.askopenfilename(initialdir=".", title="Select file",
        filetypes=(("png files", "*.png"),))
    image_load = Img.open(file_name)
    image_load_tk = ImageTk.PhotoImage(image_load)
    set_label_image(label, image_load_tk)

    if path == 0:
        image_path = file_name
    else:
        mask_path = file_name

def load_picture(label_load):
    file_name = filedialog.askopenfilename(initialdir=".", title="Select file",
        filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"),))
    return Img.open(file_name)

def save_picture(num):
    file_name = filedialog.asksaveasfilename(initialdir="/", title="Save to file",
        filetypes=(("png files", "*.png"),))
    print(file_name+'.png')

def pifu_eval():
    predict_mesh(image_path, mask_path)

def view_mesh():
    pass