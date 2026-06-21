from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/booking")
def booking():
    return render_template("booking.html")


@app.route("/thank-you")
def thank_you():
    return render_template("thank-you.html")


if __name__ == "__main__":
    app.run(debug=True)