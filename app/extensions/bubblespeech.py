from flask import Blueprint, request, send_file, render_template

from io import BytesIO

from PIL import Image, ImageSequence


bp = Blueprint("bubblespeech", __name__, url_prefix="/bubblespeech")

@bp.route("/generate", methods=["POST", "GET"])
def generate():
    if request.method == "POST":

        image = Image.open(request.files["input_image"].stream)
        bubble = Image.open("assets/bubble.png")

        hsize = int( (image.size[0] / float(bubble.size[0])) * float(bubble.size[1]) )


        bubble = bubble.resize((image.size[0], hsize))

        tier_bubble = bubble.size[1] // 4

        if image.format.lower() == "gif":
            gif_output = []
            duration = 0
            for frame in ImageSequence.Iterator(image):
                im = Image.new("RGBA", (frame.size[0], frame.size[1] + tier_bubble))
                im.paste(frame, (0, tier_bubble))
                im.paste(bubble, (0,0), mask=bubble)
                gif_output.append(im)
                duration += frame.info['duration']

            img_io = BytesIO()
            duration = duration / 1000
            gif_output[0].save(img_io, 'GIF', save_all = True, append_images = gif_output[1:], optimze= False,duration=duration, loop=0)

            img_io.seek(0)

            return send_file(img_io, mimetype="image/gif")


        else:
            im = Image.new("RGBA", (image.size[0], image.size[1] + tier_bubble))
            im.paste(image, (0, tier_bubble))

            im.paste(bubble, (0, 0),mask=bubble)

            img_io = BytesIO()
            im.save(img_io, 'PNG')
            img_io.seek(0)

            return send_file(img_io, mimetype="image/png")
        # return 'zebi'
    else:
        return "La requête doit être en POST"

@bp.route("/")
def index_page():
    return render_template("generate.html")
