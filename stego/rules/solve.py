from PIL import Image

def decode_lsb(image_path, og_image):
    image = Image.open(image_path)
    image1 = Image.open(og_image)
    pixels1 = image1.load()
    pixels = image.load()
    char_index = 0
    flag = ""
    for y in range(image1.height):
        for x in range(image1.width):
            r1,g1,b1,a1 = pixels1[x,y]
            r, g, b, a = pixels[x, y]
            if char_index < 8*21:
                if r1 > g1 and g1 > b1:
                    flag += str((g >> 1)&1)
                    char_index += 1
    b = ''.join(chr(int(flag[i:i+8],2)) for i in range(0,len(flag),8))
    print(b)

image_path = "chall.png"
og_image = "org.png"

decode_lsb(image_path, og_image)
