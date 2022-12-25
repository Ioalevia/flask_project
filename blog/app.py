from flask import Flask, request, g
from time import time
from werkzeug.exceptions import BadRequest

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return "Hello!", 200

@app.errorhandler(404)
def handler_404(error):
    app.logger.error(error)
    return '404'

@app.before_request
def process_before_request():
    g.start_time = time()

@app.after_request
def process_after_request(response):
    if hasattr(g, "start_time"):
        response.headers["process-time"] = time() - g.start_time
    return response

@app.route("/power/")
def power_value():
    x = request.args.get("x") or ""
    y = request.args.get("y") or ""
    if not (x.isdigit() and y.isdigit()):
        app.logger.info("invalid values for power: x=%r and y=%r", x, y)
        raise BadRequest("please pass integers in `x` and `y` query params")
    x = int(x)
    y = int(y)
    result = x ** y
    app.logger.debug("%s ** %s = %s", x, y, result)
    return str(result)

