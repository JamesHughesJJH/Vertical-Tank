from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About Mike')

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = float(form['radius'])
        height = float(form['height'])
        pi = 3.14
        toparea = pi * radius**2
        sidearea = 2*(pi*(radius*height))
        totalarea = toparea + sidearea
        sqfeet = totalarea/144
        matcost = 25
        totalmatcost = sqfeet*matcost
        laborcost = 15
        totallaborcost = sqfeet*laborcost
        estimate = totallaborcost+totalmatcost
        return render_template('estimate.html',quote=estimate)
    return render_template('estimate.html')


if __name__ == '__main__':
    app.run(debug=True)
