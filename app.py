from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='VTM Home Page')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About')

@app.route('/estimate', methods=['GET'])
def estimate():
    return render_template('estimate.html', pageTitle='Estimate')

def calculate_total_cost(radius,height):
    pi = 3.14
    top = pi * radius ** 2 
    side = 2 * (pi * (radius * height))
    totalinch = top + side
    totalsqfeet = totalinch/144
    material = totalsqfeet * 25
    labor = totalsqfeet * 15
    return "{:.2f}".format(material + labor)

@app.route('/result', methods=['POST'])
def add():
    if request.method == 'POST':
        radius = int(request.form['radius'])
        height = int(request.form['height'])
        totalcost = calculate_total_cost(radius,height)
        print(totalcost)
    return render_template('estimate.html', totalCost = totalcost)



if __name__ == '__main__':
    app.run(debug=True)