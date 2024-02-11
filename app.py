from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return  render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/artists')
def artists():
    return render_template("artists.html")

@app.route('/pricing')
def pricing():
    return render_template("pricing.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/buyticket')
def buyticket():
    return render_template("buyticket.html")



if __name__ == "__main__":
    app.run(debug='True')