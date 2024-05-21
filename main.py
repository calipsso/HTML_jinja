from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    user = "Kamil"
    year = 0
    return render_template(template_name_or_list="index.html", user = user, year = year )


@app.route("/order-coffe")
def order_coffe():
    return render_template("order-coffe.html")

if __name__ == "__main__":
    app.run(debug=True)