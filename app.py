from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    menu = ["Quienes Somos","Servicios","Noticias","Contactos"]
    return render_template("index.html", menu = menu)

@app.route("/quienes")
def quienessomos():
    return render_template("quienes.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/noticias")
def noticias():
    return render_template("noticias.html")

@app.route("/contacto",methods=['GET','POST'])
def contacto():
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True)