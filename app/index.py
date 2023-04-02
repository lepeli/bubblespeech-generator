from flask import Flask

from extensions import bubblespeech

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
@app.route("/")
def test():

    return "aa"
app.register_blueprint(bubblespeech.bp)

if __name__ == "__main__":

    app.run(port=4545, debug=True)