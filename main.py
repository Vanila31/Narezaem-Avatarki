from PIL import Image

monro_image = Image.open("monro.jpg")
red, green, blue = monro_image.split()
monro_merged = Image.merge("RGB", (red, green, blue))
red_coord_1 = (50, 0, red.width, red.height)
red_segment_1 = red.crop(red_coord_1)
red_coord_2 = (25, 0, red.width-25, red.height)
red_segment_2 = red.crop(red_coord_2)
red = Image.blend(red_segment_1, red_segment_2, 0.5)

blue_coord_1 = (0, 0, blue.width-50, blue.height)
blue_segment_1 = blue.crop(blue_coord_1)
blue_coord_2 = (25, 0, blue.width-25, blue.height)
blue_segment_2 = blue.crop(blue_coord_2)
blue = Image.blend(blue_segment_1, blue_segment_2, 0.5)

green_coord = (25, 0, green.width-25, green.height)
green = green.crop(green_coord)
monro_crop_merge = Image.merge("RGB", (red, green, blue))
monro_crop_merge.save("monro_crop_merge.png")
monro_crop_merge.thumbnail((80, 80))
monro_crop_merge.save("monro_ava.png")



