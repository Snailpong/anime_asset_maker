from tkinter import *
from tkinter import filedialog
from PIL import Image as Img
from PIL import ImageTk
import pyrender
import trimesh

from model_predict import *

image_path = None
mask_path = None
cartoon_images = None

# Show image in label
def set_label_image(label, image):
    label.image = image
    label.configure(image=image)

# Predict and show cartoonizated photo
def set_predicted_cartoon(image_load, label_list):
    global cartoon_images

    cartoons = predict_cartoon_anime(image_load)
    cartoon1 = predict_anime2(image_load)
    cartoon_images = cartoons + cartoon1
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

# Button event for background frame
def load_button_bg(label_list):
    image_load = load_picture()
    image_load_tk = ImageTk.PhotoImage(image_load)
    set_label_image(label_list[0], image_load_tk)
    set_predicted_cartoon(image_load, label_list)

# Button event for mesh frame
def load_button_mesh(label, path):
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

# Load picture to estimate
def load_picture():
    file_name = filedialog.askopenfilename(initialdir=".", title="Select file",
        filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"),))
    return Img.open(file_name)

# Save predicted background image
def save_picture(num):
    file_name = filedialog.asksaveasfilename(initialdir=".", title="Save to file",
        filetypes=(("png files", "*.png"),))
    file_name += '.png'
    print(file_name)
    cartoon_images[num].save(file_name)

# Show predicted mesh with pyrender
def show_viewer(file_name):
    fuze_trimesh = trimesh.load(file_name)
    mesh = pyrender.Mesh.from_trimesh(fuze_trimesh)
    scene = pyrender.Scene()
    scene.add(mesh)
    pyrender.Viewer(scene, use_raymond_lighting=True)

# Predict picture to mesh and view predicted mesh
def pifu_eval():
    obj_file_path = filedialog.asksaveasfilename(initialdir=".", title="Save to file",
        filetypes=(("obj files", "*.obj"),))
    obj_file_path += ".obj"
    predict_mesh(image_path, mask_path, obj_file_path)
    show_viewer(obj_file_path)

# View selected mesh 
def view_mesh():
    file_path = filedialog.askopenfilename(initialdir=".", title="Select file",
        filetypes=(("obj files", "*.obj"),))
    show_viewer(file_path)