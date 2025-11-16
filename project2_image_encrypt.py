from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)

    img.save("encrypted.png")
    print("Image Encrypted as encrypted.png")

key = 50
encrypt_image("input.png", key)
