from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database config
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="OnePunchMan@1",
    database="minedb"
)


# Make the form available at the root URL ('/')
@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    contact = request.form['contact']
    location = request.form['location']
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO user_info (name, contact, location) VALUES (%s, %s, %s)",
        (name, contact, location)
    )
    db.commit()
    cursor.close()
    return "Data inserted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
