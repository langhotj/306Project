__author__ = 'TJ Langhorne '

# imports
import sqlite3
from flask import Flask, render_template
from flask import request, redirect, url_for

# instantiate
app = Flask(__name__)


# route for handling the login page logic
@app.route('/')
def index():

    return render_template('index.html')

@app.route('/reserve.html', methods=['GET', 'POST'])
def reserve():
    id = ''
    numberofrooms = ''
    address = ''
    success = False

    if request.method == 'GET':
        conn = sqlite3.connect('306.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM buildings''')
        row = c.fetchone()

        if row:
            id = row[0]
            numberofrooms = row[1]
            address = row[2]

        conn.close()
    if request.method == 'POST':
        id = request.form['id']
        numberofrooms = request.form['numberofrooms']
        address = request.form['address']
        success = True

        conn = sqlite3.connect('306.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM buildings''')
        row = c.fetchone()
        if row:
            c.execute(
                '''UPDATE buildings SET numberofrooms = ?, address = ? WHERE id = ?''',
                (numberofrooms, address, id))
        else:
            c.execute('''INSERT INTO Members VALUES (?, ?, ?''',
                      (id, numberofrooms, address))
        conn.commit()
        conn.close()
    return render_template('reserve.html', id=id, numberofrooms=numberofrooms, address=address)

@app.route('/aboutus.html')
def aboutus():
    return render_template('aboutus.html')

@app.route('/contactus.html')
def contactus():
    return render_template('contactus.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    id = ''
    numberofrooms = ''
    address = ''
    success = False

    if request.method == 'GET':
        conn = sqlite3.connect('306.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM buildings''')
        row = c.fetchone()

        if row:
            id = row[0]
            numberofrooms = row[1]
            address = row[2]

        conn.close()
    if request.method == 'POST':
        id = request.form['id']
        numberofrooms = request.form['numberofrooms']
        address = request.form['address']
        success = True

        conn = sqlite3.connect('306.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM buildings''')
        row = c.fetchone()
        if row:
            c.execute(
                '''UPDATE buildings SET numberofrooms = ?, address = ? WHERE id = ?''',
                (numberofrooms, address, id))
        else:
            c.execute('''INSERT INTO Members VALUES (?, ?, ?''',
                      (id, numberofrooms, address))
        conn.commit()
        conn.close()

    return render_template('search.html', buildings = buildings)
if __name__ == "__main__":
    app.run(debug=False)
