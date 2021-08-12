import torch
import torchvision.transforms as transforms

def predict_cartoon(image_load):
    cartoongan = CartoonGANGenerator().to(device)
    checkpoint = torch.load('./cartoongan', map_location=device)
    cartoongan.load_state_dict(checkpoint['generator_state_dict'])
    cartoongan.eval()

    animegan = CartoonGANGenerator().to(device)
    checkpoint = torch.load('./animegan', map_location=device)
    animegan.load_state_dict(checkpoint['generator_state_dict'])
    animegan.eval()

    to_tensor = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
    ])
    to_pil = transforms.Compose([
        transforms.Normalize(mean=(-1, -1, -1), std=(2, 2, 2)),
        transforms.ToPILImage()
    ])


    image = Image.open(file_path)
    image = image.crop((0, 0, image.size[0] - image.size[0] % 4, image.size[1] - image.size[1] % 4))

    image = to_tensor(image)
    image = torch.unsqueeze(image, 0).to(device)

    output = generator(image).detach().cpu()[0]
    output = to_pil(output)

