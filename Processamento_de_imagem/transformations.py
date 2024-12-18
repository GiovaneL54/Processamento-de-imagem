from PIL import Image

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    image = image.resize((width, height))
    return image