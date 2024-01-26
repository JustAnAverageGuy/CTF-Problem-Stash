from PIL import Image, ImageDraw

image_name = 1

def create_grid(binary_string):
    image_size = (200, 200)  
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)
    positions = [(0, 0), (100, 0), (0, 100), (100, 100)]
    for i, char in enumerate(binary_string):
        position = positions[i]
        color = "black" if char == "1" else "white"
        draw.rectangle([position, (position[0] + 100, position[1] + 100)], fill=color)
    global image_name
    image.save(f"{image_name}.png")
    image_name += 1

def create_gif():
    images = []
    image_paths = []
    for i in range(len(b)//4):
        image_paths.append(f"{i+1}.png")
    for image_path in image_paths:
        img = Image.open(image_path)
        images.append(img)
    images[0].save(
        "chall.gif",
        save_all=True,
        append_images=images[1:],
        duration = 500,
        loop=1  
        )

FLAG = "COPS{0_4nd_1}"
b = ""
for i in FLAG:
    b += "{:08b}".format(ord(i))

print(b)

for i in range(0, len(b), 4):
    create_grid(b[i:i+4])

create_gif()

