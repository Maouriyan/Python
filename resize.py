from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import argparse
import os
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

parser = argparse.ArgumentParser()
parser.add_argument('--image_dir', help='Directory of images to resize')
args = parser.parse_args()

#image_dir = os.getcwd() + "/" + args.image_dir
image_dir = "/home/mohak/Desktop/WORK/ocr images/metal_plate_cargo" 
out_dir = "/home/mohak/Desktop/WORK/ocr images/650x450"

for f in os.listdir(image_dir):
    filename = os.fsdecode(f)
    image = Image.open(image_dir + '/' + filename)
    print(image_dir + '/' + filename)
    height, width = image.size
    if width > 600:
        resize_amt = 600 / width
        new_height = 450
        image = image.resize((650, 400))
    image.save(out_dir + "/" + filename)
