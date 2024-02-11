from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return  render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/admin')
def admin():
    return render_template("admin.html")

@app.route('/ticket')
def ticket():
    return render_template("ticket.html")



if __name__ == "__main__":
    app.run(debug='True')