from flask import Flask 
from config import DevConfig
app  = Flask(__name__)
app.config.from_object(DevConfig)

@app.route('/')
@app.route("/home")
def index():
    return "checking flask configuration"

if __name__ == "__main__":
    app.run()