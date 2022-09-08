#!/usr/bin/python
import numpy
import math
from PIL import Image

def gen_pattern(width: int, height: int):
    """Generate random dots

    Args:
        width (int): with of the image
        height (int): height of the image

    Returns:
        _type_: returns array of random dots
    """    
    return numpy.random.randint(0, 256, (int(math.ceil(width)), int(math.ceil(height))))

def autostereogram_from_file_path(image: str, output = "output.png", pattern_div = 8, invert = -1, resize = (1024, 1024)):
    """Generate stereogram from image file path

    Args:
        image (str): Image path
        output (str, optional): _description_. Defaults to "output.png".
        pattern_div (int, optional): _description_. Defaults to 8.
        invert (int, optional): _description_. Defaults to -1.
    """    
    autostereogram_from_image(Image.open(image), output, pattern_div, invert, resize = (1024, 1024))

def autostereogram_from_image(image: Image, output = "output.png", pattern_div = 8, invert = -1, resize = (1024, 1024)):
    """Generate stereogram from image

    Args:
        image (PIL.Image): Image
        output (str, optional): _description_. Defaults to "output.png".
        pattern_div (int, optional): _description_. Defaults to 8.
        invert (int, optional): _description_. Defaults to -1.
        resize (tuple, optional): _description_. Defaults to (1024, 1024).
    """    
    # Resize to visible size
    if(resize):
        image = image.resize(resize)

    depth_map = image.convert("RGB")
    depth_data = depth_map.load()

    out_img = Image.new("L", depth_map.size)
    out_data = out_img.load()

    pattern_width = depth_map.size[0] / pattern_div
    pattern = gen_pattern(pattern_width, depth_map.size[1])

    # Create stereogram
    for x in range(0, depth_map.size[0]):
        for y in range(0, depth_map.size[1]):

            if x < pattern_width:
                out_data[x, y] = int(pattern[x, y])  # Use generated pattern
            else:
                shift = depth_data[x, y][0] / pattern_div  # 255 is closest
                out_data[x, y] = out_data[x - pattern_width + (shift * invert), y]

    out_img.save(output)