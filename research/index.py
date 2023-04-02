from PIL import Image
from PIL import ImageSequence

image = Image.open("input.gif")
bubble = Image.open("bubble.png")

hsize = int( (image.size[0] / float(bubble.size[0])) * float(bubble.size[1]) )


bubble = bubble.resize((image.size[0], hsize))

tier_bubble = bubble.size[1] // 4

if image.is_animated:
    gif_output = []
    duration = 0
    for frame in ImageSequence.Iterator(image):
        im = Image.new("RGBA", (frame.size[0], frame.size[1] + tier_bubble))
        im.paste(frame, (0, tier_bubble))
        im.paste(bubble, (0,0), mask=bubble)
        gif_output.append(im)
        duration += frame.info['duration']

    duration = duration / 1000
    gif_output[0].save('output.gif', save_all = True, append_images = gif_output[1:], optimze= False,duration=duration, loop=0)

else:
    im = Image.new("RGBA", (image.size[0], image.size[1] + tier_bubble))
    im.paste(image, (0, tier_bubble))

    im.paste(bubble, (0, 0),mask=bubble)

    im.show()

    im.save("output.png")