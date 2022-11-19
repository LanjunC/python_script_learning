from PIL import Image
import os
import sys
import uuid


def img_resize(file, w, h, quality=95):
    img = Image.open(file)
    resize = img.resize((w, h), Image.ANTIALIAS)
    resize.save('resized_wh.jpg', 'jpeg', quality=quality)


def img_resize_scaling(file, ratio, quality=95):
    img = Image.open(file)
    w, h = img.size
    newW, newH = w * ratio // 100, h * ratio // 100
    resize = img.resize((newW, newH), Image.ANTIALIAS)
    resize.save('resized_scaling.jpg', 'jpeg', quality=quality)


def img_compress(file, quality=95):
    img = Image.open(file)
    img.save('compressed.jpg', 'jpeg', quality=quality)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Please provide the file name.")
        exit()
    filename = sys.argv[1]
    img_compress(filename, 50)
