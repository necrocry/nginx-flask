from . import app

@app.route("/")
def index():
    return "<h1 style='color:blue'>Hello There!</h1>"