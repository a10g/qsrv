

from flask import Flask, request, Response
import qsrv_func as q

import random

# configs - move to config.py eventually
fortune_path = 'fortunes'


app = Flask(__name__)

all_fortunes = q.get_fortunes(fortune_path)

@app.route("/")
def home():
        return "A simple quote service with API"

@app.route("/api")
def api():
        return "API Statistics"

@app.route("/api/fortune/random")
def get_random_fortune():
        return Response(all_fortunes, mimetype='text/plain')

@app.route("/api/fortune/<fortune_file>")
def get_random_fortune_from_file(fortune_file):
        fortune = random.choice(all_fortunes[fortune_file])
        return Response(fortune, mimetype='text/plain')


if __name__ == "__main__":
    app.run(debug=True)



# Routes
# /quote
# Returns a random quote from all available databases
# Query String / Parameters:
#    ?format={txt|json|html}

# /quote/{database}
# Returns a quote from the specific database requested.
