from PIL import Image

def encode_lsb(image_path, message):

    image = Image.open(image_path)
    pixels = image.load()

    if len(message) * 8 > image.width * image.height:
        raise ValueError("Message is too long to fit within the image.")

    binary_message = ''.join(format(ord(char), '08b') for char in message)

    char_index = 0

    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]
            if char_index < len(binary_message):
                if r > g and g > b:
                    g = (g & 0xFD) | (int(binary_message[char_index]) << 1)
                    char_index += 1
            pixels[x, y] = (r, g, b, a)
    encoded_image_path = "chall.png"
    image.save(encoded_image_path)

image_path = "org.png"

with open("flag.txt", "r") as f:
    flag = f.read().strip()

assert len(flag) == 21

encode_lsb(image_path, flag)
