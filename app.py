

from flask import Flask




app = Flask(__name__)

@app.route("/")
def home():
        return "A simple quote service with API"

@app.route("/api")
def api():
        return "API Statistics"

@app.route("/api/quote")
def quote():
        return "A random quote goes here."

@app.route("/api/quote/monarch")
def quote_monarch():
        return "A Monarch quote"



if __name__ == "__main__":
    app.run(debug=True)




# Routes
# /quote
# Returns a random quote from all available databases
# Query String / Parameters:
#    ?format={txt|json|html}

# /quote/{database}
# Returns a quote from the specific database requested.
