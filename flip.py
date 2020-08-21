import os
import sys
from multiprocessing import Pool
from cv2 import cv2

if (len(sys.argv) != 2):
    raise Exception("Usage: python flip.py path/to/folder")

folder = sys.argv[1]
images = os.listdir(folder)


def flip(path, image):
    im = cv2.imread(os.path.join(path,image))
    im = cv2.rotate(im, cv2.ROTATE_180)
    name = os.path.splitext(image)[0] + "_new.jpg"
    new_path = os.path.join(path, (name))
    cv2.imwrite(new_path, im)
    


for i, image in enumerate(images):
    flip(folder, image)
    os.remove(os.path.join(folder,image))