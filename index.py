from PIL import Image

image = Image.open("image.jpg")
bubble = Image.open("bubble.png")

hsize = int( (image.size[0] / float(bubble.size[0])) * float(bubble.size[1]) )


bubble = bubble.resize((image.size[0], hsize))

tier_bubble = bubble.size[1] // 4

im = Image.new("RGBA", (image.size[0], image.size[1] + tier_bubble))
im.paste(image, (0, tier_bubble))

im.paste(bubble, (0, 0),mask=bubble)

im.show()

im.save("output.png")