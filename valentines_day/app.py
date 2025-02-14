from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", show_letter=False)

@app.route("/show_letter")
def show_letter():
    return render_template("index.html", show_letter=True)

if __name__ == "__main__":
    app.run(debug=True)
