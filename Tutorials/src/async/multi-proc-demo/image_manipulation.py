# https://pillow.readthedocs.io/en/stable/
import os

from PIL import Image, ImageFilter

# image_1 = Image.open('300/photo-1530224264768-7ff8c1789d79_300.jpg')
# image_1.rotate(90).save('300/photo-1530224264768-7ff8c1789d79_300_mod.jpg')
# image_1.convert(mode='L').save('300/photo-1530224264768-7ff8c1789d79_300_mod.jpg')
# image_1.filter(ImageFilter.GaussianBlur(2)).save('300/photo-1530224264768-7ff8c1789d79_300_mod.jpg')


size_300 = (300, 300)

for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.save(f'300/{fn}_300{fext}')
        i.thumbnail(size_300)

# for f in os.listdir('.'):
#     if f.endswith('.jpg'):
#         i = Image.open(f)
#         fn, fext = os.path.splitext(f)
#         i.save(f'pngs/{fn}.png')

# image_1 = Image.open('photo-1524429656589-6633a470097c.jpg')
# image_1.show()
# image_1.save('photo-1524429656589-6633a470097c.png')
