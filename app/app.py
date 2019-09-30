

from flask import Flask, request, Response, abort
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
        db = random.choice(list(all_fortunes.keys()))
        fortune = random.choice(all_fortunes[db])
        return Response(fortune, mimetype='text/plain')

@app.route("/api/fortune/<fortune_file>")
def get_random_fortune_from_file(fortune_file):
        if fortune_file not in all_fortunes.keys():
            abort(404)
        fortune = random.choice(all_fortunes[fortune_file])
        return Response(fortune, mimetype='text/plain')

@app.route("/api/fortune/list")
def list_all_fortune_files():
    list_of_fortune_dbs = all_fortunes.keys()
    return Response(list_of_fortune_dbs)

@app.route('/<path:path>')
def catch_all(path):
    abort(404)

#@app.errorhandler(404)
#def page_not_found(error):
#   return render_template('404.html', title = '404'), 404

if __name__ == "__main__":
    app.run()



# Routes
# /quote
# Returns a random quote from all available databases
# Query String / Parameters:
#    ?format={txt|json|html}

# /quote/{database}
# Returns a quote from the specific database requested.
