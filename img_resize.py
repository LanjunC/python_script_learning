from PIL import Image
import sys
import util


def img_resize(file, w, h, quality=95):
    img = Image.open(file)
    resize = img.resize((w, h), Image.ANTIALIAS)
    resize.save(util.DEFAULT_DIR + 'resized_wh.jpg', 'jpeg', quality=quality)


def img_resize_scaling(file, ratio, quality=95):
    img = Image.open(file)
    w, h = img.size
    newW, newH = w * ratio // 100, h * ratio // 100
    resize = img.resize((newW, newH), Image.ANTIALIAS)
    resize.save(util.DEFAULT_DIR + 'resized_scaling.jpg',
                'jpeg', quality=quality)


def img_compress(file, quality=95):
    img = Image.open(file)
    img.save(util.DEFAULT_DIR + 'compressed.jpg', 'jpeg', quality=quality)


if __name__ == '__main__':
    util.mkdir_is_not_exist()
    img_compress(util.get_target_file_from_argv1(), 50)
