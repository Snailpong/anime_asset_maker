import torch
import torchvision.transforms as transforms
import numpy as np

from src.cartoon.model_cartoongan import CartoonGANGenerator
from src.cartoon.model_animegan import AnimeGANGenerator
from src.anime.model import Generator
from src.pifu.apps.eval2 import *

to_tensor = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
])
to_pil = transforms.Compose([
    transforms.Normalize(mean=(-1, -1, -1), std=(2, 2, 2)),
    transforms.ToPILImage()
])

# Preprocess image (normalization, to tensor)
def preprocess_image(image, device):
    image = image.convert("RGB").crop((0, 0, image.size[0] - image.size[0] % 4, image.size[1] - image.size[1] % 4))
    image = to_tensor(image)
    image = torch.unsqueeze(image, 0).to(device)

# Predict CartoonGAN, AnimeGAN
def predict_cartoon_anime(image):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    cartoongan = CartoonGANGenerator().to(device)
    checkpoint = torch.load('./src/cartoon/cartoongan', map_location=device)
    cartoongan.load_state_dict(checkpoint['generator_state_dict'])
    cartoongan.eval()

    animegan = AnimeGANGenerator().to(device)
    checkpoint = torch.load('./src/cartoon/animegan', map_location=device)
    animegan.load_state_dict(checkpoint['generator_state_dict'])
    animegan.eval()

    image = preprocess_image(image, device)
    output1 = to_pil(cartoongan(image).detach().cpu()[0])
    output2 = to_pil(animegan(image).detach().cpu()[0])

    return [output1, output2]

# Predict AnimeGAN2
def predict_anime2(image):
    torch.backends.cudnn.enabled = False
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    styles = ['Hayao', 'Paprika', 'Shinkai']
    outputs = []

    image = preprocess_image(image, device)

    for style in styles:
        net = Generator()
        net.load_state_dict(torch.load(f'./src/anime/pytorch_generator_{style}.pt', map_location="cpu"))
        net.to(device).eval()
        output1 = to_pil(net(image, False).detach().cpu()[0])
        outputs.append(output1)

    return outputs

# Predict PIFu
def predict_mesh(image_path, mask_path, obj_file_path):
    opt.batch_size = 1
    opt.norm_color = 'group'
    opt.load_netG_checkpoint_path = './src/pifu/checkpoints/net_G'
    opt.load_netC_checkpoint_path = './src/pifu/checkpoints/net_C'
    opt.test_folder_path = './sample_images'

    evaluator = Evaluator(opt)
    print(image_path, mask_path)
    print(os.path.dirname(image_path))
    data = evaluator.load_image(image_path, mask_path)
    evaluator.eval2(data, os.path.dirname(image_path), True, obj_file_path)