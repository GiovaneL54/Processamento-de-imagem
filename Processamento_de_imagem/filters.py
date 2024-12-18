from PIL import Image, ImageFilter

def apply_filter(image_path, filter_type):
    image = Image.open(image_path)

    if filter_type == 'BlUR':
        image = image.filter(ImageFilter.BLUR)
    elif filter_type == 'CONTOUR':
        image = image.filter(ImageFilter.CONTOUR)
    elif filter_type == 'DETAIL':
        image = image.filter(ImageFilter.DETAIL)
    else:
        raise ValueError('Unsupported filter type')
    return image
