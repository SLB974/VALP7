from app import app


@app.route("/")
@app.route("/index")
def index():
    return "Bienvenue mon enfant, je suis Grandpy, le bot qui répond à toutes \
        tes questions. Veux-tu me donner une adresse ?"
